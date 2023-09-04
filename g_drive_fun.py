from flask import Flask, request
from g_drive_service import GoogleDriveService
from googleapiclient.errors import HttpError
from googleapiclient.http import MediaFileUpload
from datetime import datetime

app=Flask(__name__)


@app.get('/gdrive-files')
def getFileListFromGDrive():
    selected_fields="files(id,name,webViewLink)"
    g_drive_service=GoogleDriveService().build()
    list_file=g_drive_service.files().list(fields=selected_fields).execute()
    return {"files":list_file.get("files")}

@app.post('/new-file')
def createNewFileGDrive():
	g_drive_service = GoogleDriveService().build()
    	
	try:
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
		print("date and time =", dt_string)
		# !!!!!!!!!!!!!!!!!!!! ex. https://drive.google.com/drive/u/0/folders/[folder id]
		file_metadata = {'name': f'sd_{dt_string}.txt', 'parents': ['## folder id ##']}
		media = MediaFileUpload('./data/data.txt',
								mimetype='text/plain')
		file = g_drive_service.files().create(body=file_metadata, media_body=media,
										fields='id').execute()
		print(F'File ID: {file.get("id")}')

	except HttpError as error:
		print(F'An error occurred: {error}')
		file = None

	return file


@app.post('/upload-file/<string:folder>/<string:file_name>')
def uploadFileGDrive(file_name, folder):
	g_drive_service = GoogleDriveService().build()

	try:
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y_%H:%M:%S")
		print("date and time =", dt_string)
		
		file_metadata = {'name': f'_{dt_string}_{file_name}', 'parents': [f'{folder}']}
		media = MediaFileUpload(f'./data/{file_name}',
								mimetype='text/plain')
		file = g_drive_service.files().create(body=file_metadata, media_body=media,
										fields='id').execute()
		print(F'File ID: {file.get("id")}')

	except HttpError as error:
		print(F'An error occurred: {error}')
		file = None

	return file


@app.post('/upload-folder/<string:folder>')
def uploadFolderGDrive(folder):
	g_drive_service = GoogleDriveService().build()
    
	try:
		now = datetime.now()
		dt_string = now.strftime("%d/%m/%Y_%H:%M")
		print("date and time =", dt_string)
		
		## !!!!!!!!!!!!!!!!!!!!!!!!!! ex. https://drive.google.com/drive/u/0/folders/[folder id]
		file_metadata = {'name': f'{folder}_{dt_string}', 'parents': ['## folder id ##'], 'mimeType': 'application/vnd.google-apps.folder'}

		folder =  g_drive_service.files().create(body=file_metadata, fields='id').execute()
		#print('Folder: ', folder)
	except HttpError as error:
		print(F'An error occurred: {error}')
		folder = None

	return folder


if __name__=='__main__':
    app.run(debug=True)