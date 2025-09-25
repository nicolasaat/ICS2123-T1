import numpy as np
import math

from parameters import *
##################
###RECORDATORIO###
##################
#Probabilidad de evento = N° casos favorables / N° casos totales
#Valor Esperado = Suma de valores en cada caso / N° casos totales


def getTheoreticalValue():
    return 1/sum(lmbda.values())

def getEmpiricalResults():
    values = []
    random_gen = np.random.default_rng(seed=SEED)

    for _ in range(N_SIMULATIONS):
        arrivals = [random_gen.exponential(1/lmbda[i]) for i in range(1, N_BOATS+1)]
        first_boat = min(arrivals)

        values.append(first_boat)
    empirical_value = sum(values)/N_SIMULATIONS
    standard_deviation = np.std(values, ddof=1)
    standard_error = standard_deviation/math.sqrt(N_SIMULATIONS)

    return empirical_value, standard_error

valor_teorico = getTheoreticalValue()
valor_empirico, error_estandar = getEmpiricalResults()
diferencia_porcentual = 100*abs((valor_empirico-valor_teorico)/valor_teorico)

print(f"PREGUNTA 4.a\n")
print(f"I. Valor Teorico: {valor_teorico}")
print(f"II. Valor Empirico: {valor_empirico}")
print(f"III. Error Estandar Empirico: {error_estandar}")
print(f"IV. Diferencia Porcentual: {diferencia_porcentual}%")