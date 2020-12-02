import csv
import pandas as pd

with open('data.csv', 'r') as file:
    reader = csv.reader(file, delimiter=',')
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
        else:
            print(f'{row[0]} has {row[1]} legs and was born in {row[2]}')
        line_count += 1
    print(f"CSV file has {line_count} lines")

with open('data.csv', 'r') as file:
    reader = csv.DictReader(file)
    line_count = 0
    for row in reader:
        if line_count == 0:
            print(f'Column names: {", ".join(row)}')
        else:
            print(f'{row["name"]} has {row["legs"]} legs and was born in {row["birthday_year"]}')
        line_count += 1
    print(f"CSV file has {line_count} lines")

with open('animals.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    writer.writerow(['hamster', 4, 2020])
    writer.writerow(['bird', 2, 2019])
    writer.writerow(['rat', 4, 2019])

with open('animals2.csv', 'w') as file:
    names = ['name', 'legs', 'birthday_year']
    writer = csv.DictWriter(file, fieldnames=names)

    writer.writeheader()
    writer.writerow({'name': 'bear', 'legs': 4, 'birthday_year': 2015})
    writer.writerow({'name': 'cow', 'legs': 4, 'birthday_year': 2016})

data_frame = pd.read_csv('data.csv')
print(data_frame)

data_frame_index = pd.read_csv('data.csv', index_col='name')
print(data_frame_index)

data_frame_date = pd.read_csv('data.csv', index_col='name', parse_dates=['birthday_year'])
print(data_frame_date)

data_frame_names = pd.read_csv(
    'animals_without_names.csv',
    index_col='name',
    parse_dates=['birthday_year'],
    names=['name', 'legs', 'birthday_year']
)
print(data_frame_names)

data_frame = pd.read_csv(
    'data.csv',
    index_col='name',
    parse_dates=['birthday_year'],
    header=0,
    names=['name', 'legs', 'birthday_year']
)
data_frame.to_csv('modified_data.csv')