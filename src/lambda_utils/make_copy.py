import pandas as pd


def copy_file(filename):
    with open(filename, "r") as source:
        reader = pd.read_csv(source)
        reader.to_csv('copy_' + 'file_data1.csv', index=False)


copy_file("../../mock_data/mock_data1.csv")

'''
copy file type exactly
'''
