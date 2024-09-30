from src.lambda_utils.change_data import change_data
import pytest
import csv
import tempfile
import os


@pytest.fixture
def test_data():
    """Creates a temporary CSV file with test data and returns its path."""
    with tempfile.NamedTemporaryFile(mode="w", delete=False) as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["name", "colour", "email_address", "music_genre"])
        writer.writerow(["name1", "Black", "example@email.com", "Metal"])
        writer.writerow(["name2", "Red", "another@email.com", "Country"])
        return csvfile.name


@pytest.mark.describe("change_data")
@pytest.mark.it("""Test given column key data is replaced correctly""")
def test_correct_pii_replacement(test_data):
    """
    Tests the `change_data` function with correct PII replacement.
    """
    result = change_data(test_data, ["name"])

    with open(result, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        assert rows[1][0] == "***"
        assert rows[2][0] == "***"

    os.remove(test_data)


@pytest.mark.describe("change_data")
@pytest.mark.it("""Test given multiple column key data
                is replaced correctly""")
def test_correct_multiple_pii_replacement(test_data):
    """
    Tests the `change_data` function with correct PII replacement
    when multiple `keys` are given.
    """
    result = change_data(test_data, ["name", "email_address"])

    with open(result, "r", newline="") as csvfile:
        reader = csv.reader(csvfile)
        rows = list(reader)
        print(rows)
        assert rows[1][0] == "***"
        assert rows[1][1] == "Black"
        assert rows[1][2] == "***"
        assert rows[1][3] == "Metal"

    os.remove(test_data)


@pytest.mark.describe("change_data")
@pytest.mark.it("Test FileNotFoundError is raised when file does not exist")
def test_change_data_file_not_found():
    """
    Tests if the change_data function raises a
    FileNotFoundError when the file is not found.
    """
    csv_file = "./no_file.csv"
    with pytest.raises(FileNotFoundError):
        change_data(csv_file, ['name'])
