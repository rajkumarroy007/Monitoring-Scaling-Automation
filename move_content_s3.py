import os
import boto3
from boto3.s3.transfer import S3Transfer
from botocore.exceptions import NoCredentialsError, ClientError

def upload_to_s3(file_path, bucket_name):
    # Create an S3 client
    s3_client = boto3.client('s3')
    transfer = S3Transfer(s3_client)

    # Extract the filename from the file path
    file_name = os.path.basename(file_path)

    try:
        # Upload the file
        print(f"Uploading {file_name} to bucket {bucket_name}...")
        transfer.upload_file(file_path, bucket_name, file_name)
        print(f"File uploaded successfully to {bucket_name}/{file_name}")

    except NoCredentialsError:
        print("Credentials not available")
    except ClientError as e:
        print(f"Error occurred: {e}")

# Specify the file path and S3 bucket name
file_path = '/var/www/html/index.html'
bucket_name = 'rajkumar-my-webapp-static-files'

# Call the function to upload the file
upload_to_s3(file_path, bucket_name)

