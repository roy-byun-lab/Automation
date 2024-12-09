import os
import move
from datetime import datetime
"""
Need modify your config
	DIR
"""

DIR = '/home/arif/Downloads/'

# all files in download folder
files_in_download_folders = os.listdir(DIR)

# moving
for single_file in files_in_download_folders:
    file_path = DIR + single_file

    if os.path.isfile(file_path):
        print("Moving ", single_file)

        move.move(single_file, file_path)

        print("Moved ", single_file)