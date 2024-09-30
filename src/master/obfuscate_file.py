from src.lambda_utils.read_json import read_json
from src.lambda_utils.download_s3 import download_s3
from src.lambda_utils.make_copy import make_copy
from src.lambda_utils.change_data import change_data
import logging
import time


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

    logging.info("Request to obfuscate file beginning...")
    try:
        requested = read_json(file_req)

    except FileNotFoundError as e:
        logging.error(f"Input file '{file_req}' not found: {e}")
        raise

    try:
        filepath = list(requested)[0]
        pii_fields = list(requested)[1]

    except IndexError as e:
        logging.error(f"Invalid input file format: {e}")
        raise

    try:
        downloaded_file = download_s3(filepath)
        time.sleep(10)

    except Exception as e:  # Catch all exceptions for S3 download
        logging.error(f"Failed to download file from S3: {e}")
        raise

    try:
        new_file = make_copy(downloaded_file)

    except Exception as e:  # Catch all exceptions for file copy
        logging.error(f"Failed to create copy of file: {e}")
        raise

    try:
        change_data(new_file, pii_fields)

    except Exception as e:  # Catch all exceptions for data change
        logging.error(f"Failed to change data in file: {e}")
        raise

    logging.info(f"{new_file} has been obfuscated")
