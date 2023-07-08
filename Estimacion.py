from TasaDesempleo import TasaDesempleo
import math


#-------------------------------------------------------------------------------------------------------------------------------------------------
# 2) Estimacion:
# 2.1 Estimar el desempleo del total de la población

def EstimacionDesempleoTotalPoblacion(tasaDesempleo):
    totalPoblacion = 1757161
    return totalPoblacion * tasaDesempleo

def IntervaloConfianza(tasaDesempleo,muestra):    
    # Cálculo del intervalo de confianza
    error_estandar = math.sqrt((tasaDesempleo * (1 - tasaDesempleo)) / muestra)
    z_value = 1.96  # Valor crítico para un nivel de confianza del 95%
    margen_error = z_value * error_estandar
    return (tasaDesempleo - margen_error, tasaDesempleo + margen_error)


