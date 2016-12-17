import sys
import csv

# try to fix '_csv.Error: field larger than field limit (131072)'
csv.field_size_limit(sys.maxint)

# write to common csv file with delimiter ','
# output the rows with matched id in id_list to a new csv file
def csv_match(id_list,key,input_file,output_file):
    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row[key] in set(id_list)]

    header = rows[0].keys()
    with open(output_file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for data in rows:
            f.write(",".join(data[h] for h in header))
            f.write('\n')

# output the rows with not matched id in id_list to a new csv file
def csv_not_match(id_list, key, input_file, output_file):
    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if not row[key] in set(id_list)]

    header = rows[0].keys()
    with open(output_file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for data in rows:
            f.write(",".join(data[h] for h in header))
            f.write('\n')





