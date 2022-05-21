from operator import concat
import pandas as pd

diccionario = dict()

with open("Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        diccionario[line.split(",")[12]] = line.split(",")[13]

with open("Cuentas.csv", "w") as document:
    print("ID,DESCRIPCION", file=document)
    for element in diccionario.keys():
        print(f"{element},{diccionario[element]}", file=document)



