import dropbox
class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        """upload a file to Dropbox using API v2
        """
        dbx = dropbox.Dropbox(self.access_token)

        with open(file_from, 'rb') as f:
            dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.Ay57PRyLMu8EOSXEbwLHFYcKmEiryw-1cQxFSS_F4doLz6wwwC6gTFye4ZfRGWq2AUBjg2PvPcpOOOBW-Jt8s2gDluaTF9yVsJbKL4RYijBc8zCelPOrQS0U2y81ZvtTx38wDM3ad7E'
    transferData = TransferData(access_token)

    file_from = input("enter the file that has to be uploaded") 
    file_to = input("enter the folder")  # The full path to upload the file to, including the file name

    # API v2
    transferData.upload_file(file_from, file_to)

if __name__ == '__main__':
    main()