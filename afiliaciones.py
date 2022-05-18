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

lista_a_devolver = []

with open("Total_afiliados_partidos_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        region_individuo = line.split(",")[4]
        region_individuo = region_individuo.replace("DEL LIBERTADOR BDO OHIGGINS", "DEL LIBERTADOR GENERAL BERNARDO O'HIGGINS")
        region_individuo = region_individuo.replace("DE MAGALLANES Y ANTARTICA CH", "DE MAGALLANES Y DE LA ANTARTICA CHILENA")
        region_individuo = region_individuo.replace("AISEN DEL GRAL CARLOS IBANEZ", "DE AYSEN DEL GENERAL CARLOS IBANEZ DEL CAMPO")
        region_individuo = region_individuo.replace("DE ", "")
        region_individuo = region_individuo.replace("DEL ", "")
        element = [
            partidos[line.split(",")[0]],
            line.split(",")[1],
            territorios[line.split(",")[2]],         
            regiones[region_individuo],
            line.split(",")[5]
        ]
        if (len(line.split(",")[3].replace(" ANOS", "").split("-")) > 1):
            element.append(line.split(",")[3].replace(" ANOS", "").split("-")[0])
            element.append(line.split(",")[3].replace(" ANOS", "").split("-")[1])
        else:
            element.append(line.split(",")[3].replace(" ANOS", "").replace(" O +", ""))
            element.append("")
        lista_a_devolver.append(element)

with open("Afiliaciones.csv", "w") as document:
    i = 0
    print("ID,PARTIDO.ID,CATEGORIA,TERRITORIO.ID,REGION.ID,SEXO,EDAD MIN, EDAD MAX", file=document)
    for element in lista_a_devolver:
        print(f"{i},{element[0]},{element[1]},{element[2]},{element[3]},{element[4]},{element[5]},{element[6]}", file=document)
        i += 1



