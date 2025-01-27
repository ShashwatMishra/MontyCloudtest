import pytest
import json
import base64
from unittest.mock import patch, MagicMock
from delete import lambda_handler as delete_lambda_handler
from download import lambda_handler as download_lambda_handler
from getImage import lambda_handler as getimage_lambda_handler
from uplaodImage import lambda_handler as upload_lamda_handler


@patch('upload_lamda_handler.boto3.client')
def test_upload_image_success(mock_boto_client):
    mock_s3 = MagicMock()
    mock_boto_client.return_value = mock_s3

    event = {
        'body': json.dumps({
            'file_name': 'test.jpg',
            'image': base64.b64encode(b'test image data').decode('utf-8'),
            'metadata': {'key1': 'value1'}
        })
    }

    response = upload_lamda_handler(event, None)

    assert response['statusCode'] == 200
    assert 'File uploaded successfully' in response['body']


@patch('upload_lamda_handler.boto3.client')
def test_upload_image_failure(mock_boto_client):
    mock_s3 = MagicMock()
    mock_s3.put_object.side_effect = Exception('Upload failed')
    mock_boto_client.return_value = mock_s3

    event = {
        'body': json.dumps({
            'file_name': 'test.jpg',
            'image': base64.b64encode(b'test image data').decode('utf-8'),
            'metadata': {'key1': 'value1'}
        })
    }

    response = upload_lamda_handler(event, None)

    assert response['statusCode'] == 500
    assert 'Error uploading file' in response['body']


@patch('delete_lambda_handler.boto3.client')
def test_delete_file_success(mock_boto_client):
    mock_s3 = MagicMock()
    mock_boto_client.return_value = mock_s3

    event = {
        'queryStringParameters': {'file_name': 'test.jpg'}
    }

    response = delete_lambda_handler(event, None)

    assert response['statusCode'] == 200
    assert 'File test.jpg deleted successfully' in response['body']


@patch('delete_lambda_handler.boto3.client')
def test_delete_file_failure(mock_boto_client):
    mock_s3 = MagicMock()
    mock_s3.delete_object.side_effect = Exception('Delete failed')
    mock_boto_client.return_value = mock_s3

    event = {
        'queryStringParameters': {'file_name': 'test.jpg'}
    }

    response = delete_lambda_handler(event, None)

    assert response['statusCode'] == 500
    assert 'Error deleting file' in response['body']