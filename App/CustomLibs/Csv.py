import csv

def read_csv_file(filename):
    data = []
    with open(filename, 'r', encoding="utf8") as csvfile:
        reader = csv.reader(csvfile, delimiter=',', quotechar='|')
        print(reader.dialect)
        for row in reader:
            print(row)
            data.append(row)
    return data