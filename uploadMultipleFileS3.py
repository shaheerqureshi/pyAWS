import boto3
import glob
from botocore.exceptions import NoCredentialsError

ACCESS_KEY = 'AKIASVD4ZM6LLBWFTUMJ'
SECRET_KEY = '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'


def upload_to_aws(local_file, bucket, s3_file):
    s3 = boto3.client('s3', aws_access_key_id=ACCESS_KEY,
                      aws_secret_access_key=SECRET_KEY)

    try:
        s3.upload_file(local_file, bucket, s3_file)
        print("Upload Successful")
        return True
    except FileNotFoundError:
        print("The file was not found")
        return False
    except NoCredentialsError:
        print("Credentials not available")
        return False
incre = 0
file = 'file'
for filepath in glob.iglob(r'/content/pics/*'):
  incre = incre + 1
  uploaded = upload_to_aws(filepath, 'bucketName', str(incre) + file+'.jpg')
