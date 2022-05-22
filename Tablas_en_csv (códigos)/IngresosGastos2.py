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

candidatos = dict()
with open("Tablas_en_csv/Candidatos.csv", "r") as document:
    lines = document.readlines()
    for line in lines[1::]:
        line = line.strip()
        candidatos[line.split(",")[1]] = line.split(",")[0]


with open("CSV limpios/Ingresos_Gastos_2017_Candidatos_CLEAN.csv", "r") as document:
    lines = document.readlines()

with open("Tablas_en_csv/IngresosGastos.csv", "w") as document:
    print("ID,TIPO,CANDIDATO,APORTANTE,FECHA,CUENTA,MONTO", file=document)
    fila = 0
    for line in lines[1::]:
        line = line.strip().split(",")
        if line[3].count(" ") == 3:
            col_candidato = line[3].split(" ")
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
        elif line[3].count(" ") > 3:
            col_candidato = line[3].split(" ")
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
        elif line[3].count(" ") == 2:
            col_candidato = line[3].split(" ")
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
            col_candidato = line[3]
            #print("CASO RARO ", col_candidato)
            col_candidato = candidatos[col_candidato]
        col_aportante = aportantes[(str(int(float(line[6]))), line[7], line[8])]
        col_cuenta = line[12]
        print(str(fila) + "," + line[0] + "," + col_candidato + "," + col_aportante + "," + line[9] + "," + col_cuenta + "," + line[16], file=document)
        fila +=1
