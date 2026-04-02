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
    # Read all rows from the input CSV into memory
    with open(input_file, 'r', encoding="utf-8") as csv_file:
        reader = csv.reader(csv_file)
        rows = list(reader)

    output_rows = []
    for row in rows:
        # Check if column 9 (index 8) exists and contains multiple comma-separated values
        if len(row) >= 9 and ',' in row[8]:
            field_9 = row[8]
            # Split the multi-value cell into individual product configuration names
            split_fields = field_9.split(',')

            # Emit one row per product configuration, copying all other columns as-is
            for field in split_fields:
                new_row = row[:]
                new_row[8] = field
                output_rows.append(new_row)
        else:
            # Row has a single product configuration (or no value): keep it unchanged
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
        print("Normalize users.csv extraction from Adobe Admin Console")
        print("Please provide the input file path as an argument.")
        sys.exit(1)

    # Read the input file path from command-line arguments
    input_file = sys.argv[1]
    # Build the output file path by appending a suffix to the input filename
    output_file = os.path.splitext(input_file)[0] + '_ProductNormalized.csv'
    # Run the normalization
    duplicate_lines_with_commas(input_file, output_file)
    print(f"Output written to {output_file}")
