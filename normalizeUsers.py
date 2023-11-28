#!/usr/bin/env python3

import csv
import sys
import os

def duplicate_lines_with_commas(input_file, output_file):
    """
    Normalize to 1NF the users.csv file extracted from Adobe Admin Console, based on column "Product Configurations"
    
    Iterate over the input_file CSV.
    For each row, get record #9 (Product Configurations).
    If the value contains commas, split on commas, duplicate the row for each obtained element and put it in column 9 
    
    """
    with open(input_file, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)
        
    output_rows = []
    for row in rows:
        if len(row) >= 9 and ',' in row[8]:
            field_9 = row[8]
            split_fields = field_9.split(',')
            
            for field in split_fields:
                new_row = row[:]
                new_row[8] = field
                output_rows.append(new_row)
        else:
            output_rows.append(row)
    
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_output:
        writer = csv.writer(csv_output)
        writer.writerows(output_rows)

# MAIN
if __name__ == '__main__':
    # requires one argument: the CSV file path
    if len(sys.argv) < 2:
        print("Usage: "+sys.argv[0]+" users.csv")
        print("")
        print("Normalize users.csv extraction from Adobe Admin Console")
        print("Please provide the input file path as an argument.")
        sys.exit(1)

    # get the argument
    input_file = sys.argv[1]
    # split the filename, get the name and append suffix
    output_file = os.path.splitext(input_file)[0] + '_normalized.csv'
    # call the main procedure
    duplicate_lines_with_commas(input_file, output_file)
    print(f"Output written to {output_file}")
