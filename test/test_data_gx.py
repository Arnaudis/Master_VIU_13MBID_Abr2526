import pandas as pd

def test_great_expectations():
    """Test para verificar que los datos cumplen con las expectativas definidas en un archivo de Great Expectations.
    
    Raises:
        AssertionError: Si alguna de las expectativas no se cumple.
    """
    # Cargar los datos
    df = pd.read_csv("data/raw/bank-additional-full.csv", sep=";")

    results={
        "success": True,
        "expectations":[],
        "statistics":{"success_count":0, "total_count":0}
    }

    def add_expectation(expectation_name, condition, message=""):
        results["statistics"]["total_count"] += 1
        if condition:
            results["statistics"]["success_count"] += 1
            results["expectations"].append({
                "expectation": expectation_name,
                "success": True
            })
        else:
            results["success"] = False
            results["expectations"].append({
                "expectation": expectation_name,
                "success": False,
                "message": message
            })

    # Validaciones a verificar sobre los datos
    # Comprobamos que la edad esté comprendida entre 18 y 100 años.
    add_expectation(
        "Rango de edad",
        df["age"].between(18, 100).all(),
        "La columna 'age' no está en el rango esperado (18-100)."
    )

    # Comprobamos que los valores de la columna target 'y' sean solo 'yes' o 'no'.
    add_expectation(
        "Valores target",
        df["y"].isin(["yes", "no"]).all(),
        "La columna 'y' contiene valores distintos a 'yes' o 'no'."
    )

    # Comprobamos que el estado civil tenga valores entre los establecidos. 
    add_expectation(
        "Estado civil",
        df["marital"].isin(["divorced", "married", "single", "unknown"]).all(),
        "La columna de estado civil contiene valores distintos a los establecidos."
    )

    # Comprobamos el modo del tipo de contacto establecido.
    add_expectation(
        "Modo de contacto establecido",
        df["contact"].isin(["cellular", "telephone"]).all(),
        "La columna referente al modo de contacto establecido contiene valores que no están definidos."
    )

    # Comprobamos que el número de contactos realizados, campaing, sea positivo.
    add_expectation(
        "Número de contactos",
        (df["campaign"]>0).all(),
        "La columna 'campaign' contiene valores negativos."
    )