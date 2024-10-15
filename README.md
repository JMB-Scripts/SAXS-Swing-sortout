# Swing-sortout
To sort out the output from SEC-SAXS experiment collected on Swing beamline at Soleil synchrotron.
Usually, Foxtrot save all files in the same folder, this script allows you to sort the files into the a designated folder.
## Goal 
For Users of the Swing Beamline at Soleil synchrotron. 
Foxtrot generate all files in a single directories where you find buffer frames, unsubtracted elution frames, subtracted elution frames, and average frames.
The script is made to cleanup the directory and put: 

1- Buffer frames in a Buffer folder 

2- Unsubtracted elution frames in the Raw folder 

3- Subtracted elution frames in the Sub folder 

4- Average frame in the Ave Folder 

5- Process directory will be created for the analysis (Dammin, EOM,  ...) of your experiment.

(6- A peak folder can be created to add if you know the file number of the peak) 

##  Manual 
Place the script in the directory above folder you want to organize.
 
  - Parent_Directory/ 
  - Swing-sortout.py
      - Pc_sec_SaxsCurves/
                 - Your files

## Running the Script:

 python Swing-sortout.py MyFolder/

## Output 
 The script will create the directories 'Ave', 'Buffer', 'Raw', 'Sub', 'Process', (and 'Peak') if they don't exist.
It will move files into the appropriate directories based on their names and contents.

## In addition Renumbering step is done for the Sub files:

The script will renumber files in the 'Sub' directory, replacing the numbers in curly braces to three-digit format (001, 002, etc.).

## Optional: 

Interesting Frames:
 The script will ask if you want to copy interesting frames to the 'Peak' directory for merging.
 Enter 'y' to proceed and provide the range of frame numbers
