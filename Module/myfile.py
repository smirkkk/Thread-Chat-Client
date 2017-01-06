import boto3
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog

def openFileNameDialog(self):
    options = QFileDialog.Options()
    options |= QFileDialog.DontUseNativeDialog
    fileName, _ = QFileDialog.getOpenFileName(self, "QFileDialog.getOpenFileName()", "",
                                              "All Files (*);;Python Files (*.py)", options=options)

    return fileName


def uploadFile(self, filename):
    s3 = boto3.resource('s3')
    s3.meta.client.upload_file(filename, 'dsm-chatting', 'qwerty')