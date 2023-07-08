from  Estimacion import *
from PruebaHipotesis import *
from  Salario import *
from TasaDesempleo import * 

filename =  'ECH_2022.csv'
#Estadisitica Descriptiva

#Parte 1 a
tasaDesempleo = TasaDesempleo(filename)
print("Tasa de desempleo: ", tasaDesempleo)
print(" ")

#Parte 1 b
print("Tasas de desempleo por rango de edad")
print("La Tasa de Desempleo es: ", tasaDesempleo)
print("La Tasa de Desempleo para el rango de edad de 14 a 17 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 14, 17))
print("La Tasa de Desempleo para el rango de edad de 18 a 25 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 18, 25))
print("La Tasa de Desempleo para el rango de edad de 26 a 40 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 26, 40))
print("La Tasa de Desempleo para mayores a 40 años es: ", TasaDesempleo_RangoEdad('ECH_2022.csv', 41, 200))


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

#Parte 2 a - histograma
HistogramaSalario(filename)

#Parte 2 b - boxplot de toda la muesrta
BoxplotSalario(filename)

#Parte 2 c - calcular media, mediana y moda de salarios
mediana =  medianaSalarios(filename)
print("Mediana de salarios: ", mediana)
moda = modaSalarios(filename)
print("Moda de salarios: ", moda)
media = mediaSalarios(filename)
print("Media de salarios: ", media)

#Parte 2 d - calcular minimo, maximo y cuartiles de salario
minimo = minimoSalarios(filename)
print("El minimo de salarios: ", minimo)
maximo =  maximoSalarios(filename)
print("El maximo de salarios: ", maximo)

q1, q2, q3 = quartiles(filename)
print("Cuartil 25%:", q1)
print("Cuartil 50%:", q2)
print("Cuartil 75%:", q3)

#Parte 2 e - Boxplot de Genero y Zona geografica
BoxplotGenero(filename)
BoxplotZonaGeografica(filename)


#Estimacion
#Parte 1 - estimacion desempleo de total de poblacion
muestra = 46522  # Tamaño de la muestra
intervaloConfianza = IntervaloConfianza(tasaDesempleo,muestra)
print("La estimacion de Desempleo del total de la poblacion es:" , EstimacionDesempleoTotalPoblacion(tasaDesempleo))

#Parte1 - Intervalo de Confianza 95%
print("Intervalo de confianza (95%):", intervaloConfianza)

#Prueba de hipotesis
 
referencia = 7.0  # Tasa de desempleo de referencia en el 2021
desviacionEstandar = math.sqrt((tasaDesempleo * (1 - tasaDesempleo)) / muestra)  
salariosgenero = SalariosGeneroLista(filename)
salariosh = salariosgenero[0]
salariosm = salariosgenero[1]

pruebaUnaCola = PruebaUnaCola(tasaDesempleo,referencia,desviacionEstandar,muestra)
print("Prueba de una cola: ", pruebaUnaCola)
pruebaDosColas = PruebaDosColas(salariosh, salariosm)
print("Prueba de dos colas: ", pruebaDosColas)