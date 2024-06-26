import csv
'''
with open('ArchivosCSV/users.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    field = ["Usuario", "Contraseña"]

    writer.writerow(field)
    writer.writerow(["Diego", "1234"])
'''

with open('ArchivosCSV/users.csv', encoding='utf-8', newline='') as f:
    data = csv.reader(f, delimiter=',')
    usr = list(data)
print(usr)

def getData(users):
    for i in range(1, len(users)):
        for j in range(len(users[i])):
            print(users[i][j])

getData(usr)
