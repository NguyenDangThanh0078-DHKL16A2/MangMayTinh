import boto3
from botocore.client import Config

# Kết nối với MinIO
s3 = boto3.client('s3',
    endpoint_url='http://localhost:9000',
    aws_access_key_id='myuser01',
    aws_secret_access_key='mysecret123',
    config=Config(signature_version='s3v4'),
    region_name='us-east-1')

# Tải file
s3.download_file('personal-data-bucket', 'sensor_data.csv', 'downloaded_sensor_data.csv')
print("Tải file thành công!")