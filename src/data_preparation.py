import pandas as pd
import numpy as np
from datetime import datetime

IMPUT_CSV = 'data/raw/bank-additional-full.csv'
OUTPUT_CSV = 'data/processed/bank_processed.csv'

def preprocess_data(input_path=IMPUT_CSV, output_path=OUTPUT_CSV):
    # Cargo los datos
    df = pd.read_csv(input_path, sep=';')

    # Adaptar nombres de columnas
    df.columns = df.columns.str.replace('.', '_')

    # Transformar los valores 'unknown' en NaN
    df.replace('unknown', np.nan, inplace=True)

    # Se elimina la columna 'default' ya que tiene valores desconocidos
    df.drop(columns=['default'], inplace=True)

    # Se hace un filtro para eliminar las filas que tienen valores nulos
    df.dropna(inplace=True)

    # Se hace un filtro para eliminar las filas duplicadas
    df.drop_duplicates(inplace=True)

    # Cambiar valores de la columna 'y' a español de forma los valores serán 'Si' o 'No'
    # df['y'] = df['y'].map({'yes': 'Si', 'no': 'No'})
    
    # Mapear la columna objetivo 'y' a valores binarios
    map = {'yes': 1, 'no': 0}
    df['y'] = df['y'].map(map)

    # Cambiar valores de la columna 'contact' a español de forma los valores serán 'Móvil' o 'Telefono'
    df['contact'] = df['contact'].map({'cellular': 'Móvil', 'telephone': 'Teléfono'})

    # Graba el dataset procesado
    df.to_csv(output_path, index=False)


    sustituciones= [(df['y'] == 'yes').sum(), (df['y'] == 'no').sum(),
                     (df['contact'] == 'Móvil').sum(), (df['contact'] == 'Teléfono').sum()]
    return df.shape, sustituciones



# Esto se va a ejecutar como un script y no como parte de pytest.
# Por ello, hay que incluir este código
if __name__ == '__main__':
    dimensiones, sustituciones=preprocess_data()
    with open('docs/transformations.txt', 'w') as f:
        fecha_hora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        f.write(f"Transformaciones realizadas el {fecha_hora}:\n")
        f.write("Se reemplazaron los valores 'unknown' por NaN.\n")
        f.write("Se elimnaron las filas con valores nulos.\n")
        f.write("Se eliminaron las filas duplicadas.\n")
        f.write("Se eliminó la columna 'default' debido a la alta cantidad de valores desconocidos.\n")
        f.write(f"Cantidad de filas finales: {dimensiones[0]}\n")
        f.write(f"Cantidad de columnas finales: {dimensiones[1]}\n")
        f.write(f"En la columna 'y' se han cambiado {sustituciones[0]} valores 'yes' por 1 y {sustituciones[1]} valores 'no' por 0.\n")
        f.write(f"En la columna 'contact' se han cambiado {sustituciones[2]} valores 'cellular' por 'Móvil' y {sustituciones[3]} valores 'telephone' por 'Teléfono'.\n")