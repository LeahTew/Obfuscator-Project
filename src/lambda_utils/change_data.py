import csv


def change_data(copy_file, pii):

    for arg in pii:
    # loop around args for all columns to change
        update_data = {arg: [None, '***']}
        # nested the original list inside another to hold the column index in the first position

        line_no = 0
        # counter for the first step

        new_csv = []
        # Holds the new rows for rewriting the file.

        with open(copy_file, 'r') as csvfile:
            filereader = csv.reader(csvfile)

            for line in filereader:
                if line_no == 0:

                    for key in update_data:
                        update_data[key][0] = line.index(key)
                        # finds the columns index and stores it

                else:

                    for key in update_data:
                        line[update_data[key][0]] = update_data[key][1]
                        # using the column index, enter the new data into the correct place

                new_csv.append(line)

                line_no += 1

        with open(copy_file, 'w') as csvfile:
            filewriter = csv.writer(csvfile)

            for line in new_csv:
                filewriter.writerow(line)


# change_data("./copy_file_data1.csv", 'email', 'name') << test print

'''change given column data to ***'''
