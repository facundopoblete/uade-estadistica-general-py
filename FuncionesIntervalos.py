import pandas as pd
import numpy as np
from scipy.stats import variation
import matplotlib.pyplot as plt
import matplotlib

def CrearDataFrame(LI, LS, f):
    return pd.DataFrame({
        "X": list(map(lambda index : '{} - {}'.format(LI[index],LS[index]), LI.index)),
        "LI": LI,
        "LS": LS,
        "f": f,
        "fr": f / pd.Series(f).sum(),
        "fr%": (f / pd.Series(f).sum()) * 100,
        "F": pd.Series(f).cumsum(),
        "G": np.cumsum(f[::-1])[::-1],
        "MP": (LI + LS) / 2
    })

def Promedio(df):
    return np.repeat(df['MP'], df['f']).mean()

def Varianza(df):
    promedio = Promedio(df)
    return (((df["MP"] - promedio) ** 2) * df['f']).sum() / (df['f'].sum() - 1)

def DesvioEstandar(df):
    varianza = Varianza(df)
    return np.sqrt(varianza)

def CoeficienteVariacion(df):
    desvio = DesvioEstandar(df)
    promedio = Promedio(df)
    return (desvio / promedio) * 100

def Moda(df):
    return df['X'][df['f'].idxmax()]

def Mediana(df):
    # Calculo Mediana
    #
    # Calcular n/2 y buscar el primer F que lo contenga.
    #
    # Me = LI + [ ( ((N/2) - F) / (f) ) * i]
    #
    div = pd.Series(df['f']).sum() / 2
    m = next(x for x, val in enumerate(df['F'].values) if val >= div)
    L = df.loc[m, 'LI']
    N = df['f'].sum()
    F = df.loc[m - 1, 'F']
    f = df.loc[m, 'f']
    C = (df['LS'] - df['LI']).loc[m]
    return L + ((N/2 - F)/(f)) * C

def Histograma(df):
    fig = matplotlib.pyplot.gcf()
    fig.set_size_inches(18.5, 10.5)

    x = np.repeat(df['LI'], df['f'])
    bins = pd.concat([df['LI'], df['LS']]).drop_duplicates()
    plt.yticks(df['f'])
    plt.xticks(bins)
    plt.hist(x, bins=bins, edgecolor='black', linewidth=2)
    
def Porcentaje(df, valorLimite, fila):
    n = df['f'].sum()
    fanterior = df.iloc[fila.index.values[0]-1].F
    return ( ( ( ( ( valorLimite - fila["LI"] ) / (fila["LS"] - fila["LI"]) ) * fila["f"] ) + fanterior) * 100 ) / n

def Percentil(df, k):
    n = df['f'].sum()
    valor = (n * k / 100)
    fila = df[df["X"] == df[(df["F"] >= valor) & (df["F"] > valor)].iloc[0].X]
    fanterior = df.iloc[fila.index.values[0]-1].F
    return fila["LI"] + ( ( ( (n * k) / 100 ) - fanterior ) / fila["f"] ) * (fila["LS"] - fila["LI"])

    