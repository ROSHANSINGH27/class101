import dropbox
import os

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    
    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)    
        files=os.listdir(file_from)
        for i in files:
         with open(file_from+'/'+i, 'rb') as f:
            dbx.files_upload(f.read(), file_to+'/'+i)

def main():
        access_token = 'sl.BF4n5ggYIyVHYRrT_C-yvsaTQuG3qeLMjmQv1-7j5tL9zrig76a5WPJF3vsl9gf5s_hDjmqsuCdNEgGAv_gWOlXRk31cPhfTJIStaPChTTCbOJWfO6ZwspMXSuHgDYRZbU_gZLno'
        transferData = TransferData(access_token)

        file_from = input("enter the path of your file")
        file_to = input("enter the path where to save")  # The full path to upload the file to, including the file name

        transferData.upload_file(file_from, file_to)

main()
