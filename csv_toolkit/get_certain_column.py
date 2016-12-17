import csv
# import PlayerTransfer

# get certain column value of csv(for specific csv file ',' in header,';' in rows)
def get_column_value(file, column_name):
    with open(file, 'rb') as f:
        role_list = []
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=';')
        for row in reader:
            role_list.append(row[column_name])
        role_set = set(role_list)
        return sorted(list(role_set))




# team_list=get_column_value('2015players.csv','players.team')

# get certain column value of csv(for common csv file(',')),and judge if it's repeated
def get_column_value2(file, column_name):
    with open(file, 'rb') as f:
        role_list = []
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        for row in reader:
            role_list.append(row[column_name])
        role_set = set(role_list)
        return sorted(list(role_set))

s1_id=[]
s1_id=get_column_value2('id_map_all.csv','id')
# PlayerTransfer.List2csv.list2csv(s1_id,'the_s1_id.csv')