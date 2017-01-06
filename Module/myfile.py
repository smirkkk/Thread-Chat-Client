import boto3
from PyQt5.QtWidgets import QFileDialog

def make_extention(file):
    blank = ''
    extention = file.split('/')
    extention = extention[-1]

    if extention.find('.') == -1:
        return blank
    else:
        extention = extention.split('.')
        extention = extention[-1]
        extention = '.'+extention
        return extention

def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
    return fileName

def uploadFile(self, file_path, file_name, folder=None, bucket='dsm-chatting'):
    s3 = boto3.resource('s3')
    print(file_path)
    extender = make_extention(file_path)
    print(extender)
    s3_path = None
    if folder:
        s3_path = folder + '/' + file_name + extender
    else:
        s3_path = file_name + extender

    print(s3_path)
    s3.meta.client.upload_file(file_path, bucket, s3_path)