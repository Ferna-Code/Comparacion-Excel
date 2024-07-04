import pandas as pd
import os

file1_path = 'ExcelSAS.xlsx'
file2_path = 'ExcelBBDD.xlsx'
contador_path = 'contador.txt'

if os.path.exists(contador_path):
    with open(contador_path, 'r') as f:
        contador = int(f.read().strip())
else:
    contador = 0

df1 = pd.read_excel(file1_path)
df2 = pd.read_excel(file2_path)

print("Columnas del primer DataFrame:")
print(df1.columns)
print("\nColumnas del segundo DataFrame:")
print(df2.columns)

merged_df = pd.merge(df1, df2, left_on='Patente', right_on='Patente', how='left')

selected_columns = merged_df[['Nro. Dcto', 'Nro. PO', 'Nombre Sucursal', 'Patente', 'Fecha Apertura', 'Tipo Pedido', 'fecha', 'hora', 'entrada', 'salida']]
selected_columns.columns = ['Nro. Dcto', 'Nro. PO', 'Sucursal', 'Patente', 'Fecha Apertura', 'Tipo Pedido', 'Fecha Movimiento', 'Hora Movimiento', 'Entrada', 'Salida']

output_path = f'archivosCreados/archivoCombinado{contador}.xlsx'
contador += 1
selected_columns.to_excel(output_path, index=False)
print(f'Datos combinados guardados en {output_path}')

with open(contador_path, 'w') as f:
    f.write(str(contador))