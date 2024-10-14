# import csv
# from io import StringIO
# import json
# from unittest.mock import patch, mock_open
# import mock
# import pytest
# from src.master.obfuscate_file import obfuscate_file


# @pytest.fixture
# def mock_download_s3(mocker):
#     """
#     Mocks the download_s3 function
#     """
#     mock_s3_client = mocker.patch('boto3.client')
#     mock_s3_client.return_value.download_file.return_value = None
#     return mock_s3_client


# @pytest.fixture
# def mock_make_copy(mocker):
#     """
#     Mocks the make_copy function to return the mock_csv_file content.
#     """
#     mock_copy = mocker.patch("src.lambda_utils.make_copy")
#     mock_csv_file = StringIO()
#     writer = csv.writer(mock_csv_file)
#     writer.writerow(['name', 'column2', 'email_address'])
#     writer.writerow(['name1', 'value2', 'test@email.com'])
#     mock_copy.return_value = mock_csv_file.getvalue()
#     return mock_copy


# @pytest.fixture
# def mock_change_data(mocker):
#     """
#     Mocks the change data function
#     """
#     mock_change = mocker.patch("src.lambda_utils.change_data")
#     return mock_change


# @patch('src.lambda_utils.read_json')
# def test_obfuscate_file_success(mock_read_json, mock_download_s3,
#                                 mock_make_copy, mock_change_data):
#     """
#     ADD DOCSTRING
#     """
#     mock_s3_client = mock_download_s3
#     mock_s3_client.download_file.return_value = mock_make_copy.return_value
#     json_file_req = "./test/test_file.json"
#     csv_data = """name,colour,email_address
#     data1,data2,data3
#     data4,data5,data6"""
#     mock_csv_file = StringIO(csv_data)

#     with patch('builtins.open', new_callable=mock_open,
#                read_data=json.dumps(
#                    {"filepath": "s3://my_bucket/new_data/file1.csv",
#                     "pii_fields": ["name", "email_address"]})):
#         obfuscate_file(json_file_req)

#     with patch('builtins.open', new_callable=mock_open,
#                read_data=mock_csv_file):
#         mock_read_json.assert_called_once_with(json_file_req)
#         mock_download_s3.assert_called_once_with(
#             "s3://my_bucket/new_data/file1.csv")
#         mock_make_copy.assert_called_once_with(mock_s3_client.return_value)
#         mock_csv_reader = mock(csv.reader)
#         # mock_change_data.assert_called_once_with(
#         # mock_make_copy.return_value, mock_csv_reader)
#         mock_change_data.assert_called_once_with(mock_make_copy.return_value,
#                                                  ["name", "email_address"])
#         mock_csv_reader.return_value = iter([["***", "data2", "***"],
#                                             ["***", "data5", "***"]])
