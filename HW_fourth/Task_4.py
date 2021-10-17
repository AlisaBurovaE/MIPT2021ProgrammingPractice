import csv

with open("C:/Users/MI/Documents/прога/local_repo/MIPT2021ProgrammingPractice/HW_fourth/table.csv", "r") as file:
    reader = csv.reader(file, delimiter=';')
    list = list()
    for x in reader:
        list.append(x)

list.insert(3, [0, 0, 0, 0, 0, 0])
for i in range(1, len(list)):
    list[i].insert(3, 0)

with open("new.csv", "w") as file:
    writer = csv.writer(file)          
    for data in list:
        writer.writerow(data)
