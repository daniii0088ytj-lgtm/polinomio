 # Solicitar al usuario la cantidad de datos a analizar
 n= int(input("eCuántos datos deseas ingresar? "))
 Leer los datos
datos=[]
contador = 0 
while contador <n:
valor - float(input(f"Ingrese el valor (contador + 1): "))
datos.append(valor)
contador += 1
Analisis con ciclo while
indice-0
SUma
maximo- datos[0]
 minimo = datos[0]
positivos=0
negativos= 0
ceros= 0
1l1 while indice <n:
valor = datos[indice]
suma += valor
if valor > maximo:
maximo valor
if valor < minimo:
minimo - valor
if valor> 0:
positivos += 1
elif valor < 0:
negativos += 1
else:
    ceros += 1
indice
 # Resultados
promedio = suma /n

if valor > 0:
positivos += 1
elif valor <0:
negativos += 1
else:
ceros + 1
indice += 1
 Resultados
promedio suma/n
Li print("InResultados del anālisis:")
Li0 print("Datos ingresados:", datos)
ll print("Suma:", suma)
 print("Promedio:", promedio)
print("Valor máximo:", maximo)
 print("valor minimo:", minimo)
print("Cantidad de positivos:", positivos)
print("Cantidad de negativos:", negativos)
print("Cantidad de ceros:", ceros)