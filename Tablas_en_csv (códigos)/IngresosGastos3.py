import re

def buscar_id_candidato(nombre, lista):
    nombre_set = set(nombre.split(" "))
    for element in lista:
        if nombre_set.issubset(element[0]):
            return element[1]
        elif element[0].issubset(nombre_set):
            return element[1]
    print(nombre)
    print(1/0)

def clean_partido(name):
    name = name.replace("PARTIDO ", "")
    name = name.replace("IND ", "")
    name = name.replace("DE ", "")
    name = name.replace("(EX-PAIS PROGRESISTA)", "")
    name = name.replace("INDEPENDIENTES", "INDEPENDIENTE")
    name = name.strip()
    return name


def clean_territorio(name):
    if "DISTRITO" in name:
        number = re.sub(r'[^0-9]+', '', name)
        name = "DISTRITO " + number
    elif "CIRCUNSCRIPCION" in name:
        number = re.sub(r'[^0-9]+', '', name)
        name = "CIRCUNSCRIPCION " + number
    return name


cuentas = dict()
with open("Tablas_en_csv/Cuentas.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip().split(",")
        cuentas[line[1]] = line[0]

aportantes = dict()
with open("Tablas_en_csv/Aportante.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip().split(",")
        aportantes[(line[1], line[2], line[3])] = line[0]

candidatura = dict()
with open("Tablas_en_csv/Candidatura.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip().split(",")
        candidatura[(line[1], line[2], line[4], line[5], line[6])] = line[0]

partidos = dict()
with open("Tablas_en_csv/Partidos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        partidos[line.split(",")[1]] = line.split(",")[0]

candidatos = list()
with open("Tablas_en_csv/Candidatos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        candidatos.append([set(line.split(",")[1].split(" ")), line.split(",")[0]])


with open("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "r") as document:
    lines = document.readlines()

with open("Tablas_en_csv/IngresosGastos.csv", "w") as document:
    print("ID,TIPO,CANDIDATO,APORTANTE,FECHA,CUENTA,MONTO,IDDOCUMENTO", file=document)
    fila = 0
    for line in lines[1::]:
        line = line.strip().split(",")
        col_candidato = buscar_id_candidato(line[3], candidatos)
        col_aportante = aportantes[(str(int(float(line[6]))), line[7], line[8])]
        col_cuenta = line[12]
        col_documento = line[14]
        print(str(fila) + "," + line[0] + "," + col_candidato + "," + col_aportante + "," + line[9] + "," + col_cuenta + "," + line[16] + "," + col_documento, file=document)
        fila +=1
