from src.lambda_utils.make_copy import make_copy
from unittest.mock import patch
import pytest
import pandas as pd
import io


@pytest.mark.describe("make_copy")
@pytest.mark.it("""Test pandas read method is invoked""")
@patch("src.lambda_utils.make_copy.pd")
def test_read_method_is_invoked(mock_pd):
    """
    Given:
    Existing csv file

    Returns:
    Check pandas read method is invoked using a mock
    """

    assert mock_pd.read_csv.call_count == 0
    make_copy("./mock_data/mock_data1.csv")
    assert mock_pd.read_csv.call_count == 1


@pytest.mark.describe("make_copy")
@pytest.mark.it("""Test pandas write method is invoked with print statement""")
@patch("src.lambda_utils.make_copy.pd")
def test_write_method_is_invoked(filename):
    """
    Given:
    Existing csv file

    Returns:
    Pandas write method is invoked using a mock as print statement invoked
    """

    expected = 'A copy of ./mock_data/mock_data1.csv has been created\n'
    with patch('sys.stdout', new=io.StringIO()) as fake_stdout:
        make_copy("./mock_data/mock_data1.csv")

    assert fake_stdout.getvalue() == expected


@pytest.mark.describe("make_copy")
@pytest.mark.it("""Test copied file path returned""")
@patch("src.lambda_utils.make_copy.pd")
def test_returns_copied_file_path(filename):
    """
    Given:
    Existing csv file

    Returns:
    File name of copied file as - 'copy_file.csv' is created and file path returned
    """

    with patch('os.path.abspath') as abspath_mock:
        test_abspath = 'test/abs/path/copy_file.csv'
        abspath_mock.return_value = test_abspath
        result = make_copy("./mock_data/mock_data.csv")

        assert result == test_abspath


    
# @pytest.mark.describe("make_copy")
# @pytest.mark.it("""Test copied file contains exact copy of original file""")
# @patch("src.lambda_utils.make_copy.pd")
# def test_write_method_is_invoked(mock_pd):
#     """
#     Given:
#     Existing csv file

#     Returns:
#     Boolean value of if files are exact copies
#     """
#     file1 = mock_pd.read_csv('./mock_data/mock_data.csv')
#     make_copy("./mock_data/mock_data.csv")
#     file2 = mock_pd.read_csv()

#     assert 