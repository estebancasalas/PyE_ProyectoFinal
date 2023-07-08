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
# Parte principal del programa.
