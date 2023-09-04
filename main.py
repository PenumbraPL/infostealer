from os import listdir, getcwd, mkdir
from shutil import rmtree
import g_drive_fun
from get_data import takeAllData

if 'data' in listdir(getcwd()):
		rmtree('data')	
mkdir('data')
takeAllData()

folder_id = g_drive_fun.uploadFolderGDrive('Web')
print('Folder ID: ', folder_id)

for file in listdir(getcwd() + '\\data'):
	g_drive_fun.uploadFileGDrive(file, folder_id.get('id'))

print('============== Finished Uploading =============')