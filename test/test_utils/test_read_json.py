from src.lambda_utils.read_json import read_json
from unittest.mock import patch, mock_open
import pytest
import json


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test """)
@patch('builtins.open', new_callable=mock_open,
       read_data=json.dumps({"file": "./test/mock_data.csv",
                             "column": "name"}))
def test_read_file_data(self):
    """
    Given:


    Returns:

    """

    filename = 'example.json'

    self.assert_called_with(filename, 'r')


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test """)
@patch('builtins.open', new_callable=mock_open,
       read_data=json.dumps({"file": "./test/mock_data.csv",
                             "column": "name"}))
def test_returns_values_from_json_file(self):
    """
    Given:


    Returns:

    """
    expected_output = {"file": "./test/mock_data.csv", "column": "name"}
    filename = 'example.json'
    actual_output = read_json(filename)
    actual_output_to_list = list(actual_output)
    expected_output_values_to_list = list(expected_output.values())
    assert actual_output_to_list == expected_output_values_to_list


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test """)
@patch('builtins.open', new_callable=mock_open,
       read_data=json.dumps({"file": "./test/mock_data.csv",
                             "column": ["name", "email"]}))
def test_returns_values_from_json_file_multiple_cols(self):
    """
    Given:


    Returns:

    """
    expected_output = {"file": "./test/mock_data.csv",
                       "column": ["name", "email"]}
    filename = 'example.json'
    actual_output = read_json(filename)
    actual_output_to_list = list(actual_output)
    expected_output_values_to_list = list(expected_output.values())
    print(actual_output_to_list)
    assert actual_output_to_list == expected_output_values_to_list


def test_read_invalid_json():
    """Tests reading an invalid JSON file."""
    json_file = "./test/invalid_data.json"
    with pytest.raises(json.JSONDecodeError):
        read_json(json_file)


def test_read_nonexistent_file():
    """Tests reading a non-existent file."""
    json_file = "nonexistent_file.json"
    with pytest.raises(FileNotFoundError):
        read_json(json_file)
