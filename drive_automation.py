import os
import sys

import webbrowser

from googleapiclient.discovery import build, MediaFileUpload
from httplib2 import Http
from oauth2client import file, client, tools

# If modifying these scopes, delete the file token.json.
SCOPES = 'https://www.googleapis.com/auth/drive'

class DriveAutomator:
    def __init__(self):
        store = file.Storage('token.json')
        creds = store.get()
        if not creds or creds.invalid:
            flow = client.flow_from_clientsecrets('credentials.json', SCOPES)
            creds = tools.run_flow(flow, store)
        self.service = build('drive', 'v3', http=creds.authorize(Http()))

    def create_doc(self, title):
        file_metadata = {
            'name': title,
            'mimeType': 'application/vnd.google-apps.document'
        }
        local_filename = "temp_file.html"
        with open(local_filename, "w") as f:
            f.write("<html></html>")
        media = MediaFileUpload(local_filename,
                                mimetype='text/html')
        f = self.service.files().create(body=file_metadata,
                                    media_body=media,
                                    fields='id').execute()
        file_id = f.get('id')
        print(f"File ID: {file_id}")
        os.remove(local_filename)
        webbrowser.open(f"https://docs.google.com/document/d/{file_id}/edit", new=2)

    def list_files(self, count):
        results = self.service.files().list(
            pageSize=count, fields="nextPageToken, files(id, name)").execute()
        items = results.get('files', [])

        if not items:
            print('No files found.')
        else:
            print('Files:')
            for item in items:
                print('{0} ({1})'.format(item['name'], item['id']))
