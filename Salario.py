import csv
import matplotlib.pyplot as plt
import seaborn as sns
import statistics
import numpy as np


def SalarioLista(filename):
    salarios = [] # Lista para almacenar los salarios
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            salario_str = row[8]  # Obtén la cadena del salario de la columna 8 (índice 8)
            salario_str = salario_str.replace(',', '.')  # Reemplaza la coma por un punto en la cadena
            salario = float(salario_str)  # Convierte la cadena modificada a float
   
            salarios.append(salario)
    return salarios


def HistogramaSalario(filename):
    
    salarios = SalarioLista(filename)
    particion = [0,25000,50000,75000,100000,125000,150000,175000,200000]
    plt.hist(salarios,bins=particion, edgecolor='black')
    plt.xlabel('Salario')
    plt.ylabel('Frecuencia')
    plt.title('Histograma de Salarios')
    plt.show()

def BoxplotSalario(filename):
    salarios = [] # Lista para almacenar los salarios

    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            salario_str = row[8]  # Obtén la cadena del salario de la columna 8 (índice 8)
            salario_str = salario_str.replace(',', '.')  # Reemplaza la coma por un punto en la cadena
            salario = float(salario_str)  # Convierte la cadena modificada a float
            if(row[7] == "0"):
                salarios.append(salario)

    salariosfiltrados = np.clip(salarios,0,500000)
    
    fig, ax = plt.subplots()
    ax.boxplot(salariosfiltrados, whis=350)
    plt.show()
    #plt.ylabel('Salarios')
    #plt.title('Histograma de Salarios')
    #plt.show()


def medianaSalarios(filename):
    salarios = SalarioLista(filename)

    mediana = statistics.median(salarios)
    return mediana

def modaSalarios(filename):
    salarios = SalarioLista(filename)

    moda = statistics.mode(salarios)
    return moda

def mediaSalarios(filename):
    salarios = SalarioLista(filename)

    media = statistics.mean(salarios)
    return media




def quartiles(filename):
    salarios = SalarioLista(filename)

    cuartil_25 = np.percentile(salarios, 25)
    cuartil_50 = np.percentile(salarios, 50)
    cuartil_75 = np.percentile(salarios, 75)

    return cuartil_25, cuartil_50, cuartil_75

# Ejemplo de uso

def maximoSalarios(filename):
    salarios = SalarioLista(filename)

    return max(salarios)

def minimoSalarios(filename):
    salarios = SalarioLista(filename)

    return min(salarios)

def SalariosGeneroLista(filename):
    MujeresSalarios = [] # Lista para almacenar los salarios
    HombresSalarios = []
    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            salario_str = row[8]  # Obtén la cadena del salario de la columna 8 (índice 8)
            salario_str = salario_str.replace(',', '.')  # Reemplaza la coma por un punto en la cadena
            salario = float(salario_str)  # Convierte la cadena modificada a float
            if(row[3] == "1"):
                HombresSalarios.append(salario)
            else :
                MujeresSalarios.append(salario)
    return [HombresSalarios, MujeresSalarios]

def SalariosZonaLista(filename):
    InteriorSalarios = [] # Lista para almacenar los salarios
    MdeoSalarios = []

    with open(filename,'r') as file:
        reader = csv.reader(file, delimiter=';')
        reader.__next__() # Salta la primera linea, que es la de los nombres de las columnas
        for row in reader:
            salario_str = row[8]  # Obtén la cadena del salario de la columna 8 (índice 8)
            salario_str = salario_str.replace(',', '.')  # Reemplaza la coma por un punto en la cadena
            salario = float(salario_str)  # Convierte la cadena modificada a float
            if(row[5] == "1"):
                MdeoSalarios.append(salario)
            else :
                InteriorSalarios.append(salario)
    return [MdeoSalarios, InteriorSalarios]


HistogramaSalario('ECH_2022.csv')
#boxplot genero
salarios = SalariosGeneroLista('ECH_2022.csv')
salariosh = salarios[0]
salariosm = salarios[1]

datos = {'Genero': ['Hombres'] * len(salariosh) + ['Mujeres'] * len(salariosm),
         'Salarios': salariosh + salariosm}
print(len(datos))
etiquetas = ['Hombres', 'Mujeres']

sns.boxplot(x='Genero', y='Salarios', data=datos)
plt.ylabel('Salarios')
plt.xlabel('Generos')
plt.title('Histograma de Salarios')
plt.show()


#boxplot genero
salarios = SalariosZonaLista('ECH_2022.csv')
salariosMdeo = salarios[0]
salariosInterior = salarios[1]

datos = {'Zona': ['Mdeo'] * len(salariosMdeo) + ['Interior'] * len(salariosInterior),
         'Salarios': salariosMdeo + salariosInterior}
print(len(datos))
etiquetas = ['Mdeo', 'Interior']

sns.boxplot(x='Zona', y='Salarios', data=datos)
plt.ylabel('Salarios')
plt.xlabel('Zonas')
plt.title('Histograma de Salarios')
plt.show()


BoxplotSalario('ECH_2022.csv')

print(minimoSalarios('ECH_2022.csv'))
print(maximoSalarios('ECH_2022.csv'))


q1, q2, q3 = quartiles('ECH_2022.csv')
print("Cuartil 25%:", q1)
print("Cuartil 50%:", q2)
print("Cuartil 75%:", q3)

print(medianaSalarios('ECH_2022.csv'))
print(modaSalarios('ECH_2022.csv'))
print(mediaSalarios('ECH_2022.csv'))