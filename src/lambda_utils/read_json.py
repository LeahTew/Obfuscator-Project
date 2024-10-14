import json


def read_json(json_file):
    """
    Reads a JSON file and returns its values.

    Args:
        json_file (str): The path to the JSON file.

    Returns:
        dict: A dictionary containing the values from the JSON file.

    Raises:
        FileNotFoundError: If the JSON file is not found.
        json.JSONDecodeError: If there is an error decoding the JSON.
        Exception: If there is an unexpected error.
    """
    try:
        with open(json_file, 'r', encoding='utf-8') as jf:
            sample_load_file = json.load(jf)

        values = sample_load_file.values()

        return values

    except FileNotFoundError:
        raise FileNotFoundError(f"Error: JSON file '{json_file}' not found.")

    except json.JSONDecodeError as e:
        print(f"Error decoding JSON: {e}")
        raise e

    except Exception as e:
        print(f"Unexpected error: {e}")
        raise e
