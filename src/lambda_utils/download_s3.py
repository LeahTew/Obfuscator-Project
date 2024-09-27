import boto3
import botocore


def download_s3(filepath):
    """
    Downloads an S3 object to a local file.

    Args:
        filepath (str): The S3 path to the object, e.g., "s3://my-bucket/my-file.txt".

    Returns:
        str: The name of the downloaded file.

    Raises:
        botocore.exceptions.ClientError: If there's an error downloading the file.
    """
    path_parts = filepath.replace("s3://", "").split("/")
    bucket = path_parts.pop(0)
    key = "/".join(path_parts)
    filename = path_parts[1]

    s3 = boto3.client('s3')

    try:
        s3.download_file(bucket, key, filename)
        return filename
    except botocore.exceptions.ClientError as e:
        if e.response['Error']['Code'] == "404":
            print("The object does not exist.")
        else:
            raise
