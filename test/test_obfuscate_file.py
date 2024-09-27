from src.master.obfuscate_file import obfuscate_file
import pytest
from unittest.mock import patch


@pytest.fixture
def mock_read_json():
    with patch('obfuscate_file.read_json') as mock_read_json:
        yield mock_read_json

@pytest.fixture
def mock_download_s3():
    with patch('obfuscate_file.download_s3') as mock_download_s3:
        yield mock_download_s3

@pytest.fixture
def mock_make_copy():
    with patch('obfuscate_file.make_copy') as mock_make_copy:
        yield mock_make_copy

@pytest.fixture
def mock_change_data():
    with patch('obfuscate_file.change_data') as mock_change_data:
        yield mock_change_data

def test_obfuscate_file_success(mock_read_json, mock_download_s3, mock_make_copy, mock_change_data):
    # Arrange
    file_req = "./json_files/test_json.json"
    mock_read_json.return_value = ["s3://bucket/key/file.csv", ["column1", "column2"]]
    mock_download_s3.return_value = "file.csv"
    mock_make_copy.return_value = "file_copy.csv"
    mock_change_data.return_value = "file_copy.csv"

    # Act
    obfuscate_file(file_req)

    # Assert
    mock_read_json.assert_called_once_with(file_req)
    mock_download_s3.assert_called_once_with("s3://bucket/key/file.csv")
    mock_make_copy.assert_called_once_with("file.csv")
    mock_change_data.assert_called_once_with("file_copy.csv", ["column1", "column2"])