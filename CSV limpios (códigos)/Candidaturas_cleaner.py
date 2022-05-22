import re
import pandas as pd

# "Candidaturas_2013_2017.csv"

output_document = open("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", "w")

with open('Originales/Candidaturas_2013_2017.csv', encoding="UTF-8", mode="r") as document:
    lines = document.readlines()
    fila = 0
    for line in lines:
        line = line.strip()
        line = line.strip(";")
        line = line.upper()
        line = line.replace("Á", "A")
        line = line.replace("É", "E")
        line = line.replace("Í", "I")
        line = line.replace("Ó", "O")
        line = line.replace("Ú", "U")
        line = line.replace("Ý", "Y")
        line = line.replace("Ñ", "N")
        columns = line.split(";")
        if (fila == 0):
            total_columnas = len(columns)
        if (len(columns) > total_columnas):
            continue
        for i in range(0, len(columns)):
            columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
            columns[i] = ' '.join(columns[i].split())
        '''
        if (fila != 0):
            name = columns[5].split(" ")
            if (len(name) > 2):
                columns[5] = name[2] + " " + name[0] + " " + name[1]
            else:
                columns[5] = name[1] + " " + name[0]
        '''
        new_line = ';'.join(columns)
        print(new_line, file=output_document)
        fila += 1
output_document.close()

df = pd.read_csv("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
# df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", index=False)


# "Candidaturas_2021.csv"

output_document = open("CSV limpios/Candidaturas_2021_CLEAN.csv", "w")
i = 0
with open("Originales/Candidaturas_2021.csv", encoding="UTF-8", mode="r") as document:
    lines = document.readlines()
    fila = 0
    for line in lines:
        line = line.strip()
        line = line.strip(";")
        line = line.upper()
        line = line.replace("Á", "A")
        line = line.replace("É", "E")
        line = line.replace("Í", "I")
        line = line.replace("Ó", "O")
        line = line.replace("Ú", "U")
        line = line.replace("Ý", "Y")
        line = line.replace("Ñ", "N")
        columns = line.split(";")
        if (fila == 0):
            total_columnas = len(columns)
            index_rango = columns.index("RANGO")
        if (len(columns) != total_columnas):
            continue
        for i in range(0, len(columns)):
            if (i != index_rango):
                columns[i] = re.sub(r'[^A-Za-z0-9 ]+', '', columns[i])
            columns[i] = ' '.join(columns[i].split())
        '''
        if (fila != 0 and columns[5] != "" and columns[6] != "" and columns[7] != ""):
            columns[4] = columns[5].split(" ")[0]
            columns[4] += " " + columns[6] + " " + columns[7]
        elif (fila != 0):
            if (columns[4].count(" ") >= 3):
                nombre = columns[4].split(" ")
                columns[4] = nombre[0] + " " + nombre[2] + " " + nombre[3]
        '''
        if (columns[-1] != ""):
            new_line = ';'.join(columns)
            print(new_line, file=output_document)
        fila += 1
output_document.close()

df = pd.read_csv("CSV limpios/Candidaturas_2021_CLEAN.csv", header=0, sep=";")

df_without_duplicates = df.drop_duplicates()
#df_without_null = df_without_duplicates.dropna()
df_without_duplicates.to_csv("CSV limpios/Candidaturas_2021_CLEAN.csv", index=False)
