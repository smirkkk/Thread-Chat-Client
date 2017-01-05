import boto3

s3 = boto3.resource('s3')

"""
Upload
s3.meta.client.upload_file('업로드할 파일명, 경로 포함', '버킷명', '파일명')
"""

"""
Download
s3.meta.client.download_file('버킷명', '버킷 안의 파일명', '저장할 경로 및 이름')
"""