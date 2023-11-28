#!/usr/bin/env python3

import csv
import sys
import os

def duplicate_lines_with_commas(input_file, output_file):
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

if __name__ == '__main__':
    if len(sys.argv) < 2:
        print("Usage: "+sys.argv[0]+" users.csv")
        print("")
        print("Normalize users.csv extraction from Adobe Admin Console")
        print("Please provide the input file path as an argument.")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = os.path.splitext(input_file)[0] + '_normalized.csv'
    duplicate_lines_with_commas(input_file, output_file)
    print(f"Output written to {output_file}")
