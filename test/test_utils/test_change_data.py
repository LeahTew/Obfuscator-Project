from src.lambda_utils.change_data import change_data
from unittest.mock import patch, mock_open
import pytest
import csv


@pytest.mark.describe("change_data")
@pytest.mark.it("""Test """)
def test_change_data():
    """
    Given:


    Returns:

    """
    test_piis = ["name", "email_address"]
    testfile = 'test/test_utils/testfiles/test.csv'
    output_data = {
        'id': [1, 2],
        'music_genre': ['Country', 'Reggae'],
        'colour': ['Maroon', 'Yellow'],
        'name': ['***', '***'],
        'email_address': ['***', '***']
    }
    expected = csv.reader()

    actual_output = change_data(testfile, test_piis)
    newlist = []

    assert 1 == 2
