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
    try:
        prefix = event.get('queryStringParameters', {}).get('prefix', '')
        response = s3.list_objects_v2(Bucket=bucket_name,Prefix=prefix)
        if 'Contents' in response:
            files = [obj['Key'] for obj in response['Contents']]
            return {
                'statusCode': 200,
                'body': json.dumps({'files': files})
            }
        else:
            return {
                'statusCode': 200,
                'body': json.dumps({'files': []})
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error retrieving files: {str(e)}')
        }