from operator import concat
import pandas as pd

diccionario = dict()

with open("AAportes_Privados_2017_en_excel_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        if (line.split(",")[1] == "PARTIDO"):
            diccionario[line.split(",")[0]] = ""

with open("Aportes_publicos_anual_arreglados_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        diccionario[line.split(",")[0]] = ""
        
with open("Candidaturas_2013_2017_arreglado_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        diccionario[line.split(",")[4]] = ""

with open("Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        diccionario[line.split(",")[5]] = ""

with open("Total_afiliados_partidos_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        diccionario[line.split(",")[0]] = ""

# Aporta más info
with open("Candidaturas_2021_arreglado_2.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        diccionario[line.split(",")[12]] = line.split(",")[11]

with open("Partidos.csv", "w") as document:
    i = 0
    print("ID,SIGLA,NOMBRE", file=document)
    for element in diccionario.keys():
        if (not element.startswith("IND ")):
            print(f"{i},{element},{diccionario[element]}", file=document)
            i += 1



