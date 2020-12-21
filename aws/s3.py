import boto3
import json

def repos_name_get(credentials):
    s3 = boto3.resource('s3')

    content_object = s3.Object(
        credentials['AWS_S3_BUCKET'],
        credentials['AWS_S3_BUCKET_FILE_NAME']
    )
    file_content = content_object.get()['Body'].read().decode('utf-8')

    return json.loads(file_content)