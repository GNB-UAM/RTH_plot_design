import sys
import os
from plot_interface import *
import subprocess

class Interface(QtWidgets.QMainWindow):

	def __init__(self, parent=None):
		QtWidgets.QMainWindow.__init__(self, parent)
		self.ui = Ui_MainWindow()
		self.ui.setupUi(self)

		# Buttons conectors
		self.ui.pushButton_plot.clicked.connect(self.pyplot_call)
		self.ui.pushButton_selectfile.clicked.connect(self.file_explorer)
		self.ui.pushButton_selectlast.clicked.connect(self.get_last)

	##############################
	#  Funcs for custom actions  #
	##############################
	def pyplot_call(self):
		print("func has been called!")

	def file_explorer(self):
		current_path = self.ui.textEdit_experiment.toPlainText()
		if current_path.find('s_data.txt') != -1:
			# We want to stay in the same day
			result = current_path.split('/')[-2]
			filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', 'data/'+result, 'Text files (*.txt);;All files (*)')[0]

		else:
			# No day choose yet
			filename = QtWidgets.QFileDialog.getOpenFileName(self, 'Select file', 'data', 'Text files (*.txt);;All files (*)')[0]
		
		self.ui.textEdit_experiment.setPlainText(filename)

	def get_last(self):
		folders = [f for f in os.listdir('data') if os.path.dirname(os.path.join('data', f))]
		folders.sort(key=lambda x: os.path.getmtime('data/'+x))
		onlyfiles = [f for f in os.listdir('data/'+folders[-1]) if os.path.isfile(os.path.join('data/'+folders[-1], f))]
		onlyfiles.sort(key=lambda x: os.path.getmtime('data/'+folders[-1]+'/'+x))
		self.ui.textEdit_experiment.setPlainText(os.getcwd()+"/data/"+folders[-1]+'/'+onlyfiles[-1])

if __name__ == "__main__":
	app = QtWidgets.QApplication(sys.argv)

	myapp = Interface()
	myapp.show()

	sys.exit(app.exec_())