import re


def clean_partido(partido):
    partido = partido.replace("INDEPENDIENTES", "INDEPENDIENTE")
    partido = partido.replace("PARTIDO ", "")
    partido = partido.replace("DE ", "")
    return partido

'''
def clean_name(name, candidatos):
    if name.count(" ") == 3:
        col_candidato = name.split(" ")
        name = " ".join([col_candidato[0], col_candidato[2], col_candidato[3]])
        if (name in candidatos.keys()):
            col_candidato = candidatos[name]
        else:
            name = " ".join([col_candidato[2], col_candidato[0], col_candidato[1]])
            if (name in candidatos.keys()):
                col_candidato = candidatos[name]
            else:
                name = " ".join([col_candidato[3], col_candidato[0], col_candidato[2]])
                name = name.replace("BUSSI MARIA ALLENDE", "BUSSI ISABEL ALLENDE")
                name = name.replace("BURGOS NESTOR CRUCES", "BURGOS EDUARDO CRUCES")
                name = name.replace("ALVARADO ANDRES LEAL", "GUILLERMO ANDRES ALFONSO")
                name = name.replace("RIO RODRIGO DEL", "TOLEDO RODRIGO ALEJANDRO")
                name = name.replace("GALINDO RICARDO COGLER", "GALINDO NICOLAS COGLER")
                name = name.replace("INFANTE JUAN LETURIA", "INFANTE CRISTOBAL LETURIA")
                #print(name, "caso raro line 79")
                col_candidato = candidatos[name]
    elif name.count(" ") > 3:
        col_candidato = name.split(" ")
        name = " ".join([col_candidato[2], col_candidato[0], col_candidato[1]])
        name = name.replace("PEREZ LILY JOVANKA", "SAN LILY PEREZ")
        name = name.replace("YANNETT LILIAN TATIANA", "ESPINOZA TATIANA RUDOLPH")
        name = name.replace("BORJA FRANCISCO DE", "CORREA FRANCISCO EGUIGUREN")
        name = name.replace("RUBEN IVAN SIGFRIDO", "DAVID GUERRA LUNA")
        name = name.replace("CLAUDIO JUAN JOSE", "ARCOS JUAN JOSE")
        name = name.replace("CARMEN ANDREA DEL", "VIDAL ANDREA DUARTE")
        name = name.replace("HERRERA CLAUDIO ENRIQUE", "SAN CLAUDIO HERRERA")
        name = name.replace("ALEJANDRO DANIEL ARTURO", "ZUNIGA ARTURO MUNOZ")
        name = name.replace("DANIEL CLAUDIO PATRICIO", "MONTERO CLAUDIO PATRICIO")
        #print(line[3], "caso raro nombre largo line 85")
        col_candidato = candidatos[name]
    elif name.count(" ") == 2:
        col_candidato = name.split(" ")
        name = " ".join([col_candidato[0], col_candidato[1], col_candidato[2]])
        if (name in candidatos.keys()):
            col_candidato = candidatos[name]
        else:
            name = " ".join([col_candidato[2], col_candidato[0], col_candidato[1]])
            if (name in candidatos.keys()):
                col_candidato = candidatos[name]
            else:
                #print(line[3])
                name = " ".join([col_candidato[1], col_candidato[2], col_candidato[0]])
                name = name.replace("PALMA NUNEZ CLAUDIA", "PALMA CLAUDIA ANDREA")
                name = name.replace("FOITZICH SANDOVAL PAZ", "FOITZICH PAZ MARITZA")
                name = name.replace("MURILLO NEUMANN ANDREA", "MURILLO ANDREA MACARENA")
                name = name.replace("CUEVAS TRONCOSO RODRIGO", "BENITEZ RODRIGO CUEVAS")
                name = name.replace("LOPEZ VEGA CARLOS", "CARLOS ALARCON VEGA") #REVISAR
                name = name.replace("PEREZ MARIN JUAN", "PEREZ JUAN ANTONIO")
                name = name.replace("CROOCKER VILLA JEANNE", "CROOCKER JEANNE KATHERINE")
                name = name.replace("ROJAS OVANDO IVAN", "ROJAS IVAN ROBERTO")
                name = name.replace("VERGARA ARIAS ALEJANDRO", "VERGARA ALEJANDRO GERMAN")
                name = name.replace("LEAL ARAVENA FERNANDO", "LEAL FERNANDO ADILIO")
                name = name.replace("SUAREZ PEREZ GRACIELA", "SUAREZ GRACIELA HAYDEE")
                name = name.replace("ASTETE ALVAREZ CARLOS", "ASTETE CARLOS HERNAN")
                name = name.replace("BELMAR RUIZ BERTA", "BELMAR BERTA ANGELICA")
                name = name.replace("PINO SEGUEL HERNAN", "PINO HERNAN ORLANDO")
                name = name.replace("CENTONZIO ROSSEL GIGLIOLA", "CENTONZIO GIGLIOLA ELINA")
                name = name.replace("SALDIAS CARRENO PATRICIA", "SALDIAS PATRICIA WALEWESKA")
                name = name.replace("LOBOS LOBOS JULIO", "LOBOS JULIO OMAR")
                name = name.replace("LAGOS LIZAMA FABIOLA", "LAGOS FABIOLA PATRICIA")
                name = name.replace("JOUANNET VALDERRAMA ANDRES", "JOUANNET ANDRES ALFONSO")
                name = name.replace("ALLENDE GONZALEZ GUILLERMO", "ALLENDE GUILLERMO ISMAEL")
                name = name.replace("NUYADO ANCAPICHUN EMILIA", "NUYADO EMILIA IRIS")
                name = name.replace("PARISI FERNANDEZ ZANDRA", "PARISI ZANDRA ESTHER")
                name = name.replace("VERGARA MALDONADO FELIPE", "VERGARA LUIS FELIPE")
                name = name.replace("BOSSHARD PENA LISETTE", "BOSSHARD LISETTE HEDWIG")
                name = name.replace("GARCIA ASPILLAGA PEDRO", "GARCIA PEDRO ENRIQUE")
                name = name.replace("SUAREZ BRIONES PAZ", "SUAREZ PAZ ANDREA")
                name = name.replace("MADRID FUENTES JULIO", "MADRID JULIO ENRIQUE")
                name = name.replace("VARAS MONTERO MELISSA", "VARAS MELISSA ESTEFANIA")
                name = name.replace("URIBE FLORES SANDRA", "URIBE SANDRA ELENA")
                name = name.replace("BOZAN RAMOS ANGEL", "BOZAN ANGEL RICARDO")
                col_candidato = candidatos[name]
    else:
        col_candidato = name
        col_candidato = candidatos[col_candidato]
    return col_candidato
'''
def buscar_id_candidato(nombre, lista):
    nombre_set = set(nombre.split(" "))
    for element in lista:
        if nombre_set.issubset(element[0]):
            return element[1]
        elif element[0].issubset(nombre_set):
            return element[1]
    print(nombre)
    print(1/0)

