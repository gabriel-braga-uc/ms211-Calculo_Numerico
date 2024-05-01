## This method approximates the root of a continuous function in a initial pre determined interval [a, b] by checking where the tangent line of a starting point crosses the x-axis, then choosing a new tangent line vertically above this intersection and on and on... ##
import math
from decimal import *

getcontext().prec = 100
## Critérios Parada ##
episolon1 = 0.00000001
episolon2 = episolon1
kmax = 999999
## Aproximação Inicial ##
x_0 = 3.0000000000000000000000000000000000000000000000
## Função ##
def f(x):
    return(math.sin(x))
## Derivada da função ##
def df(x):
    return(math.cos(x))
## VARIAVEIS AUX. PARA O ALGORITMO ##
x_linha = 0
k = 1
x_pre = x_0
## ALGORITMO ##
if(math.sqrt((f(x_0))**2) < episolon1):
    x_linha = x_0
else:
    while(k < kmax):
        print(k)
        x_pos = x_pre - ((f(x_pre))/(df(x_pre)))
        if (math.sqrt((f(x_pos))**2) < episolon1) or math.sqrt((x_pos - x_pre)**2) < episolon2:
            x_linha = x_pos
            break
        else:
            x_linha = x_pos
            x_pre = x_pos
            k = k + 1
## MOSTRA RESULTADO ##
print(x_linha)
    