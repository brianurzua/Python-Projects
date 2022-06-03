import shutil
import datetime
import os

src_Fol = '/Users/brian/OneDrive/Desktop/modified' # source file
dest_Fol = '/Users/brian/OneDrive/Desktop/DailyCopies' # Destination File

now = datetime.datetime.now() # gets current time
before = now - datetime.timedelta(hours=24) # gets time of 24 hours ago


allFiles = os.listdir(src_Fol) # lists out all files in directory

""" This for loop will create/grab file path and time of modification
	then with the if statement, it will compare time of modification and now.
	if the file has been modified in the last 24 hours then it will send that 
	file to the destination folder."""
def fileCheck():
	for i in allFiles:
		filePath = src_Fol+'/'+i
		timestamp = os.path.getmtime(filePath)
		dateMod = datetime.datetime.fromtimestamp(timestamp)

		if dateMod > before:
			destFile = dest_Fol+'/'+i
			shutil.move(filePath, dest_Fol)
			print('Files have been moved from {} to {}'.format(filePath, destFile))



if __name__ == '__main__':
	fileCheck()
