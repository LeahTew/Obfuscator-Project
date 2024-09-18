from src.lambda_utils.read_json import read_json
from src.lambda_utils.make_copy import make_copy
from src.lambda_utils.change_data import change_data

def obfuscate_file(file_req):
    '''
    Parent function, takes filepath to json file containing details of file to be obfuscated and column names to obfuscate
    '''
    print('Request to obfuscate file beginning...')
    
    requested = read_json(file_req)

    filepath = list(requested)[0]
    pii_fields = list(requested)[1]

    new_file = make_copy(filepath)

    change_data(new_file, pii_fields)
    print (f'{new_file} has been obfuscated')

# obfuscate_file('./json_files/local_input.json')