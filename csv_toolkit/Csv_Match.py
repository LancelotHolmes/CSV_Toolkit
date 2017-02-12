import sys
import csv

# try to fix '_csv.Error: field larger than field limit (131072)'
csv.field_size_limit(sys.maxint)

# write to common csv file with delimiter ','
# output the rows with matched key in refer_list to a new csv file
# @params
# refer_list: the list referred to
# key,key2: column name of csv file to check the value in the refer_list or not
def csv_match(refer_list,key,input_file,output_file):
    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if row[key] in set(refer_list)]

    header = rows[0].keys()
    with open(output_file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for data in rows:
            f.write(",".join(data[h] for h in header))
            f.write('\n')

# output the rows with matched key1 or key2 in refer_list to a new csv file
# @params
# refer_list: the list referred to
# key,key2: column name of csv file to check the value in the refer_list or not
def csv_match2(refer_list, key1, key2, input_file, output_file):
    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if (row[key1] in set(refer_list)) or (row[key2] in set(refer_list))]

    header = rows[0].keys()
    with open(output_file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for data in rows:
            f.write(",".join(data[h] for h in header))
            f.write('\n')


# output the rows that not matched with key in refer_list to a new csv file
# @params
# refer_list: the list referred to
# key,key2: column name of csv file to check the value in the refer_list or not
def csv_not_match(refer_list, key, input_file, output_file):
    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if not row[key] in set(refer_list)]

    header = rows[0].keys()
    with open(output_file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for data in rows:
            f.write(",".join(data[h] for h in header))
            f.write('\n')

# output the rows that not matched with key in refer_list to a new csv file
# @params
# refer_list: the list referred to
# key,key2: column name of csv file to check the value in the refer_list or not
def csv_not_match2(refer_list, key1,key2, input_file, output_file):
    with open(input_file, 'rb') as f:
        reader = csv.DictReader(f)
        rows = [row for row in reader if (row[key1] not in set(refer_list)) and (row[key2] not in set(refer_list))]

    header = rows[0].keys()
    with open(output_file, 'w') as f:
        f.write(','.join(header))
        f.write('\n')
        for data in rows:
            f.write(",".join(data[h] for h in header))
            f.write('\n')



