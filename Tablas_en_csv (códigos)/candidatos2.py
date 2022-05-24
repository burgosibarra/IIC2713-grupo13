id = 0
names = dict()
info = dict()

with open("CSV limpios/Candidaturas_2021_CLEAN.csv", "r") as document:
    lines_2021 = document.readlines()
    
with open("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", "r") as document:
    lines_2013_2017 = document.readlines()

for line in lines_2021[1::]:
    line = line.strip().split(",")
    col_name = line[4]
    info[col_name] = [line[8], line[9]]
    col_name_set = set(col_name.split(" "))
    found = False
    for name in names.keys():
        name_set = set(name.split(" "))
        if col_name_set.issubset(name_set):
            found = True
            break
        elif name_set.issubset(col_name_set):
            names[col_name] = names[name]
            del names[name]
            found = True
            break
    if not found:
        names[col_name] = id
        id += 1

print("2021 is finished")

for line in lines_2013_2017[1::]:
    line = line.strip().split(",")
    col_name = line[5]
    info[col_name] = [line[6], line[7]]
    col_name_set = set(col_name.split(" "))
    found = False
    for name in names.keys():
        name_set = set(name.split(" "))
        if col_name_set.issubset(name_set):
            found = True
            break
        elif name_set.issubset(col_name_set):
            names[col_name] = names[name]
            del names[name]
            found = True
            break
    if not found:
        names[col_name] = id
        id += 1

print("2013_2017 is finished")

with open("Tablas_en_csv/Candidatos.csv", "w") as document:
    print("ID,NOMBRE,SEXO,EDAD", file=document)
    for name in names.keys():
        print(str(names[name]) + "," + name + "," + info[name][0] + "," + info[name][1], file=document)