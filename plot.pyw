import sys
import os
from plot_lib.plot_interface import *
import subprocess

class Interface(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		# Qt
		QtWidgets.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Init and variables
		self.path_text = 'Select file...'
		self.current_path = self.path_text

		# Buttons conectors
		self.ui.pushButton_plot.clicked.connect(self.pyplot_call)
		self.ui.pushButton_selectfile.clicked.connect(self.file_explorer)
		self.ui.pushButton_selectlast.clicked.connect(self.get_last)

		self.ui.pushButton_selectlast.clicked.connect(self.cal_time)
		self.ui.pushButton_selectfile.clicked.connect(self.cal_time)
		self.ui.frecuency.valueChanged.connect(self.cal_time)


	##############################
	#  Funcs for custom actions  #
	##############################
	def pyplot_call(self):
		self.current_path = self.ui.textEdit_experiment.toPlainText()
		error_plot='None'
		program  = 'python3 plot_lib/plot.py'

		# File to plot
		program += ' -f ' + self.current_path
		if self.current_path=='' or self.current_path==self.path_text:
			error_plot='You have to select a file'
			self.ui.textEdit_experiment.setPlainText( self.path_text )

		# Jump points
		program += ' -j ' + str( self.ui.JumpPointsValue.value() )

		# Frecuency
		program += ' -fr ' + str ( self.ui.frecuency.value() )

		# Start and end poinst
		if self.ui.PlotAll.isChecked() == False:
			s = self.ui.spinBox_from_m.value()*60 + self.ui.spinBox_from_s.value()
			e = self.ui.spinBox_to_m.value()*60   + self.ui.spinBox_to_s.value()
			if (s>=e):
				error_plot='End time must be greater than start time'
			program += ' -s ' + str(s)
			program += ' -e ' + str(e)

		# Latency
		if self.ui.latency_on.isChecked() == True:
			program += ' -lat 1'
			
		# Drift
		program += ' -d 0 '

		# Errors
		if error_plot != 'None':
			QtWidgets.QMessageBox.warning(self, "Can't plot", error_plot)

		# Plot
		else:
			print(program)
			pid=os.fork()
			if pid==0: # new process
				os.system(program)
				exit()

	def file_explorer(self):
		self.current_path = self.ui.textEdit_experiment.toPlainText()
		if self.current_path.find('s_data.txt') != -1:
			# We want to stay in the same day
			result = self.current_path.split('/')[-2]
			filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', 'data/'+result, 'Text files (*.txt);;All files (*)')[0]

		else:
			# No day choose yet
			filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', 'data', 'Text files (*.txt);;All files (*)')[0]
		
		self.ui.textEdit_experiment.setPlainText(filename)
		self.current_path = self.ui.textEdit_experiment.toPlainText()

	def get_last(self):
		folders = [f for f in os.listdir('data') if os.path.dirname(os.path.join('data', f))]
		folders.sort(key=lambda x: os.path.getmtime('data/'+x))
		onlyfiles = [f for f in os.listdir('data/'+folders[-1]) if os.path.isfile(os.path.join('data/'+folders[-1], f))]
		onlyfiles.sort(key=lambda x: os.path.getmtime('data/'+folders[-1]+'/'+x))
		self.ui.textEdit_experiment.setPlainText(os.getcwd()+"/data/"+folders[-1]+'/'+onlyfiles[-1])
		self.current_path = self.ui.textEdit_experiment.toPlainText()

	def cal_time(self):
		if self.current_path=='' or self.current_path==self.path_text:
			self.ui.label_time.setText('Duration')
			return

		num_lines = sum(1 for line in open(self.current_path)) - 1
		segs = int (num_lines / self.ui.frecuency.value())
	
		if segs > 59:
			mins = int (segs/60)
			segs = int (segs-(mins*60))
			self.ui.label_time.setText(str(mins)+'m '+str(segs)+'s')
		else:
			self.ui.label_time.setText(str(segs)+'s')

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	myapp = Interface()
	myapp.show()

	sys.exit(app.exec_())