import csv
import math
import matplotlib.pyplot as plt

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Calcular Poblacion Economicamente Activa

def PEA(filename):
    counter = 0
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            if (int(row[4]) > 13) and (int(row[6]) == 1):   # row[4] es la columna de Edad, y row[6] es la columna de Poblacion Economicamente Activa
                counter += 1
    return counter

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 2. Calcular Poblacion Desocupada
def PersonasDesempleadas(filename):
    counter = 0
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            if (int(row[4]) > 13) and (int(row[7]) == 1):   # row[4] es la columna de Edad, y row[7] es la columna de Poblacion Desocupada
                counter += 1
    return counter

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Calcular Tasa de Desempleo
def TasaDesempleo(filename):
    return (PersonasDesempleadas(filename) / PEA(filename))



#-------------------------------------------------------------------------------------------------------------------------------------------------

# 4. Calcular Tasa de Desempleo por rangos de Edad.
#    Primero desarrollaremos las funciones anteriores, pero teniendo en cuenta el rango de edad.

def PEA_RangoEdad(filename, minEdad, maxEdad):
    counter = 0
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            if (int(row[4]) >= minEdad) and (int(row[4]) <= maxEdad) and (int(row[6]) == 1):  # row[4] es la columna de Edad, y row[6] es la columna de Poblacion Economicamente Activa
                counter += 1
    return counter

def PersonasDesempleadas_RangoEdad(filename, minEdad, maxEdad):
    counter = 0
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            if (int(row[4]) >= minEdad) and (int(row[4]) <= maxEdad) and (int(row[7]) == 1):  # row[4] es la columna de Edad, y row[7] es la columna de Poblacion Desocupada
                counter += 1
    return counter

def TasaDesempleo_RangoEdad(filename, minEdad, maxEdad):
    return (PersonasDesempleadas_RangoEdad(filename, minEdad, maxEdad) / PEA_RangoEdad(filename, minEdad, maxEdad))

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



#-------------------------------------------------------------------------------------------------------------------------------------------------
# Parte principal del programa.

muestra = 46522  # Tamaño de la muestra
tasaDesempleo = TasaDesempleo('ECH_2022.csv')
intervaloConfianza = IntervaloConfianza(tasaDesempleo,muestra)
tasaDesempleo2022 = 7.0  # Tasa de desempleo observada en el 2022
referencia = 7.5  # Tasa de desempleo de referencia en el 2021
desviacionEstandar = math.sqrt((tasaDesempleo * (1 - tasaDesempleo)) / muestra)  # Desviación estándar (valor hipotético)

print("La Tasa de Desempleo es: ", tasaDesempleo)
print("La Tasa de Desempleo para el rango de edad de 14 a 17 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 14, 17))
print("La Tasa de Desempleo para el rango de edad de 18 a 25 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 18, 25))
print("La Tasa de Desempleo para el rango de edad de 26 a 40 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 26, 40))
print("La Tasa de Desempleo para mayores a 40 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 41, 200))
#Estimacion:2.1
print("La estimacion de Desempleo del total de la poblacion es:" , EstimacionDesempleoTotalPoblacion(tasaDesempleo))
#Estimacion:2.2
print("Intervalo de confianza (95%):", intervaloConfianza)
#Prueba Hipotesis 3
print(PruebaUnaCola(tasaDesempleo,referencia,desviacionEstandar,muestra))

tdRango1 = TasaDesempleo_RangoEdad('ECH_2022.csv', 14, 17)  # tdRango1 = Tasa de Desempleo para el rango de edad de 14 a 17 años
tdRango2 = TasaDesempleo_RangoEdad('ECH_2022.csv', 18, 25)  # tdRango2 = Tasa de Desempleo para el rango de edad de 18 a 25 años
tdRango3 = TasaDesempleo_RangoEdad('ECH_2022.csv', 26, 40)  # tdRango3 = Tasa de Desempleo para el rango de edad de 26 a 40 años
tdRango4 = TasaDesempleo_RangoEdad('ECH_2022.csv', 41, 200) # tdRango4 = Tasa de Desempleo para mayores a 40 años

# Graficar
plt.plot(["14-17","18-25","26-40","40+"],[tdRango1,tdRango2,tdRango3,tdRango4])
plt.xlabel("Rango de Edad")
plt.ylabel("Tasa de Desempleo")
plt.title("Tasa de Desempleo por Rango de Edad")
plt.show()