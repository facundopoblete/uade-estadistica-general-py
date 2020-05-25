from scipy.stats import norm
import numpy as np

def Normal_CalcularZ(x, u, o):
    return (x - u) / o

def Normal_Menor(x, u, o):
    z = Normal_CalcularZ(x, u, o)
    return (norm.cdf(z)).round(5)
    
def Normal_Mayor(x, u, o):
    z = Normal_CalcularZ(x, u, o)
    return (1-norm.cdf(z)).round(5)

def Normal_Entre(x, y, u, o):
    z1 = Normal_CalcularZ(x, u, o)
    z2 = Normal_CalcularZ(y, u, o)
    return ((1-norm.cdf(z1)) - (1-norm.cdf(z2))).round(5)

# Dado un X de la APP, obtener un X de la materia
def Normal_DespejarA(x,u,o):
    return round(((x*o)+u),4)

# Dado una probabilidad, buscar X menores EJ: P(X < a) = 0.975
def Normal_Menores_Dado_Probabilidad(p,u,o):
    return Normal_DespejarA(norm.ppf(p),u,o).round(5);s
    
# Dado una probabilidad, buscar X mayores EJ: P(X > a) = 0.25
def Normal_Mayores_Dado_Probabilidad(p,u,o):
    return Normal_DespejarA(norm.ppf(1-p),u,o).round(5);

def Normal_Menores_Desvio_Dado_Probabilidad_Promedio_ValorX(p,u,x):
    return ((x - u) / norm.ppf(p)).round(5)

def Normal_Mayores_Desvio_Dado_Probabilidad_Promedio_ValorX(p,u,x):
    return ((x - u) / norm.ppf(1-p)).round(5)

def Normal_Probabilidad_Menor_Sin_Z(p):
    return (norm.ppf(p)).round(5)

def Normal_Probabilidad_Mayor_Sin_Z(p):
    return (norm.ppf(1-p)).round(5)

def Normal_Calcular_O_y_U_2_Ecuaciones(x1,p1, x2,p2):
    m_list = [[p1, 1], [p2, 1]]
    A = np.array(m_list)
    B = np.array([x1, x2])
    return np.linalg.inv(A).dot(B)

def Normal_Menores_Media_Dado_Probabilidad_Desvio_ValorX(p,o,x):
    return (((norm.ppf(p) * o) - x) * -1).round(5)

def Normal_Mayores_Media_Dado_Probabilidad_Desvio_ValorX(p,o,x):
    return (((norm.ppf(1-p) * o) - x) * -1).round(5)