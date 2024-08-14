import os
import boto3
from dotenv import load_dotenv

def upload_to_s3(file_name, bucket, object_name=None):
    """
    Upload a file to an S3 bucket

    :param file_name: File to upload
    :param bucket: Bucket to upload to
    :param object_name: S3 object name. If not specified then file_name is used
    :return: True if file was uploaded, else False
    """
    # If S3 object_name was not specified, use file_name
    if object_name is None:
        object_name = os.path.basename(file_name)

    # Upload the file
    s3_client = boto3.client('s3')
    try:
        s3_client.upload_file(file_name, bucket, object_name)
        print(f"File {file_name} uploaded to {bucket}/{object_name}")
        return True
    except Exception as e:
        print(f"Error uploading file: {e}")
        return False

if __name__ == "__main__":
    # Load environment variables from .env file
    load_dotenv()

    # Retrieve AWS credentials and bucket name from environment variables
    AWS_ACCESS_KEY_ID = os.getenv('AWS_ACCESS_KEY_ID')
    AWS_SECRET_ACCESS_KEY = os.getenv('AWS_SECRET_ACCESS_KEY')
    AWS_REGION = os.getenv('AWS_REGION')
    S3_BUCKET_NAME = os.getenv('S3_BUCKET_NAME')

    # File to upload
    INPUT_FILE = 'transformed_data_clean.csv'

    # Upload the transformed data to S3
    upload_to_s3(INPUT_FILE, S3_BUCKET_NAME)
