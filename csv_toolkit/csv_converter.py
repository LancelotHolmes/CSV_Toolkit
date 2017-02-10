import csv

#---------------------------------------------------csv <--> dict--------------------------------------------

# convert csv file to dict
# @params:
# key/value: the column of original csv file to set as the key and value of dict
def csv2dict(in_file,key,value):
    new_dict = {}
    with open(in_file, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            new_dict[row[key]] = row[value]
    return new_dict


# convert csv file to dict(key-value pairs each row)
# default: set row[0] as key and row[1] as value of the dict
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

# build a dict of list like {key:[...element of lst_inner_value...]}
# key is certain column name of csv file
# the lst_inner_value is a list of specific column name of csv file
def build_list_dict(source_file, key, lst_inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            for element in lst_inner_value:
                new_dict.setdefault(row[key], []).append(row[element])
    return new_dict
# sample:
# test_club=build_list_dict('test_info.csv','season',['move from','move to'])
# print test_club

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

# build specific nested dict from csv files
# @params:
#   source_file
#   outer_key:the outer level key of nested dict
#   lst_inner_value: a list of column name,for circumstance that the inner value of the same outer_key are not distinct
#   {outer_key:[{pairs of lst_inner_value}]}
def build_level2_dict3(source_file,outer_key,lst_inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            new_dict.setdefault(row[outer_key], []).append({k: row[k] for k in lst_inner_value})
    return new_dict

# build specific nested dict from csv files
# @params:
#   source_file
#   outer_key:the outer level key of nested dict
#   lst_inner_value: a list of column name,for circumstance that the inner value of the same outer_key are not distinct
#   {outer_key:{key of lst_inner_value:[...value of lst_inner_value...]}}
def build_level2_dict4(source_file,outer_key,lst_inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            # print row
            item = new_dict.get(row[outer_key], dict())
            # item.setdefault('move from',[]).append(row['move from'])
            # item.setdefault('move to', []).append(row['move to'])
            for element in lst_inner_value:
                item.setdefault(element, []).append(row[element])
            new_dict[row[outer_key]] = item
    return new_dict

# build specific nested dict from csv files
# @params:
#   source_file
#   outer_key:the outer level key of nested dict
#   lst_inner_key:a list of column name
#   lst_inner_value: a list of column name,for circumstance that the inner value of the same lst_inner_key are not distinct
#   {outer_key:{lst_inner_key:[...lst_inner_value...]}}
def build_list_dict2(source_file,outer_key,lst_inner_key,lst_inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            # print row
            item = new_dict.get(row[outer_key], dict())
            item.setdefault(row[lst_inner_key], []).append(row[lst_inner_value])
            new_dict[row[outer_key]] = item
    return new_dict

# dct=build_list_dict2('test_info.csv','season','move from','move to')

# build specific nested dict from csv files
# a dict like {outer_key:{inner_key1:{inner_key2:{rest_key:rest_value...}}}}
# the params are extract from the csv column name as you like
def build_level3_dict(source_file,outer_key,inner_key1,inner_key2):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        fieldnames = next(reader)
        inner_keyset=fieldnames
        inner_keyset.remove(outer_key)
        inner_keyset.remove(inner_key1)
        inner_keyset.remove(inner_key2)
        csv_file.seek(0)
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            item = new_dict.get(row[outer_key], dict())
            sub_item = item.get(row[inner_key1], dict())
            sub_item[row[inner_key2]] = {k: row[k] for k in inner_keyset}
            item[row[inner_key1]] = sub_item
            new_dict[row[outer_key]] = item
    return new_dict

# build specific nested dict from csv files
# a dict like {outer_key:{inner_key1:{inner_key2:inner_value}}}
# the params are extract from the csv column name as you like
def build_level3_dict2(source_file,outer_key,inner_key1,inner_key2,inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            item = new_dict.get(row[outer_key], dict())
            sub_item = item.get(row[inner_key1], dict())
            sub_item[row[inner_key2]] = row[inner_value]
            item[row[inner_key1]] = sub_item
            new_dict[row[outer_key]] = item
    return new_dict

# build specific nested dict from csv files
# a dict like {outer_key:{inner_key1:{inner_key2:[inner_value]}}}
# for multiple inner_value with the same inner_key2,thus gather them in a list
# the params are extract from the csv column name as you like
def build_level3_dict3(source_file,outer_key,inner_key1,inner_key2,inner_value):
    new_dict = {}
    with open(source_file, 'rb')as csv_file:
        data = csv.DictReader(csv_file, delimiter=",")
        for row in data:
            item = new_dict.get(row[outer_key], dict())
            sub_item = item.get(row[inner_key1], dict())
            sub_item.setdefault(row[inner_key2], []).append(row[inner_value])
            item[row[inner_key1]] = sub_item
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