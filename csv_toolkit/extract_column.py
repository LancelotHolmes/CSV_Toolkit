import csv
# extract certain column from csv file according to the column#
def column_extract(file_in,file_out,index):
    with open(file_in,'r') as f_in:
        with open(file_out,'w') as f_out:
            for line in f_in:
                f_out.write(line.split(',')[index])
                f_out.write('\n')

#deal_file(r'E:\Research\1\offshoreleaks_data-csv\offshore_leaks_csvs\part\count\count_underlying.csv',r'E:\Research\1\offshoreleaks_data-csv\offshore_leaks_csvs\part\count\degree_underlying.csv')
def column_extract2(file_in,file_out,index):  # deal file for degree ('\n')
    with open(file_in,'r') as f_in:
        with open(file_out,'w') as f_out:
            for line in f_in:
                f_out.write(line.split(',')[index])