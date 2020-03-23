import pandas as pd
import numpy as np
from scipy.stats import variation
import matplotlib.pyplot as plt
import matplotlib

def CrearDataFrame(x, f):
    return pd.DataFrame({
        "x": x,
        "f": f,
        "fr": f / pd.Series(f).sum(),
        "fr%": (f / pd.Series(f).sum()) * 100,
        "F": pd.Series(f).cumsum(),
        "G": np.cumsum(f[::-1])[::-1]
    })

def Promedio(df):
    return np.repeat(df['x'], df['f']).mean()

def Varianza(df):
    return pd.Series.repeat(df["x"], df["f"]).var()

def DesvioEstandar(df):
    return pd.Series.repeat(df["x"], df["f"]).std()

def CoeficienteVariacion(df):
    desvio = DesvioEstandar(df)
    promedio = Promedio(df)
    return (desvio / promedio) * 100

def Moda(df):
    return pd.Series.repeat(df["x"], df["f"]).mode()

def Mediana(df):
    return pd.Series.repeat(df["x"], df["f"]).median()

def Histograma(df):
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)

    x = np.repeat(df['x'], df['f'])
    plt.yticks(df['f'])
    plt.xticks(df['x'])
    plt.hist(x, bins=df['x'], edgecolor='black', linewidth=2)

    