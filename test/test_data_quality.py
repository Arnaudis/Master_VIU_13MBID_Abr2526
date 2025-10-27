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
    datos=pd.read_csv("data/raw/bank-additional-full.csv", sep=";")
    return datos



# Se hacen varios tests pq un test da verdadero o falso y si juntamos varias validaciones en un solo test, 
# puede que alguna falle y no sepamos cual.
def test_esquema(datos_banco):
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
