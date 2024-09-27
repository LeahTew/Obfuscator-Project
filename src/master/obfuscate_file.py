from src.lambda_utils.read_json import read_json
from src.lambda_utils.download_s3 import download_s3
from src.lambda_utils.make_copy import make_copy
from src.lambda_utils.change_data import change_data


def obfuscate_file(file_req):
    """
    Master function that obfuscates a specified file.

    Args:
        file_req (str): The path to a JSON file containing details of
        the file to be obfuscated and column names to obfuscate.

    Returns:
        None

    Raises:
        FileNotFoundError: If the specified input file does not exist.
        EmptyDataError: If the CSV file is empty.
    """

    print('Request to obfuscate file beginning...')

    requested = read_json(file_req)

    filepath = list(requested)[0]
    pii_fields = list(requested)[1]

    downloaded_file = download_s3(filepath)
    new_file = make_copy(downloaded_file)

    change_data(new_file, pii_fields)
    return print(f'{new_file} has been obfuscated')
