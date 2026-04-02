#!/usr/bin/env python3

import csv
import sys
import os

def duplicate_lines_with_commas(input_file, output_file):
    """
    Normalize to 1NF the users.csv file extracted from Adobe Admin Console, based on column "User Groups"

    Iterate over the input_file CSV.
    For each row, get record #11 (User Groups).
    If the value contains commas, split on commas, duplicate the row for each obtained element and put it in column 11

    """
    # Read all rows from the input CSV into memory
    with open(input_file, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    output_rows = []
    for row in rows:
        # Check if column 12 (index 11) exists and contains multiple comma-separated values
        if len(row) >= 12 and ',' in row[11]:
            field_12 = row[11]
            # Split the multi-value cell into individual group names
            split_fields = field_12.split(',')

            # Emit one row per group, copying all other columns as-is
            for field in split_fields:
                new_row = row[:]
                new_row[11] = field
                output_rows.append(new_row)
        else:
            # Row has a single group (or no value): keep it unchanged
            output_rows.append(row)

    # Write the normalized rows to the output CSV
    with open(output_file, 'w', newline='', encoding="utf-8") as csv_output:
        writer = csv.writer(csv_output)
        writer.writerows(output_rows)

# MAIN
if __name__ == '__main__':
    # Require exactly one argument: the input CSV file path
    if len(sys.argv) < 2:
        print("Usage: "+sys.argv[0]+" users.csv")
        print("")
        print("Normalize users.csv extraction from Adobe Admin Console, creating a 1NF table based on User Groups column")
        print("Please provide the input file path as an argument.")
        sys.exit(1)

    # Read the input file path from command-line arguments
    input_file = sys.argv[1]
    # Build the output file path by appending a suffix to the input filename
    output_file = os.path.splitext(input_file)[0] + '_GroupNormalized.csv'
    # Run the normalization
    duplicate_lines_with_commas(input_file, output_file)
    print(f"Output written to {output_file}")
