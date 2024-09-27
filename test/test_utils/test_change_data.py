from src.lambda_utils.change_data import change_data
import pytest
import csv
import os
from unittest.mock import patch, mock_open


# @pytest.mark.describe("change_data")
# @pytest.mark.it("tests csv file content is changed")
# def test_change_data_success():
#     test_data = 'name,column2,email_address\nname1,data1,original_email@example.com\n'

#     expected_result = '***,data1,original_email@example.com\r\n'

#     with patch('builtins.open', new_callable=mock_open, read_data=test_data) as mock_file:
#         copy_file = 'test_file.csv'
#         pii_columns = ['name']
#         result = change_data(copy_file, pii_columns)

#         # expected_result = os.path.abspath(copy_file)
#         # assert result == expected_result

#         mock_file().write.assert_called_with(expected_result)

#         with open(copy_file, 'r') as f:
#             actual_result = f.read()
#             assert actual_result == expected_result


# @pytest.mark.describe("change_data")
# @pytest.mark.it("tests csv content is changed")
# def test_change_data_file_not_found():
#     """
#     Tests if the change_data function raises a ValueError when the file is not found.
#     """
#     with pytest.raises(ValueError) as excinfo:
#         change_data('./nonexistent_file.csv', [])
#     assert str(excinfo.value) == "CSV file './nonexistent_file.csv' not found."


# @pytest.mark.describe("change_data")
# @pytest.mark.it("tests csv content is changed")
# def test_change_data_invalid_csv():
#     """
#     Tests if the change_data function raises a ValueError when the CSV file is invalid.
#     """
#     invalid_csv_data = "invalid data"
#     with patch('builtins.open', mock_open(read_data=invalid_csv_data)) as mock_file:
#         with pytest.raises(ValueError) as excinfo:
#             change_data('./mock_data.csv', [])
#     assert str(excinfo.value).startswith("Error reading CSV file:")


# @pytest.mark.describe("change_data")
# @pytest.mark.it("tests csv content is changed")
# def test_change_data_pii_column_not_found():
#     """
#     Tests if the change_data function raises a KeyError when a PII column is not found.
#     """
#     pii_columns = ['nonexistent_column']
#     mock_data = [
#         ['column1', 'column2', 'email_address'],
#         ['data1', 'data2', 'original_email@example.com'],
#         ['data3', 'data4', 'another_email@example.com']
#     ]

#     with patch('builtins.open', mock_open(read_data='\n'.join(csv.writer(mock_data)).join('\n'))) as mock_file:
#         with pytest.raises(KeyError) as excinfo:
#             change_data('./mock_data.csv', pii_columns)
#     assert str(excinfo.value) == "PII column 'nonexistent_column' not found."
