import pandas as pd
import os


def make_copy(filename):
    """
    This function reads a csv file, makes an exact copy in a new file and returns the copied file path.

    Args:
        `filename`: string of the csv file name
    ---------------------------
    Returns:
        `copy_path`: sting of the copied csv absolute path

    Raises:
        ?????
    """

    with open(filename, "r") as source:
        reader = pd.read_csv(source)
        reader.to_csv('copy_file.csv', index=False)
        print(f'A copy of {filename} has been created')
        copy_path = os.path.abspath('copy_file.csv')
    return copy_path
