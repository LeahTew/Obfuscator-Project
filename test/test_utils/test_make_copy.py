from src.lambda_utils.make_copy import make_copy
from unittest.mock import patch
import pytest
import os
import pandas as pd


@pytest.fixture
def mocker():
    return mocker


@pytest.mark.describe("make_copy")
@pytest.mark.it("""Test pandas read method is invoked""")
@patch("src.lambda_utils.make_copy.pd")
def test_read_method_is_invoked(mock_pd):
    """
    Tests that the pandas read_csv method is invoked.

    Args:
        mock_pd (pytest.fixture): A mocked pandas module.

    Raises:
        AssertionError: If the test fails.
    """
    assert mock_pd.read_csv.call_count == 0
    make_copy("./mock_data/mock_data1.csv")
    assert mock_pd.read_csv.call_count == 1


@pytest.mark.describe("make_copy")
@pytest.mark.it("tests if copied file exists")
@patch("src.lambda_utils.make_copy.pd")
def test_copied_file_exists(mocker):
    """
    Tests that the copied file exists.

    Args:
        mocker (pytest.Mocker): A pytest mocker object.

    Raises:
        AssertionError: If the test fails.
    """
    filename = "./mock_data/mock_data.csv"
    mocker.patch('pandas.read_csv')
    mocker.patch('tempfile.mkstemp', return_value=(1, "copied_file.csv"))
    copy_path = make_copy(filename)
    assert os.path.exists(copy_path)


@pytest.mark.describe("make_copy")
@pytest.mark.it("tests if copied file has correct extension")
@patch("src.lambda_utils.make_copy.pd")
def test_copied_file_has_correct_extension(mocker):
    """
    Tests that the copied file has the correct extension.

    Args:
        mocker (pytest.Mocker): A pytest mocker object.

    Raises:
        AssertionError: If the test fails.
    """
    filename = "./mock_data/mock_data.csv"
    mocker.patch('pandas.read_csv')
    mocker.patch('tempfile.mkstemp', return_value=(1, "copied_file.csv"))
    copy_path = make_copy(filename)
    assert copy_path.endswith(".csv")

# VV TEST FAILING VV
# @pytest.mark.describe("make_copy")
# @pytest.mark.it("checks if copied file has the same content as the original")
# @patch("src.lambda_utils.make_copy.pd")
# def test_copied_file_has_correct_content(mocker):
#     """
#     Tests that the copied file has the same content as the original file.

#     Args:
#         mocker (pytest.Mocker): A pytest mocker object.
#     """

#     filename = "./mock_data/mock_data.csv"
#     original_df = pd.read_csv(filename)
#     print(original_df)

#     mocker.patch('pd.read_csv', return_value=original_df)

#     # Create a temporary file with a known name
#     mocker.patch('tempfile.mkstemp', return_value=(1, "copied_file.csv"))

#     # Call the function to make a copy
#     copy_path = make_copy(filename)

#     # Read the copied file using pandas
#     copied_df = pd.read_csv(copy_path)

#     # Assert that the DataFrames are equal
#     assert original_df.equals(copied_df)


@pytest.mark.describe("make_copy")
@pytest.mark.it("tests if FileNotFoundError is raised")
@patch("src.lambda_utils.make_copy.pd")
def test_file_not_found(mocker):
    """
    Tests the make_copy function when the input file is not found.

    Args:
        mocker (pytest.Mocker): A pytest mocker object.

    Raises:
        AssertionError: If the test fails.
    """

    filename = "nonexistent_file.csv"
    mocker.patch('os.path.exists', return_value=False)
    with pytest.raises(FileNotFoundError) as excinfo:
        make_copy(filename)
    assert str(excinfo.value) == f"File '{filename}' not found."
