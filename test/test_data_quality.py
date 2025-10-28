from datetime import datetime
import pandas as pd
# Define test orientados a la estructura del datraframe pues viene de pandas
from pandera.pandas import DataFrameSchema, Column
# Controla todo a nivel general
import pytest
# Great Expectation... Genera casos de pruebas, expectation, que se van a validar en los datos

# No es correcto leer para cada test el dataframe.
# El decorador @pytest.fixture hace que se lea una sola vez y se pase a cada test. Pytest se encarga de gestionarlo.

@pytest.fixture
def datos_banco():
    """Carga los datos del banco desde el CSV
        Retorna:
        pd.DataFrame: DataFrame con los datos del banco
    """
    datos=pd.read_csv("data/raw/bank-additional-full.csv", sep=";")
    return datos



# Se hacen varios tests pq un test da verdadero o falso y si juntamos varias validaciones en un solo test, 
# puede que alguna falle y no sepamos cual.
def test_esquema(datos_banco):
    """Test para validar el esquema del dataframe del banco
        Args: (pd.DataFrame): DataFrame con los datos del banco   
    """
    dataset=datos_banco
    esquema = DataFrameSchema({
        "age": Column(int, nullable=False),
        "job": Column(str, nullable=False),
        "marital": Column(str, nullable=False),
        "education": Column(str, nullable=False),
        "default": Column(str, nullable=False),
        "housing": Column(str, nullable=False),
        "loan": Column(str, nullable=False),
        "contact": Column(str, nullable=False),
        "month": Column(str, nullable=False),
        "day_of_week": Column(str, nullable=False),
        "duration": Column(int, nullable=False),
        "campaign": Column(int, nullable=False),
        "pdays": Column(int, nullable=False),
        "previous": Column(int, nullable=False),
        "poutcome": Column(str, nullable=False),
        "emp.var.rate": Column(float, nullable=False),
        "cons.price.idx": Column(float, nullable=False),
        "cons.conf.idx": Column(float, nullable=False),
        "euribor3m": Column(float, nullable=False),
        "nr.employed": Column(float, nullable=False),
        "y": Column(str, nullable=False)
    })
    
    esquema.validate(dataset)



def test_basico(datos_banco):
    """Test básico para verificar que el datafram no esté vacío y tiene las columnas esperadas.
        
        Args: (pd.DataFrame): DataFrame con los datos del banco   
    """
    dataset=datos_banco
    # Verificar que el DataFrame no esté vacío
    assert not dataset.empty, "El DataFrame está vacío"
    # Validar que no hay valores nulos
    assert dataset.isnull().sum().sum() == 0, "El DataFrame contiene valores nulos"
    # Vefiricar que tiene filas duplicadas
    # Se ejecutará el siguiente assert tras las transformaciones que eliminen duplicados
    # assert dataset.duplicated().sum() == 0, "El DataFrame contiene filas duplicadas"
    # Validar que el número de columnas es el esperado
    assert dataset.shape[1] == 21, f"El DataFrame debería tener 21 columnas, pero tiene {dataset.shape[1]}"


# Comentamos ya que no vamos a generar el archivo test_results.txt desde aquí.     
# Para pasarlo a un pipeline, hay que convertirlo en un scrtip.py
# if __name__ == "__main__":
#     try:
#         # Ejecutar los tests directamente
#         test_esquema(datos_banco())
#         test_basico(datos_banco())
#         print("Todos los tests pasaron correctamente.")
#         with open("docs/test_results/test_results.txt", "w") as f:
#             # Grabamos fecha y hora
#             date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             f.write(f"{date}")
#             f.write("Todos los tests pasaron correctamente.\n")
#     except AssertionError as e:
#         print(f"Fallo en los tests: {e}")
#         with open("docs/test_results/test_results.txt", "w") as f:
#             date=datetime.now().strftime("%Y-%m-%d %H:%M:%S")
#             f.write(f"{date}")
#             f.write(f"Fallo en los tests: {e}\n")