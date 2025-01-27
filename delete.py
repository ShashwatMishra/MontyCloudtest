import json
import boto3
aws_access_key_id = ""
aws_secret_access_key = ""
region_name = ""
s3 = boto3.client('s3',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name=region_name)
bucket_name = ""

def lambda_handler(event, context):
    file_name = event['queryStringParameters']['file_name']
    try:
        s3.delete_object(Bucket=bucket_name, Key=file_name)
        return {
            'statusCode': 200,
            'body': json.dumps(f'File {file_name} deleted successfully')
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error deleting file: {str(e)}')
        }