import boto3
import os
from dotenv import load_dotenv

load_dotenv()

# Initialize the S3 client
s3 = boto3.client('s3',
                    aws_access_key_id=os.getenv('aws_access_key_id'),
                    aws_secret_access_key=os.getenv('aws_secret_access_key')
                )

# Your bucket and access point name
BUCKET_NAME = os.getenv('BUCKET_NAME')
ACCESS_POINT_ARN = os.getenv('ACCESS_POINT_ARN')  # replace region, account-id, and your-access-point-name accordingly

# Upload a file
file_name = 'test.txt'
with open(file_name, 'wb') as f:
    f.write(b'This is a test file')

s3.upload_file(file_name, BUCKET_NAME, file_name, ExtraArgs={"ACL": "bucket-owner-full-control"})

print(f'Uploaded {file_name} to {BUCKET_NAME}')

# Download the file
download_path = 'downloaded_test.txt'
s3.download_file(BUCKET_NAME, file_name, download_path)

print(f'Downloaded {file_name} to {download_path}')

# Ensure the content matches
with open(download_path, 'rb') as f:
    content = f.read()
assert content == b'This is a test file'
print('File content matches!')

