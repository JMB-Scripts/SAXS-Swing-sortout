## Goal 
# For Users of the Swing Beamline at Soleil synchrotron. 
# Foxtrot generate all files in a single directories where you find buffer frames, unsubtracted elution frames, subtracted elution frames, and average frames.
# The script is made to cleanup the directory and put: 
# 1- Buffer frames in a Buffer folder 
# 2- Unsubtracted elution frames in the Raw folder 
# 3- Subtracted elution frames in the Sub folder 
# 4- Average frame in the Ave Folder 
# 5- Process directory will be created for the analysis (Dammin, EOM,  ...) of your experiment.
# (6- A peak folder can be created to add if you know the file number of the peak) 
##  Manual 
# Place the script in the directory above folder you want to organize.
#   - Parent_Directory/ 
#   - Swing-sortout.py
#       - Pc_sec_SaxsCurves/
#                   - Your files
## Running the Script:
# python Swing-sortout.py MyFolder/
## Output 
# The script will create the directories 'Ave', 'Buffer', 'Raw', 'Sub', 'Process', and 'Peak' if they don't exist.
# It will move files into the appropriate directories based on their names and contents.
## In addition Renumbering step is done for the Sub files:
# The script will renumber files in the 'Sub' directory, replacing the numbers in curly braces to three-digit format (001, 002, etc.).
## Optional: 
# Interesting Frames:
# The script will ask if you want to copy interesting frames to the 'Peak' directory for merging.
# Enter 'y' to proceed and provide the range of frame numbers
#
# Jean-Marie Bourhis et Chat GPT because I'm still a "tanche" in Python programming 

import os
import sys
import shutil
import re

# Get the folder name from command-line argument
if len(sys.argv) != 2:
    print("Usage: python Swing-sortout.py <folder_name>")
    sys.exit(1)

folder_name = sys.argv[1]
script_directory = os.path.dirname(os.path.abspath(__file__))

folder_path = os.path.join(script_directory, folder_name)

if not os.path.exists(folder_path):
    print(f"Folder '{folder_name}' does not exist in the parent directory.")
    sys.exit(1)

os.chdir(folder_path)

# Create directories if they don't exist
directories = ['Ave', 'Buffer', 'Raw', 'Sub', 'Process']

for directory in directories:
    dir_path = os.path.join(folder_path, directory)
    if not os.path.exists(dir_path):
        os.mkdir(dir_path)
    else:
        print(f"""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
REMARKS: The {directory} folder exists.
Backup the data, otherwise they will be crushed without mercy.
Then relaunch me!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""")
        resp = input(f"Do you want to continue anyway? (y/n): ")
        if resp.lower() == 'n':
            exit()

# Move files to appropriate directories
for filename in os.listdir():
    if filename.startswith('Av') and filename.endswith('.dat'):
        shutil.move(filename, 'Ave')
    elif 'Buffer' in filename and filename.endswith('.dat'):
        shutil.move(filename, 'Buffer')
    elif filename.endswith('.dat') and not 'Sub' in filename:
        shutil.move(filename, 'Raw')
    elif filename.startswith('Sub') and filename.endswith('.dat'):
        shutil.move(filename, 'Sub')

print("###########################")
print("Renumbering is starting, please wait...")
print("###########################")

# Renumber Sub files
for filename in os.listdir('Sub'):
    if filename.startswith('Sub'):
        match = re.search(r'\{(\d+)\}', filename)
        if match:
            number = int(match.group(1))
            new_number = str(number).zfill(3)
            new_filename = filename.replace(match.group(), f"{{{new_number}}}")
            os.rename(os.path.join('Sub', filename), os.path.join('Sub', new_filename))

print("###########################")
print("Renumbering is DONE")
print("###########################")

# Move interesting frames to Peak directory
resp = input("Do you want to put interesting frames in the Peak directory to merge them? (y/n): ")
if resp.lower() == 'y':
    i = int(input("Enter the first frame number: "))
    limit = int(input("Enter the last frame number: "))
    
    if not os.path.exists('Peak'):
        os.mkdir('Peak')
    else:
        print("""
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
REMARKS: The Peak folder exists.
Backup the data, otherwise they will be crushed without mercy.
Then relaunch me!
!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
""")
        resp = input(f"Do you want to continue anyway? (y/n): ")
        if resp.lower() == 'n':
            exit()
    
    while i <= limit:
        for filename in os.listdir('Sub'):
            if filename.startswith('Sub'):
                match = re.search(r'\{(\d+)\}', filename)
                if match:
                    number = int(match.group(1))
                    if number == i:
                        shutil.copy(os.path.join('Sub', filename), 'Peak')
        i += 1

    print("###########################")
    print("The files have been sorted out, interesting frames are under Peak.")
    print("It has been a pleasure.")
    print("Have a lovely day.")
    print("###########################")
else:
    print("###########################")
    print("The files have been sorted out.")
    print("It has been a pleasure.")
    print("Have a lovely day.")
    print("###########################")
