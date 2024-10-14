# Obfuscator-Project
GDPR Obfuscator Project for Launchpad

A general-purpose tool that can be integrated as a library module into a Python codebase.

The tool will be deployed within the AWS account, supplied with the S3 location of a file containing sensitive information, and the names of the affected fields.

It will create a new file containing an exact copy of the input csv file but with the sensitive data replaced with obfuscated strings. 


## Set-up
##### Setting up variable environment for the project
Before running the project, you will need to run the following command to set up your variable environment and install any required dependencies:

`make requirements`


## Master Function - obfuscate_file()
The master function 'obfuscate_file(filepath)' is supplied with a json file path containing the s3 location URL and the PII fields requiring obfuscating.

The function flows through the util functions below

The end product is a file with obfuscated strings that has replaced the original data.

##### Execute obfuscate file:
run `obfuscate_file(json_file)` replacing `json_file` with your given JSON filepath.


## Util Functions
##### read_json()
read_json() is supplied a file path to a json file containing the s3 URL and the PII fields required to have its data changed.

The json values are split to `filepath` and `pii_fields` to pass through the required functions.

##### download_file()
download_file() takes the `filepath` obtained from read_json() and downloads the .csv file stored in the given AWS S3 location.

The relative filepath of the downloaded csv file is returned.

##### make_copy()
make_copy() takes the downloaded csv `filepath` to create and absolute copy.

This ensures that the original data is not manipulated and no data is lost.

The absolute path of the copied csv file is returned.

##### change_data()
change_data() takes the copied csv file path and the PII fields obtained from `read_json()` to identify the index of the required fields needing the data changed to `***`.

The copied csv file is overwritten to the updated data fields.


## Testing Functions
To test a specific function, run `make unit-test file/to/test`, replacing `file/to/test` with the required test filepath.

To test all the functions, run `make unit-tests`. This will execute pytest for all functions.

To test security on the requirements and python files, run `make security-test` which uses a safety check and bandit.

To test for PEP8 compliance, run `make run-flake`.

To test the test coverage of the functions, run `make check-coverage`.

You can also run all the tests as one by using `make run-checks`.

https://github.com/northcoders/grad-post-programme-projects/blob/main/DE/gdpr_obfuscator.md
