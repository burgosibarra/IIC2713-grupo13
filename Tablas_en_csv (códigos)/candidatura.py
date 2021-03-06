from operator import concat
import pandas as pd
import re

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

def buscar_id_candidato(nombre, lista):
    if (nombre == "SANTANA CARMONA MIGUEL" or nombre == "MIGUEL SANTANA CARMONA"):
        nombre += " ARNOLDO"
    nombre_set = set(nombre.split(" "))
    for element in lista:
        if nombre_set.issubset(element[0]):
            return element[1]
        elif element[0].issubset(nombre_set):
            return element[1]
    print(nombre)
    print(1/0)

partidos = dict()

with open("Tablas_en_csv/Partidos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        partidos[line.split(",")[1]] = line.split(",")[0]

regiones = dict()

with open("Tablas_en_csv/Region.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        region = line.split(",")[1]
        region = region.replace("DE ", "")
        region = region.replace("DEL ", "")
        regiones[region] = line.split(",")[0]

territorios = dict()

with open("Tablas_en_csv/Territorio.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        territorios[line.split(",")[1]] = line.split(",")[0]

candidatos = list()

with open("Tablas_en_csv/Candidatos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        candidatos.append([set(line.split(",")[1].split(" ")), line.split(",")[0]])


lista_a_devolver = set()

with open("CSV limpios/Candidaturas_2021_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        region_candidatura = line.split(",")[2]
        region_candidatura = region_candidatura.replace("DE ", "")
        region_candidatura = region_candidatura.replace("DEL ", "")
        element = (
            line.split(",")[0],
            regiones[region_candidatura],
            territorios[clean_territorio(line.split(",")[3])],
            buscar_id_candidato(line.split(",")[4], candidatos),
            2021,
            partidos[clean_partido(line.split(",")[12])]
        )

        lista_a_devolver.add(element)

with open("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        element = (
            line.split(",")[1],
            line.split(",")[2].replace(".0",""),
            territorios[clean_territorio(line.split(",")[3])],
            buscar_id_candidato(line.split(",")[5], candidatos),
            line.split(",")[0],
            partidos[clean_partido(line.split(",")[4])]
        )
        if(line == "2017,CONSEJEROS REGIONALES,9.0,CAUTIN 1,PARTIDO POR LA DEMOCRACIA,MIGUEL SANTANA CARMONA,HOMBRE,48"):
            print(element)

        lista_a_devolver.add(element)

with open("Tablas_en_csv/Candidatura.csv", "w") as document:
    i = 0
    print("ID,CARGO,REGION.ID,TERRITORIO.ID,CANDIDATO.ID,ANO,PARTIDO.ID", file=document)
    for element in lista_a_devolver:
        print(f"{i},{element[0]},{element[1]},{element[2]},{element[3]},{element[4]},{element[5]}", file=document)
        i += 1



