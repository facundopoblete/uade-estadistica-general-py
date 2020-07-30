from scipy.stats import norm
import scipy.stats
import math
import numpy as np
from sympy import symbols, solve

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

def Normal_Funcion_Imagen(x,u,o):
    return (1 / (pow((2*math.pi),0.5)*o)) * pow(math.e, (-1/(2*pow(o,2))*pow((x-u),2)))


##########
## LOG NORMAL
##########

def LogNormal_Calcular_Mediana(u, o):
    return pow(math.e, LogNormal_Calcular_m(u,o));
               
def LogNormal_Calcular_Moda(u, o):
    return pow(math.e, LogNormal_Calcular_m(u,o) - pow(LogNormal_Calcular_D(u,o),2));

def LogNormal_Calcular_D(u, o):
    return pow(np.log(1+pow(o/u,2)),0.5)
    
def LogNormal_Calcular_m(u, o):
    return np.log((u)/(pow((1+pow(o/u,2)), 0.5)))

def LogNormal_Mayor(x,u,o):
    return 1-scipy.stats.lognorm(s=LogNormal_Calcular_D(u,o) , scale=math.exp(LogNormal_Calcular_m(u,o))).cdf(x)

def LogNormal_Mayor_m_d(x,m,d):
    return 1-scipy.stats.lognorm(s=d , scale=math.exp(m)).cdf(x)

def LogNormal_Menor_m_d(x,m,d):
    return scipy.stats.lognorm(s=d , scale=math.exp(m)).cdf(x)

def LogNormal_Menor(x,u,o):
    return scipy.stats.lognorm(s=LogNormal_Calcular_D(u,o) , scale=math.exp(LogNormal_Calcular_m(u,o))).cdf(x)

def LogNormal_Entre(x1,x2,u,o):
    return scipy.stats.lognorm(s=LogNormal_Calcular_D(u,o) , scale=math.exp(LogNormal_Calcular_m(u,o))).cdf(x2-x1)

def LogNormal_Porcentaje_Menor(p,u,o):
    return scipy.stats.lognorm(s=LogNormal_Calcular_D(u,o) , scale=math.exp(LogNormal_Calcular_m(u,o))).ppf(p)

def LogNormal_Porcentaje_Mayor(p,u,o):
    return scipy.stats.lognorm(s=LogNormal_Calcular_D(u,o) , scale=math.exp(LogNormal_Calcular_m(u,o))).ppf(1-p)

##########
## POISSON
##########

def Poisson_Calcular_m(lamb, t):
    return lamb * t;

def Poisson_Mayor(x, lamb, t):
    return 1-scipy.stats.poisson.cdf(x, Poisson_Calcular_m(lamb,t))

def Poisson_Menor(x, lamb, t):
    return scipy.stats.poisson.cdf(x, Poisson_Calcular_m(lamb,t))

def Poisson_Calcular_m_Teniendo_Probabilidad_X(p,x, lamb):
    m = symbols('m')
    expr = pow(math.e, -m) * pow(m, x) / math.factorial(x) - p
    return solve(expr)[0] / lamb

##########
## GAMMA
##########

def Gamma_Calcular_Modo(x, lamb):
    return (x-1)/lamb

def Gamma_Calcular_Mediana(x, lamb):
    return (x/lamb) * pow((1-(1/(9*x))),3)

##########
## PARETO
##########

def Pareto_Calcular_Esperanza(tita, b):
    return (b*tita) / (b-1)

def Pareto_Calcular_b_Teniendo_Esperanza_y_tita(esperanza, tita):
    return esperanza / (esperanza - tita)

def Pareto_Calcular_Mediana(tita, b):
    return tita * pow(2,1/b)

def Pareto_Calcular_Menores(tita,b,x):
    return 1 - pow( (tita / x) ,b)

def Pareto_Calcular_Mayores(tita,b,x):
    return pow( (tita / x) ,b)

##########
## UNIFORME
##########

def Uniforme_Calcular_Entre(a,b,x,y):
    return Uniforme_Calcular_Menores(a,b,y) - Uniforme_Calcular_Menores(a,b,x)

def Uniforme_Calcular_Menores(a,b,x):
    return (x-a)/(b-a)

def Uniforme_Calcular_Mayores(a,b,x):
    return 1-Uniforme_Calcular_Menores(a,b,x)

def Uniforme_Calcular_Mediana(a,b):
    return (a+b)/2

def Uniforme_Calcular_Esperanza(a,b):
    return (a+b)/2

def Uniforme_Calcular_Densidad(a,b):
    return 1/(b-a)

def Uniforme_Calcular_Varianza(a,b):
    return pow((b-a), 2) / 12

##########
## Weibull
##########

def Weibull_Calcular_Menores(beta,omega,x):
    return 1 - pow(math.e, pow(-(x/beta), omega))

def Weibull_Calcular_Mayores(beta,omega,x):
    return 1-Weibull_Calcular_Menores(beta,omega,x)

def Weibull_Calcular_Mediana(beta,omega):
    return beta * pow(math.log(2), (1/omega))

def Weibull_Calcular_Densidad_Probabilidad(beta,omega,x):
    return omega * pow((1/beta), omega) * pow(x, omega-1) * pow(math.e, pow(-(x/beta), omega))

def Weibull_Entre(x, y, beta,omega):
    p1 = Weibull_Calcular_Menores(beta,omega, y)
    p2 = Weibull_Calcular_Menores(beta,omega, x)
    return p1 - p2

##########
## Gumbel del minimo
##########

def Gumbel_Minimo_Calcular_Menores(beta,tita,x):
    return 1 - pow(math.e, pow(-math.e, (x-tita)/beta))

def Gumbel_Minimo_Calcular_Mayores(beta,tita,x):
    return 1-Gumbel_Calcular_Menores(beta,tita,x)

def Gumbel_Minimo_Calcular_Mediana(beta,tita):
    return tita + beta * math.log(math.log(2))

def Gumbel_Minimo_Calcular_Varianza(beta,tita):
    return (pow(math.pi,2)/6) * pow(beta,2)

def Gumbel_Minimo_Calcular_Esperanza(beta,tita):
    return tita - (beta * 0.577215664)

##########
## Gumbel del maximo
##########

def Gumbel_Maximo_Calcular_Menores(beta,tita,x):
    return pow(math.e, pow(-math.e, -(x-tita)/beta))

def Gumbel_Maximo_Calcular_Mayores(beta,tita,x):
    return 1-Gumbel_Maximo_Calcular_Menores(beta,tita,x)

def Gumbel_Maximo_Calcular_Mediana(beta,tita):
    return tita - beta * math.log(math.log(2))

def Gumbel_Maximo_Calcular_Varianza(beta,tita):
    return (pow(math.pi,2)/6) * pow(beta,2)

def Gumbel_Maximo_Calcular_Esperanza(beta,tita):
    return tita + (beta * 0.577215664)