def clean_territorio(name):
    if "DISTRITO" in name:
        number = re.sub(r'[^0-9]+', '', name)
        name = "DISTRITO " + number
    elif "CIRCUNSCRIPCION" in name:
        number = re.sub(r'[^0-9]+', '', name)
        name = "CIRCUNSCRIPCION " + number
    return name

partidos = dict()
with open("Tablas_en_csv/Partidos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        partidos[line.split(",")[1]] = line.split(",")[0]

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

candidaturas = dict()
with open("Tablas_en_csv/Candidatura.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        candidaturas[(line.split(",")[1], line.split(",")[3],line.split(",")[4],line.split(",")[5])] = line.split(",")[0]

with open("CSV limpios/Aportes_Privados_2017_partido_CLEAN.csv", "r") as document:
    lines = document.readlines()


with open("Tablas_en_csv/Aportes_Privados_2017_partido.csv", "w") as document:
    fila = 0
    print("ID,NOMBRE APORTANTE, TIPO APORTANTE, CARGO, PARTIDO, TIPO APORTE, FECHA, MONTO", file=document)
    for line in lines[1::]:
        line = line.strip().split(",")
        if (line[6] != line[2]):
            continue
        partido_id_1 = partidos[clean_partido(line[2])]
        ano = line[8].split("-")[2]
        cargo = line[4].replace("PRESIDENTE", "PRESIDENCIAL")
        print(str(fila) + "," + line[0] + "," + line[1] + "," + cargo + "," + partido_id_1 + "," + line[7] + "," + line[8] + "," + line[9], file=document)
        fila += 1
