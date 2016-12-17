import csv
import csv_converter

# sort the csv file by certain column to put the similar record together for further analysis
def sort_csv_byColumn(in_file, out_file,column_name):
    with open(in_file, 'rb') as f:
        reader = csv.reader(f, delimiter=',')
        fieldnames = next(reader)
        reader = csv.DictReader(f, fieldnames=fieldnames, delimiter=',')
        sorted_list = sorted(reader, key=lambda row: row[column_name], reverse=True)
        # print sorted_list
        csv_converter.nestedlist2csv(sorted_list, out_file)

# sort_csv_byColumn('leagues_size.csv','ordered_leagues_size.csv','league_name')
sort_csv_byColumn('leagues_size.csv','orderedbysize_leagues_size.csv','league_size')
