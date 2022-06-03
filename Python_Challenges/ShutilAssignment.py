import shutil
import os

# set where the source of the files (Folder A)
source = '/Users/brian/OneDrive/Desktop/FolderA/'

# set the destination path to folder B
destination = '/Users/brian/OneDrive/Desktop/FolderB/'
files = os.listdir(source)

for i in files:
	# move files represented by 'i' to their new destination
	shutil.move(source+i, destination)