import boto3

# Initialize an S3 client
s3 = boto3.client('s3')

# Create a unique bucket name and define region
bucket_name = 'rajkumar-my-webapp-static-files1'
region = 'us-west-2'

# Create the S3 bucket
response = s3.create_bucket(
    Bucket=bucket_name,
    CreateBucketConfiguration={
        'LocationConstraint': region
    }
)

print(f"Bucket {bucket_name} created successfully.")
