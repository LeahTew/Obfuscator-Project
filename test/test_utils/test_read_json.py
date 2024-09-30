from src.lambda_utils.read_json import read_json
from unittest.mock import patch, mock_open
import pytest
import json


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test values are retrieved from JSON file""")
@patch('builtins.open', new_callable=mock_open,
       read_data=json.dumps({"file": "./test/mock_data.csv",
                             "column": "name"}))
def test_retrieves_values_from_json_file(self):
    """
    This test verifies that the `read_json` function successfully retrieves
    values from a JSON file.
    """
    expected_output = {"file": "./test/mock_data.csv", "column": "name"}
    filename = 'example.json'
    actual_output = read_json(filename)
    actual_output_to_list = list(actual_output)
    expected_output_values_to_list = list(expected_output.values())
    assert actual_output_to_list == expected_output_values_to_list


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test multiple column values are retrieved from JSON file""")
@patch('builtins.open', new_callable=mock_open,
       read_data=json.dumps({"file": "./test/mock_data.csv",
                             "column": ["name", "email"]}))
def test_retrieves_values_from_json_file_multiple_cols(self):
    """
    This test verifies that the `read_json` function
    successfully retrieves values from a JSON file,
    when the "column" key holds a list of multiple values.
    """
    expected_output = {"file": "./test/mock_data.csv",
                       "column": ["name", "email"]}
    filename = 'example.json'
    actual_output = read_json(filename)
    actual_output_to_list = list(actual_output)
    expected_output_values_to_list = list(expected_output.values())
    print(actual_output_to_list)
    assert actual_output_to_list == expected_output_values_to_list


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test read_json successfully reads a JSON file""")
def test_read_json_success():
    """
    Tests if the read_json function successfully reads a valid JSON file.

    Args:
        json_file (str): The path to the JSON file.

    Asserts:
        values (dict): The values read from the JSON file are not None.
    """
    json_file = "./json_files/local_input.json"
    values = read_json(json_file)
    assert values is not None


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test FileNotFoundError is raised
                when file does not exist""")
def test_read_json_not_found():
    """
    Tests if the read_json function raises a
    FileNotFoundError when the file is not found.

    Args:
        json_file (str): The path to the JSON file.

    Asserts:
        FileNotFoundError: The function raises a FileNotFoundError.
    """
    json_file = "./test_file.json"
    with pytest.raises(FileNotFoundError):
        read_json(json_file)


@pytest.mark.describe("read_json")
@pytest.mark.it("""Test JSONDecodeError is raised when JSON is invalid""")
def test_read_json_invalid_json():
    """
    Tests if the read_json function raises a
    JSONDecodeError when the JSON is invalid.

    Args:
        json_file (str): The path to the JSON file.

    Asserts:
        JSONDecodeError: The function raises a JSONDecodeError.
    """
    json_file = "./json_files/invalid_file.json"
    with pytest.raises(json.JSONDecodeError):
        read_json(json_file)
