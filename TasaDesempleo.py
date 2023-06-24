import csv

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 1. Calcular Poblacion Economicamente Activa

def PEA(filename):
    counter = 0
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            if (int(row[4]) > 13) and (int(row[6]) == 1):
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
            if (int(row[4]) > 13) and (int(row[7]) == 1):
                counter += 1
    return counter

#-------------------------------------------------------------------------------------------------------------------------------------------------

# 3. Calcular Tasa de Desempleo
def TasaDesempleo(filename):
    return (PersonasDesempleadas(filename) / PEA(filename))
print(TasaDesempleo('ECH_2022.csv'))
