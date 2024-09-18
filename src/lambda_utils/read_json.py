import json


def read_json(json_file):
    with open(json_file, 'r') as jf:
        sample_load_file = json.load(jf)

    values = sample_load_file.values()

    return values
