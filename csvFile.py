import csv

with open('ArchivosCSV/users.csv', 'w', encoding='utf-8', newline='') as file:
    writer = csv.writer(file)
    field = ["Usuario", "Contraseña"]

    writer.writerow(field)
    writer.writerow(["Diego", "1234"])


users = ''
with open('ArchivosCSV/Usuarios.csv', newline='') as f:
    data = csv.reader(f, delimiter=',')
    users = list(data)
print(users)

def getData(users):
    for i in range(1, len(users)):
        for j in range(len(users[i])):
            print(users[i][j])
