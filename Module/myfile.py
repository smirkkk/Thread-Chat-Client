import boto3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog

def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)
    return fileName

def uploadFile(self, file_path, file_name, folder=None, bucket='dsm-chatting'):
    s3 = boto3.resource('s3')
    s3_path = None
    if folder:
        s3_path = folder + file_name
    else :
        s3_path = file_name

    s3.meta.client.upload_file(file_path, bucket, s3_path)
