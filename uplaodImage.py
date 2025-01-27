import json
import boto3
import base64
aws_access_key_id = ""
aws_secret_access_key = ""
region_name = ""

def lambda_handler(event, context):
    try :
        bucket_name = ""
        body = json.loads(event['body'])
        image_data = base64.b64decode(body['image'])
        metadata = body['metadata']
        file_name = body['file_name']
        s3 = boto3.client('s3',
                    aws_access_key_id=aws_access_key_id,
                    aws_secret_access_key=aws_secret_access_key,
                    region_name=region_name)
        s3.put_object(
                Bucket=bucket_name,
                Key=file_name,
                Body=image_data,
                Metadata=metadata
            )
        return {
                'statusCode': 200,
                'body': json.dumps('File uploaded successfully')
            }
    except Exception as e:
        return {
            'statusCode': 500,
            'body': json.dumps(f'Error uploading file: {str(e)}')
        }
