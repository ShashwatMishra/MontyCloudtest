import json
import boto3
import base64

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
    print(file_name)
    try:
        s3_url = f"https://{bucket_name}.s3.amazonaws.com/{file_name}.jpg"
        return {
            'statusCode': 200,
            'body': json.dumps({'s3_url': s3_url})
        }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error retrieving image: {str(e)}')
        }