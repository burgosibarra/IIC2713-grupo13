from operator import index
import pandas as pd
import openpyxl
df_1 = pd.read_csv("CSV arreglados/Candidaturas_2013_2017_arreglado_2.csv", header=0)
df_2 = pd.read_csv("CSV arreglados/Candidaturas_2021_arreglado_2.csv", header=0)
df_3 = pd.read_csv("CSV arreglados/AAportes_Privados_2017_en_excel_2.csv", header=0)
df_4 = pd.read_csv("CSV arreglados/Total_afiliados_partidos_CLEAN.csv", header=0)
df_derivated_1 = df_1[['TERRITORIO']]
df_derivated_2 = df_2[['TERRITORIO']]
df_3[['TERRITORIO']] = df_3[['Territorio']]
df_derivated_3 = df_3[['TERRITORIO']]
df_4[['TERRITORIO']] = df_4[['COMUNA']]
df_derivated_4 = df_4[['TERRITORIO']]
df_derivated = pd.concat([df_derivated_1, df_derivated_2, df_derivated_3, df_derivated_4])
data = df_derivated
df_without_duplicates = data.drop_duplicates()
df_without_duplicates['ID'] = df_without_duplicates.index
df_derivated_final = df_without_duplicates[['ID', 'TERRITORIO']]
df_derivated_final.to_csv("Territorio.csv", index=False)

print(df_derivated.head(5))