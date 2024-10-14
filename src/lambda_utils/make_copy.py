import os
import tempfile
import pandas as pd


def make_copy(filename, output_filename=None):
    """
    This function reads a csv file, makes an exact copy in
    a new file and returns the copied file path

    Args:
        filename: string of the csv file name
        output_filename: optional string of the desired output file name.
        If not provided, a default name will be generated

    Returns:
        string of the copied CSV absolute path

    Raises:
        FileNotFoundError: If the specified input file does not exist
        EmptyDataError: If the CSV file is empty
    """
    if not os.path.exists(filename):
        raise FileNotFoundError(f"File '{filename}' not found.")

    if not output_filename:
        output_filename = tempfile.mkstemp(suffix=".csv")[1]

    with open(filename, "r") as source:
        try:
            df = pd.read_csv(source)
        except pd.errors.EmptyDataError as e:
            raise e(f"File '{filename}' is empty")

    df.to_csv(output_filename, index=False)

    print(f"A copy of '{filename}' has been created as '{output_filename}'.")
    return os.path.abspath(output_filename)
