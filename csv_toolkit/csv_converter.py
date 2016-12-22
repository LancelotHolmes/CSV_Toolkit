import csv

#---------------------------------------------------csv <--> dict--------------------------------------------

# convert csv file to dict(for id_map.csv)
def csv2dict(in_file):
    new_dict = {}
    with open(in_file, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            new_dict[row['id']] = row['players.player_id']
    return new_dict


# convert csv file to dict(key-value pairs each row)
def row_csv2dict(csv_file):
    dict_club={}
    with open(csv_file)as f:
        reader=csv.reader(f,delimiter=',')
        for row in reader:
            dict_club[row[0]]=row[1]
    return dict_club

# write dict to csv file
# write each key/value pair on a separate row
def dict2csv(dict, file):
    with open(file, 'wb') as f:
        w = csv.writer(f)
        # write each key/value pair on a separate row
        w.writerows(dict.items())

# write dict to csv file
# write all keys on one row and all values on the next
def dict2csv2(dict, file):
    with open(file, 'wb') as f:
        w = csv.writer(f)
        # write all keys on one row and all values on the next
        w.writerow(dict.keys())
        w.writerow(dict.values())

# build specific nested dict from csv files
# @params:
#   source_file
#   outer_key:the outer level key of nested dict
#   inner_key:the inner level key of nested dict,and rest key-value will be store as the value of inner key
def build_level2_dict(source_file,outer_key,inner_key):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        fieldnames = next(reader)
        inner_keyset=fieldnames
        inner_keyset.remove(outer_key)
        inner_keyset.remove(inner_key)
        csv_file.seek(0)
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            item = new_dict.get(row[outer_key], dict())
            item[row[inner_key]] = {k: row[k] for k in inner_keyset}
            new_dict[row[outer_key]] = item
    return new_dict

# build specific nested dict from csv files
# @params:
#   source_file
#   outer_key:the outer level key of nested dict
#   inner_key:the inner level key of nested dict
#   inner_value:set the inner value for the inner key
def build_level2_dict2(source_file,outer_key,inner_key,inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            item = new_dict.get(row[outer_key], dict())
            item[row[inner_key]] = row[inner_value]
            new_dict[row[outer_key]] = item
    return new_dict

#----------------------------------------------------------------------------------------------------------

#---------------------------------------------------csv <--> list--------------------------------------------

def list2csv(list, file):
# def list2csv(list):
#     wr = csv.writer(open(file, 'wb'), quoting=csv.QUOTE_ALL)
    wr=open(file,'w')
    for word in list:
        # print ''.join(word)
        # wr.writerow([word])
        wr.write(word+'\n')
        # wr.writerow(str.split(word,'"')[0])
        # print [word]

# test_list = ['United States', 'China', 'America', 'England']

# list2csv(test_list,'small_test.csv')

# write nested list of dict to csv
def nestedlist2csv(list, out_file):
    with open(out_file, 'wb') as f:
        w = csv.writer(f)
        fieldnames=list[0].keys()  # solve the problem to automatically write the header
        w.writerow(fieldnames)
        for row in list:
            w.writerow(row.values())

# collect and convert the first column of csv file to list
def csv2list(csv_file):
    lst = []
    with open(csv_file, 'rb')as f:
        reader = csv.reader(f, delimiter=',')
        for row in reader:
            lst.append(row[0])
    return list(set(lst))
#----------------------------------------------------------------------------------------------------------