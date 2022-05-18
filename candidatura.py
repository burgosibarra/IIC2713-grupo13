from operator import concat
import pandas as pd

partidos = dict()

with open("Partidos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        partidos[line.split(",")[1]] = line.split(",")[0]

regiones = dict()

with open("Region.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        region = line.split(",")[1]
        region = region.replace("DE ", "")
        region = region.replace("DEL ", "")
        regiones[region] = line.split(",")[0]

territorios = dict()

with open("Territorio.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        territorios[line.split(",")[1]] = line.split(",")[0]

candidatos = dict()

with open("Candidatos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        candidatos[line.split(",")[1]] = line.split(",")[0]


lista_a_devolver = set()
'''
with open("Candidaturas_2021_arreglado_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        region_candidatura = line.split(",")[2]
        region_candidatura = region_candidatura.replace("DE ", "")
        region_candidatura = region_candidatura.replace("DEL ", "")
        element = (
            line.split(",")[0],
            regiones[region_candidatura],
            territorios[line.split(",")[3]],
            candidatos[line.split(",")[4]],
            2021,
            partidos[line.split(",")[12]]
        )

        lista_a_devolver.add(element)
'''
with open("Candidaturas_2013_2017_arreglado_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        element = (
            line.split(",")[1],
            line.split(",")[2].replace(".0",""),
            territorios[line.split(",")[3]],
            candidatos[line.split(",")[5]],
            line.split(",")[0],
            partidos[line.split(",")[4]]
        )

        lista_a_devolver.add(element)

with open("Candidatura.csv", "w") as document:
    i = 0
    print("ID,CARGO,REGION.ID,TERRITORIO.ID,CANDIDATO.ID,ANO,PARTIDO.ID", file=document)
    for element in lista_a_devolver:
        print(f"{i},{element[0]},{element[1]},{element[2]},{element[3]},{element[4]},{element[5]}", file=document)
        i += 1



