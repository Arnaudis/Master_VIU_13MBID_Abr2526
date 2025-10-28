# Importación de librerías y supresión de advertencias
import pandas as pd
import warnings
import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path
from ydata_profiling import ProfileReport

def visualizar_datos(fuente: str="data/raw/bank-additional-full.csv", 
                     salida: str="docs/figures/"):
    """Genera una serie de gráficos sobre los datos y los exporta.
    
    Args:
        fuente (str, optional): Ruta al archivo de datos. Default es "data/raw/bank-additional-full.csv"
        salida (str, optional): Ruta al directorio de salida para los gráficos. Default es "docs/figures"
    """

    # Crea el directorio de salida si no existe
    Path(salida).mkdir(parents=True, exist_ok=True)

    # Leer los datos
    datos = pd.read_csv(fuente, sep=';')

    # Las tablas del dataset
    print(datos.info())

    # Gráfico 1: Distribución de la variable objetivo
    plt.figure(figsize=(8, 6))
    sns.countplot(x="y", data=datos)
    plt.title("Distribución de la variable objetivo (suscripción al depósito)")
    plt.xlabel("¿Suscribió un depósito a plazo?")
    plt.ylabel("Cantidad de clientes")
    # No mostramos en la libreta con plt.show() si no que lo guardamos
    plt.savefig(f"{salida}/1_distribucion_target.png")
    plt.close()

    # Gráfico 2: Distribución del nivel educativo
    plt.figure(figsize=(12, 4))
    col="education"
    order=datos[col].value_counts().index
    sns.countplot(y=col, data=datos, order=order)
    plt.title(f"Distribución de {col}")
    plt.xlabel("Cantidad")
    plt.ylabel(col)
    plt.savefig(f"{salida}/2_distribucion_educacion.png")
    plt.close()

    ##########################################################################
    #  AÑADIR DOS GRÁFICOS MÁS SIMILARES A LOS ANTERIORES
    ##########################################################################

    # Gráfico 3: Distribución de trabajos
    plt.figure(figsize=(12, 4))
    col="job"
    order=datos[col].value_counts().index
    sns.countplot(y=col, data=datos, order=order)
    # Cambio el nombre del titulo a español
    plt.title(f"Distribución de trabajo")
    plt.xlabel("Cantidad")
    plt.ylabel(col)
    plt.savefig(f"{salida}/3_distribucion_trabajo.png")
    plt.close()
    
    # Gráfico 4: Distribución de estado civil
    plt.figure(figsize=(8, 4))
    col="marital"
    order=datos[col].value_counts().index
    sns.countplot(y=col, data=datos, order=order)
    # Cambio el nombre del titulo a español
    plt.title(f"Distribución de estado civil")
    plt.xlabel("Cantidad")
    plt.ylabel(col)
    plt.savefig(f"{salida}/4_distribucion_estado_civil.png")
    plt.close()

    # Gráfico 5: Matriz de correlación
    num_df=datos.select_dtypes(include=['float64', 'int64'])
    corr=num_df.corr()
    plt.figure(figsize=(8, 12))
    sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
    plt.title('Matriz de correlaciones')
    plt.savefig(f"{salida}/5_matriz_correlacion.png")
    plt.close()

    # Gráfico 6: Estado civil vs suscripción al depósito (variable target)
    plt.figure(figsize=(10, 6))
    col="marital"
    order=datos[col].value_counts().index
    sns.countplot(y=col, data=datos, order=order, hue="y")
    plt.title("Distribución del estado civil según suscripción")
    plt.xlabel("Cantidad de clientes")
    plt.ylabel("Estado civil")
    plt.legend(title="¿Suscribió?")
    plt.tight_layout()
    plt.savefig(f"{salida}/6_estado_civil_vs_target.png")
    plt.close()



def informe_exploratorio():
    """Genera un informe exploratorio de los datos y lo guarda como HTML."""
    # Leer los datos
    datos=pd.read_csv("data/raw/bank-additional-full.csv", sep=';')
    # Generar el informe
    profile=ProfileReport(datos, title="Informe exploratorio del banco", explorative=True, minimal=True)
    # Mostrar en notebook
    # profile.to_notebook_iframe()
    # O guardar como HTML
    profile.to_file("docs/figures/7_Informe_banco.html")



# Podríamos hacer que se pidieran los archivos pero está implementado en la descripción de la función con 
# los valores por defecto del nombre de los archivos.
if __name__ == "__main__":
    visualizar_datos()
    informe_exploratorio()
