import csv



# eliminated the completely repeated record in repeated file for further analysis
def eliminate_repeated_row(in_file,out_file):
    with open(in_file,'rb') as in_file,open(out_file,'wb')as out_file:
        seen=set()
        for line in in_file:
            # print line
            if line in seen:continue

            seen.add(line)
            out_file.write(line)

# eliminate_repeated_row('black_list.csv','black_list_clean.csv')
# eliminate_repeated_row('repeated_id.csv','repeated_id_clean.csv')


# return a dict with the same value in original as new key and keys as value
def dict_same_value(original_dict):
    new_dict={}
    for k,v in original_dict.iteritems():
        new_dict.setdefault(v,[]).append(k)
    return new_dict


