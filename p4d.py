import numpy as np
import math
import random as rd

from parameters import *
##################
###RECORDATORIO###
##################
#Probabilidad de evento = N° casos favorables / N° casos totales
#Valor Esperado = Suma de valores en cada caso / N° casos totales


def getTheoreticalValue():
    alpha_m = alpha/60
    sumatory = 0
    lmbda_a = alpha_m*p
    lmbda_b = alpha_m*(1-p)
    for k in range(0, math.floor(M/r)+1):
        probability_Sb = ((lmbda_b**k)*beta)/((lmbda_b+beta)**(k+1))
        if r*k>M:
            probability_Sa = 0
        else:
            prob_S1_j = []
            for j in range(0, M+1):
                sum_lower_a = sum((lmbda_a * a)**m / math.factorial(m) for m in range(j+1))
                sum_lower_b = sum((lmbda_a * b)**m / math.factorial(m) for m in range(j+1))
                prob_j = (sum_lower_a * math.exp(-lmbda_a * a) - sum_lower_b * math.exp(-lmbda_a * b)) / ((b - a) * lmbda_a)
                prob_S1_j.append(prob_j)

            probability_Sa = sum(prob_S1_j[r*k:])

        sumatory += probability_Sb*probability_Sa

    return sumatory

def getEmpiricalResults():
    counter = 0
    random_gen = np.random.default_rng(seed=SEED)

    for _ in range(N_SIMULATIONS):
        aboard_1 = 0
        aboard_2 = 0

        alpha_m = alpha/60

        timelimit_1 = random_gen.uniform(a, b)
        timelimit_2 = random_gen.exponential(1/beta)

        time_elapsed = 0

        while time_elapsed < max(timelimit_1, timelimit_2):
            new_arrival_time = random_gen.exponential(1/alpha_m)
            time_elapsed += new_arrival_time
            random_number = random_gen.random()
            if random_number <= p and aboard_1 < M and time_elapsed < timelimit_1:
                aboard_1 += 1
            elif random_number > p and aboard_2 < M and time_elapsed < timelimit_2:
                aboard_2 += 1
            
        if aboard_1 >= r*aboard_2:
            counter += 1

    empirical_value = counter/N_SIMULATIONS
    standard_error = math.sqrt(empirical_value*(1-empirical_value)/N_SIMULATIONS)

    return empirical_value, standard_error

valor_teorico = getTheoreticalValue()
valor_empirico, error_estandar = getEmpiricalResults()
diferencia_porcentual = 100*abs((valor_empirico-valor_teorico)/valor_teorico)

print(f"PREGUNTA 4.d\n")
print(f"I. Valor Teorico: {valor_teorico}")
print(f"II. Valor Empirico: {valor_empirico}")
print(f"III. Error Estandar Empirico: {error_estandar}")
print(f"IV. Diferencia Porcentual: {diferencia_porcentual}%")