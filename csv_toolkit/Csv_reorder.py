import csv
# reorder the column of the csv file to what you want
def csv_reorder(in_file, out_file,lst_order):
    with open(in_file, 'rb') as infile, open(out_file, 'wb') as outfile:
        fieldnames=lst_order
        writer = csv.DictWriter(outfile, fieldnames=fieldnames)
        writer.writeheader()
        for row in csv.DictReader(infile):
            writer.writerow(row)


lst_order = ['league_name','season_id','league_size']
csv_reorder('leagues_size.csv', 'leagues_size_new.csv', lst_order)
