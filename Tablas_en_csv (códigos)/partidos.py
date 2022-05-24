from operator import concat
import pandas as pd


def clean(name):
    name = name.replace("PARTIDO ", "")
    name = name.replace("DE ", "")
    name = name.replace("(EX-PAIS PROGRESISTA)", "")
    name = name.replace("INDEPENDIENTES", "INDEPENDIENTE")
    name = name.strip()
    return name


diccionario = dict()

with open("CSV limpios/Aportes_Privados_2017_partido_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        if (line.split(",")[1] == "PARTIDO"):
            name = clean(line.split(",")[0])
            diccionario[name] = ""

with open("CSV limpios/Aportes_Privados_2017_candidato_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        if (line.split(",")[1] == "PARTIDO"):
            name = clean(line.split(",")[0])
            diccionario[name] = ""

with open("CSV limpios/Aportes_publicos_anual_arreglados_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        name = clean(line.split(",")[0])
        diccionario[name] = ""
        
with open("CSV limpios/Candidaturas_2013_2017_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        name = clean(line.split(",")[4])
        diccionario[name] = ""

with open("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        name = clean(line.split(",")[5])
        diccionario[name] = ""

with open("CSV limpios/Total_afiliados_partidos_CLEAN2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        name = clean(line.split(",")[0])
        diccionario[name] = ""

# Aporta más info
with open("CSV limpios/Candidaturas_2021_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        name = clean(line.split(",")[12])
        diccionario[name] = line.split(",")[11]

with open("Tablas_en_csv/Partidos.csv", "w") as document:
    i = 0
    print("ID,SIGLA,NOMBRE", file=document)
    for element in diccionario.keys():
        if (not element.startswith("IND ")):
            print(f"{i},{element},{diccionario[element]}", file=document)
            i += 1



