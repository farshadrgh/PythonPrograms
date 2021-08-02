import csv
import sys

with open('temp.csv', 'wt') as f:
    writer = csv.writer(f)
    writer.writerow(('id1', 'id2', 'date'))
    
    for i in range(3):
        row = (
            i + 1,
            chr(ord('a') + i),
            '01/{:02d}/2019'.format(i + 1),)
        writer.writerow(row)
        
print(open('temp.csv', 'rt').read())
