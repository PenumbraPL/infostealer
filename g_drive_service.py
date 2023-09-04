from os import environ, path, getcwd
from googleapiclient.discovery import build
from oauth2client.service_account import ServiceAccountCredentials


class GoogleDriveService:
    def __init__(self):
        self._SCOPES=['https://www.googleapis.com/auth/drive']

# Credentials from external file - not necessary
        #_credential_path=path.join(getcwd(), 'credential.json')
        #environ["GOOGLE_APPLICATION_CREDENTIALS"] = _credential_path

    def build(self):
# Credentials from external file - not necessary
#        creds = ServiceAccountCredentials.from_json_keyfile_name(os.getenv("GOOGLE_APPLICATION_CREDENTIALS"), self._SCOPES)
        json = {
                # !!!!!
                # json data from google cloud : https://obikastanya.medium.com/easy-way-to-integrate-your-python-apps-with-google-drive-api-2f29ed0be239
                }
        creds = ServiceAccountCredentials.from_json_keyfile_dict(json, self._SCOPES)

        service = build('drive', 'v3', credentials=creds)

        return service