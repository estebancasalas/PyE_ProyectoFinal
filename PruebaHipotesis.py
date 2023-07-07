
import math
from TasaDesempleo import TasaDesempleo
from Salario import SalariosGeneroLista
import scipy.stats as stats


def PruebaUnaCola(tasa_desempleo, referencia, desviacion_estandar, tamaño_muestra):
    # Cálculo del valor de prueba (Z-score)
    z = (tasa_desempleo - referencia) / (desviacion_estandar / math.sqrt(tamaño_muestra))
    
    # Valor crítico para un nivel de significancia del 95%
    valor_critico = 1.645
    
    # Toma de decisión
    if z > valor_critico:
        return "Se rechaza la hipótesis nula. Hay evidencia para afirmar que la tasa de desempleo ha aumentado."
    else:
        return "No se rechaza la hipótesis nula. No hay suficiente evidencia para afirmar que la tasa de desempleo ha aumentado."


def prueba_dos_colas(salarios_hombres, salarios_mujeres):
    # Cálculo de estadísticas descriptivas
    media_hombres = sum(salarios_hombres) / len(salarios_hombres)
    media_mujeres = sum(salarios_mujeres) / len(salarios_mujeres)
    desviacion_hombres = stats.tstd(salarios_hombres)
    desviacion_mujeres = stats.tstd(salarios_mujeres)
    tamaño_muestra_hombres = len(salarios_hombres)
    tamaño_muestra_mujeres = len(salarios_mujeres)

    # Cálculo del valor de prueba (t-score)
    numerador = media_hombres - media_mujeres
    denominador = math.sqrt((desviacion_hombres ** 2 / tamaño_muestra_hombres) + (desviacion_mujeres ** 2 / tamaño_muestra_mujeres))
    t = numerador / denominador

    # Valor crítico para un nivel de significancia del 99% (dos colas)
    valor_critico = stats.t.ppf(0.995, tamaño_muestra_hombres + tamaño_muestra_mujeres - 2)

    # Toma de decisión
    if abs(t) > valor_critico:
        return "Se rechaza la hipótesis nula. Hay evidencia para afirmar que hay diferencias en el salario promedio entre géneros."
    else:
        return "No se rechaza la hipótesis nula. No hay suficiente evidencia para afirmar que hay diferencias en el salario promedio entre géneros."




muestra = 46522  # Tamaño de la muestra
tasaDesempleo = TasaDesempleo('ECH_2022.csv')
referencia = 7.5  # Tasa de desempleo de referencia en el 2021
desviacionEstandar = math.sqrt((tasaDesempleo * (1 - tasaDesempleo)) / muestra)  # Desviación estándar (valor hipotético)
salarios = SalariosGeneroLista('ECH_2022.csv')
salariosh = salarios[0]
salariosm = salarios[1]


#Prueba Hipotesis 3
print(PruebaUnaCola(tasaDesempleo,referencia,desviacionEstandar,muestra))
print(prueba_dos_colas(salariosh, salariosm))


