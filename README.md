# NeuroLux Software
## NeuroLux Bluetooth software installation:
All latest software can be found under Releases at https://github.com/NeuroLux-Inc/Neurolux-Software-Releases/releases/latest

Use the NeuroLux Bluetooth Installer.msi file for the NeuroLux software installation. This is the only file you will need to get started with your Bluetooth-enabled Neurolux devices. Install on a computer with a dedicated graphics card for optimal performance. A shortcut to the application folder will be found on your desktop.

Ensure use of BLE antenna provided with system to boost device connectivity.

### Pairing:
Search for devices, select ‘connect’ to pair with NNV###, EEG###, IMA###, MA###. Select ‘start data stream’ to begin viewing data.

### Data saving:
‘Begin recording’ will save to a SQLite database. Date in name of file will update on pressing begin ‘Begin recording’.‘New savefile every X sec’ sets how often a new csv (incrementally numbered) is created on export at end of session. At end of recording, click single database export to select a SQLite file to export to csv. Click batch export databases to select a parent folder in which to recursively export data from all databases found in tree. A new db is created each time start recording is pressed and for each unique device. Databases can be viewed in a SQLite viewer and manipulated as is. Note that the database needs to be sorted by time when queried, as it is not in order when saved initially. 

### Event Marking
Devices will be assigned a local event keyboard shortcut on connect, this shortcut can also be assigned by the user. A global event binding is also able to be assigned.

### Arduino Connection
An Arduino can be used to mark events and start/stop recording over serial communication. Connect to Arduinos by selecting the com port corresponding to the Arduino in the 'Serial Ports' drop down menu and selecting connect. By sending a 'g' over serial, a global event will be marked. Sending an 'r' will toggle starting and stopping recording data. Baud rate should be set to 9600.

### Plot Navigation
Shift + left click on plot = X axis zoom
Shift + right click on plot = X axis zoom out
Ctrl+ left click on plot = Y axis zoom
Ctrl+ right click on plot = Y axis zoom out

## Analysis

### First time setup:
1. Install a distribution of Anaconda following instructions at: https://docs.anaconda.com/free/anaconda/install/windows/
   Note: you do not need to check the box to add anaconda to PATH environment variable
2. Open the freshly installed annaconda navigator and launch Jupyter Notebook from the navigator menu
3. Navigate to the analysis script in the file browser on the left side of the window and double click to open the file

### Running the Python MA Analysis script:
1. Select the data you want to view by toggling the plots (plot_accel_x, plot_accel_y, etc) in the settings. Also select if you want to show HR and RR peaks (plot_HR_peaks, plot_RR_peaks). Select "scrolling" if you would like to zoom in to the data (recommended for viewing HR and RR peaks). Adjust "scroll_window" to zoom in or out. 

-------------------------------------------------------------------------------------------------

### Recommended settings for viewing overall data (no zoom):
plot_accel_x = True                 #plot x acceleration
plot_accel_y = True                 #plot y acceleration
plot_accel_z = True                 #plot z acceleration
plot_temperature = True             #plot temperature
plot_HR = True                      #plot heart rate
plot_RR = True                      #plot respiratory rate
plot_activity = True                #plot activity
plot_SQI = True 		    #plot signal quality index

-------------------------------------------------------------------------------------------------

### Recommended settings for viewing individual HR and RR peaks (with zoom):
plot_accel_x = True                 #plot x acceleration
plot_accel_y = True                 #plot y acceleration
plot_accel_z = True                 #plot z acceleration
plot_temperature = True             #plot temperature
plot_accel_z_clean = True           #plot z acceleration with motion artifacts removed
plot_hs_sh_raw = True               #plot shannon energy envelope of heart sound
plot_hs_sh_filtered = True          #plot shannon energy envelope of heart sound with LPF applied
plot_hs_lt = True                   #plot length transform of heart sound
plot_x_resp = True                  #plot x respiration data
plot_HR = True                      #plot heart rate
plot_RR = True                      #plot respiratory rate
plot_activity = True                #plot activity
plot_SQI = True                     #plot signal quality index

plot_HR_peaks = True                #plot HR peaks
plot_RR_peaks = True                #plot RR peaks

scrolling = True                    #produce additional interactive figure with scrolling 
scroll_window = 2                   #scrolling window size (seconds)

-------------------------------------------------------------------------------------------------

2. Click the triangular run button at the top of the file to begin analysis. 
3. Once you run the script you will be prompted to select the .csv files you want to analyze. Make sure you minimize the Jupyter Notebook to see the selection window. When selecting the files, make sure there is at least 1 minute of data in each .csv file. Also make sure there is not a large time gap (>5 min) between CSV files. The order of selecting the CSV files does not matter. Once selected, the code will execute for a minute or two.
4. After running the code, several files will appear in the folder of the original .csv files you selected for analysis. One of the files is a PNG plotting the heart rate, respiratory rate, and other characteristics over time. The rest of the files are CSV files containing numerical data. To verify that the MA device is producing viable data, ensure that the heart rate falls between 400 and 800 bpm and that the SQI consistently hovers above 50%. 
