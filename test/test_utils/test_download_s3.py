from src.lambda_utils.download_s3 import download_s3
import botocore
from unittest.mock import patch
import pytest


@pytest.mark.describe("download_s3")
@pytest.mark.it("""Test successful s3 download file method""")
def test_successful_download():
    """
    Tests the download_s3 function when a file is successfully downloaded.

    Raises:
        AssertionError: If the test fails.
    """
    with patch('boto3.client') as mock_client:
        filepath = 's3://test_bucket/folder1/test_file.csv'
        mock_client.return_value.download_file.return_value = None

        result = download_s3(filepath)

        assert result == 'test_file.csv'
        mock_client.assert_called_once_with('s3')
        mock_client.return_value.download_file.assert_called_once_with(
            'test_bucket', 'folder1/test_file.csv', 'test_file.csv')


@pytest.mark.describe("download_s3")
@pytest.mark.it("""Test file not found""")
def test_file_not_found():
    """
    Tests the download_s3 function when the file is not found.

    Raises:
        AssertionError: If the test fails.
    """
    with patch('boto3.client') as mock_client:
        filepath = 's3://test_bucket/folder1/no_test_file.csv'
        mock_client.return_value.download_file.side_effect = botocore.exceptions.ClientError(
            {'Error': {'Code': '404'}}, 'operation')

        result = download_s3(filepath)

        assert result is None
        mock_client.assert_called_once_with('s3')
        mock_client.return_value.download_file.assert_called_once_with(
            'test_bucket', 'folder1/no_test_file.csv', 'no_test_file.csv')


@pytest.mark.describe("download_s3")
@pytest.mark.it("""Test client error""")
def test_client_error():
    """
    Tests the download_s3 function when a ClientError occurs.

    Raises:
        AssertionError: If the test fails.
    """
    with patch('boto3.client') as mock_client:
        filepath = 's3://test_bucket/folder1/test_file.csv'
        mock_client.return_value.download_file.side_effect = botocore.exceptions.ClientError(
            {'Error': {'Code': 'InternalServerError'}}, 'operation')

        try:
            download_s3(filepath)
        except botocore.exceptions.ClientError as e:
            assert e.response['Error']['Code'] == 'InternalServerError'
        else:
            assert False
