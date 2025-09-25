import numpy as np
import math

from parameters import *
##################
###RECORDATORIO###
##################
#Probabilidad de evento = N° casos favorables / N° casos totales
#Valor Esperado = Suma de valores en cada caso / N° casos totales


def getTheoreticalValue():
    return 3/8

def getEmpiricalResults(rate=alpha):
    
    values = []
    random_gen = np.random.default_rng(seed=SEED)

    for _ in range(N_SIMULATIONS):
        time_elapsed = 0
        waiting_time = []
        while time_elapsed < 3/4:
            new_arrival_time = random_gen.exponential(1/rate)
            time_elapsed += new_arrival_time
            if time_elapsed < 3/4:
                time_left = 3/4 - time_elapsed
                waiting_time.append(time_left)
        average_waiting_time = sum(waiting_time)/len(waiting_time)
        values.append(average_waiting_time)

    empirical_value = sum(values)/N_SIMULATIONS
    standard_deviation = np.std(values, ddof=1)
    standard_error = standard_deviation/math.sqrt(N_SIMULATIONS)

    return empirical_value, standard_error

valor_teorico = getTheoreticalValue()
valor_empirico_1, error_estandar_1 = getEmpiricalResults()
valor_empirico_2, error_estandar_2 = getEmpiricalResults(rate=2*alpha)
diferencia_porcentual_1 = 100*abs((valor_empirico_1-valor_teorico)/valor_teorico)
diferencia_porcentual_2 = 100*abs((valor_empirico_2-valor_teorico)/valor_teorico)

print(f"PREGUNTA 4.c\n")
print(f"I. Valor Teorico: {valor_teorico}hrs ({valor_teorico*60}min)")
print(f"II.a Valor Empirico (~Exp(alpha)): {valor_empirico_1}")
print(f"II.b Valor Empirico (~Exp(2*alpha)): {valor_empirico_2}")
print(f"III. Error Estandar Empirico (~Exp(alpha)): {error_estandar_1}")
print(f"III. Error Estandar Empirico (~Exp(2*alpha)): {error_estandar_2}")
print(f"IV. Diferencia Porcentual (~Exp(alpha)): {diferencia_porcentual_1}%")
print(f"IV. Diferencia Porcentual (~Exp(2*alpha)): {diferencia_porcentual_2}%")