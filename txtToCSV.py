import os
import sys

if len(sys.argv) != 2:
    print('Usage: python txtToTable.py <file_name w/o .txt>')
    sys.exit(1)

file_name = sys.argv[1]

data_path = 'data/'
file_path = data_path + file_name + '.txt'
if not os.path.isfile(file_path):
    print('File does not exist: ' + file_path)
    print('Make sure you put the file in the data/ directory.')
    sys.exit(1)

lines = []
with open(f'{file_path}', 'r') as f:
    for line in f:
        line = line.replace(',', '-')
        lines.append(line.strip().split('\t'))


csv_lines = []
for line in lines:
    csv_lines.append(','.join(line))

csv_txt = '\n'.join(csv_lines)

save_path = data_path + file_name + '.csv'
with open(f'{save_path}', 'w') as f:
    f.write(csv_txt)
