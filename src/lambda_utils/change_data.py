import csv
import os


def change_data(copy_file, pii):
    """
    Replaces sensitive data in specified columns of a CSV file with '***'.

    Args:
        copy_file: The path to the copied CSV file.
        pii_columns: A list of column names containing sensitive data.

    Returns:
        Updated CSV filepath with the modified data.

    Raises:
        ValueError: If the CSV file cannot be opened or read.
        KeyError: If a specified PII column is not found in the CSV file.
    """

    try:
        for arg in pii:
            update_data = {arg: [None, '***']}

            line_no = 0

            new_csv = []

            with open(copy_file, 'r') as csvfile:
                filereader = csv.reader(csvfile)

                for line in filereader:
                    if line_no == 0:

                        for key in update_data:
                            update_data[key][0] = line.index(key)

                    else:

                        for key in update_data:
                            line[update_data[key][0]] = update_data[key][1]

                    new_csv.append(line)

                    line_no += 1

            with open(copy_file, 'w') as csvfile:
                filewriter = csv.writer(csvfile)

                for line in new_csv:
                    filewriter.writerow(line)

        return os.path.abspath(copy_file)

    except FileNotFoundError:
        raise FileNotFoundError(f"CSV file '{copy_file}' not found.")

    except csv.Error as e:
        raise e(f"Error reading CSV file: {e}")
