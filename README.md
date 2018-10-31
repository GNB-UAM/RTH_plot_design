<a target="_blank" rel="noopener noreferrer" href="https://github.com/GNB-UAM/RTHybrid"> <img src="assets/logo_rthy.png?raw=true" width="100" height="100"> </a>&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;	
<a target="_blank" rel="noopener noreferrer" href="https://github.com/GNB-UAM"> <img src="assets/logo_gnb.png?raw=true" width="100" height="100"> </a>

# RTHybrid Plot Designer 
Auxiliary Qt project to design and test the UI of the RTHybrid Plot Tool

## RTHybrid
For more information about full RTHybrid please check out:

#### https://github.com/GNB-UAM/RTHybrid 

##### - Read RTHybrid project to use and cite this work
##### - Stable code of this repository is included in RTHybrid and is the one to use

## About
- Qt Creator is use to design rth_plot/mainwindow.ui
- With the .ui file plot_lib/plot_interface.py is created:
```
pyuic5 rth_plot/mainwindow.ui -o plot_lib/plot_interface.py
```
- plot_main.pyw manage the interface and call plot_lib/plot.py (the final program)
- plot_lib/ contains also the rest of the code use for plots

## How to include in RTHybrid
Just copy these files in RTHybrid root folder:
- plot_main.pyw
- plot.sh
- /plot_lib folder

## Requirements
- Qt5
- Python libraries (matplotlib, pandas, numpy...). All included in Anaconda 
