# 
# This program changes the filenames in a given directory to lower case and appends 'file' to the beginning of each filename
import os
print ('Running the UNPOFORATOR!')
# Designates input folder location
in_path = 'c:/Users/sergioh/downloads/501Lab3/text_files/'
# Designates output folder
mypath = 'c:/Users/sergioh/downloads/501Lab3/text_files_fixed/'
if not os.path.isdir(mypath):
    os.makedirs(mypath)   
print ('Mischieve managed!')
# for loop tha goes through the folder 
for root, dirs, files in os.walk(in_path):
    for file_lower in files:

        file_lower = file_lower.lower()
        file_split = file_lower.split('.')
    	# changes input files by splitting and renaming as desired
        if file_split[1] == 'txt':
            os.rename(in_path + file_lower, mypath + "file_" + file_lower +'.txt')
        else:
            os.rename(in_path + file_lower, mypath + "file_" + file_split[0] + '.txt')

        
