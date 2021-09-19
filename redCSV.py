import csv

with open('valores.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    Xfile=[]
    Yfile=[]
    
    for line in csv_reader:
        Xfile.append(line['x'])
        Yfile.append(line['y'])
    print(Xfile)
    print(Yfile)
