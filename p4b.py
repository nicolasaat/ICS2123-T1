import numpy as np
import math

from parameters import *
##################
###RECORDATORIO###
##################
#Probabilidad de evento = N° casos favorables / N° casos totales
#Valor Esperado = Suma de valores en cada caso / N° casos totales


def getTheoreticalValue():
    prob_c1 = lmbda[1]/(lmbda[1]+lmbda[2])
    prob_c2 = lmbda[2]/(lmbda[1]+lmbda[2])
    return (prob_c1**2)*(1 + 2*prob_c2 + 3*(prob_c2**2))

def getEmpiricalResults():
    counter = 0
    random_gen = np.random.default_rng(seed=SEED)

    for _ in range(N_SIMULATIONS):
        times_c1 = 0
        times_c2 = 0
        times_c1 += sum([random_gen.exponential(1/lmbda[1]) for _ in range(2)])
        times_c2 +=  sum([random_gen.exponential(1/lmbda[2]) for _ in range(3)])

        if times_c1 < times_c2:
            counter += 1

    empirical_value = counter/N_SIMULATIONS
    standard_error = math.sqrt(empirical_value*(1-empirical_value)/N_SIMULATIONS)

    return empirical_value, standard_error

valor_teorico = getTheoreticalValue()
valor_empirico, error_estandar = getEmpiricalResults()
diferencia_porcentual = 100*abs((valor_empirico-valor_teorico)/valor_teorico)

print(f"PREGUNTA 4.b\n")
print(f"I. Valor Teorico: {valor_teorico}")
print(f"II. Valor Empirico: {valor_empirico}")
print(f"III. Error Estandar Empirico: {error_estandar}")
print(f"IV. Diferencia Porcentual: {diferencia_porcentual}%")