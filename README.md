<a target="_blank" rel="noopener noreferrer" href="https://github.com/GNB-UAM/RTHybrid"> <img src="logo.png?raw=true" width="100" height="100"> </a>
<a target="_blank" rel="noopener noreferrer" href="https://github.com/GNB-UAM"> <img src="gnb.png?raw=true" width="100" height="100"> </a>

# RTH Plot Design 
Auxiliary Qt project to design and test the UI of the RTHybrid plot tool 

## RTHybrid
For more information about RTHybrid please check out:

#### https://github.com/GNB-UAM/RTHybrid 

#### Note: 
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
Just need to copy plot_main.pyw, plot.sh and plot_lib folder in RTHybrid root folder

## Requirements
- Qt5
- Python libraries (matplotlib, pandas, numpy...). All included in Anaconda 
