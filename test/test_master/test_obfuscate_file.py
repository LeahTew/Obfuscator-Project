import pytest
from src.master.obfuscate_file import obfuscate_file
import csv
from io import StringIO
import json


@pytest.fixture
def mock_read_json(mocker):
    mock = mocker.patch("src.lambda_utils.read_json")
    return mock


@pytest.fixture
def mock_download_s3(mocker):
    mock_s3_client = mocker.patch('boto3.client')
    mock_s3_client.return_value.download_file.return_value = None
    return mock_s3_client


@pytest.fixture
def mock_csv_file():
    """Creates a mock CSV file."""
    csv_data = StringIO()
    writer = csv.writer(csv_data)
    writer.writerow(['name', 'column2', 'email_address'])
    writer.writerow(['name1', 'value2', 'test@email,com'])
    csv_data.seek(0)
    return csv_data


@pytest.fixture
def mock_make_copy(mocker, mock_csv_file):
    mock = mocker.patch("src.lambda_utils.make_copy")
    mock.return_value = mock_csv_file
    return mock


@pytest.fixture
def mock_change_data(mocker):
    mock = mocker.patch("src.lambda_utils.change_data")
    return mock


def test_obfuscate_file_success(mock_read_json, mock_download_s3,
                                mock_make_copy, mock_change_data,
                                mock_csv_file):
    mock_read_json.return_value = json.dumps({
        "filepath": "s3://my_ingestion_bucket/new_data/file1.csv",
        "pii_fields": ["name", "email"]
    })
    mock_s3_client = mock_download_s3
    mock_s3_client.return_value.download_file.return_value = "file1.csv"

    obfuscate_file("./json_files/s3_input.json")

    mock_read_json.assert_called_once_with("./json_files/s3_input.json")
    mock_s3_client.return_value.download_file.assert_called_once_with(
        "file1.csv")
    mock_make_copy.assert_called_once_with("file1.csv")
    mock_change_data.assert_called_once_with(
        "new_file.csv", ["name", "email_address"])
