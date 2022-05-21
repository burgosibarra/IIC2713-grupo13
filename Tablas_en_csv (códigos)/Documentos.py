
tipos_docs = dict()
with open("Tablas_en_csv/Tipo_documento.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip().split(",")
        tipos_docs[(line[1], line[2])] = line[0]

documentos = dict()
with open("CSV arreglados/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip().split(",")
        documentos[int(line[14])] = (tipos_docs[(line[10], line[11])], line[15])

with open("Tablas_en_csv/Documento.csv", "w") as document:
    print("ID,TIPO DOCUMENTO,GLOSA", file=document)
    for id in documentos.keys():
        print(str(id) + "," + documentos[id][0] + "," + documentos[id][1], file=document)