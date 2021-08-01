#Escriba un programa que reciba una temperatura con el siguiente formato: 34F
#Donde primero se encuentra número de grados y luego el posfijo que indica la escala que se
#maneja, puede ser F: Fahrenheit, C: Celsius o K: kelvin.
#Posterior a eso el programa debe esperar una de las tres iniciales (C, K, F) que indique en
#qué escala espera la salida. Por último, realice la conversión de temperaturas desde la
#cantidad dada hasta la escala esperada.

entry = input("Ingrese La Temperatura A Cambiar : ")
change = input("Ingrese La Escala de Cambio : ")

scale = entry[-1]
temperature = int(entry[0:len(entry)-1])

if scale == 'K':
    if change == 'C':
        new_temperature = temperature - 273.15
    elif change == 'F':
        new_temperature = (temperature-273.15)*(9/5)+32
    else:
        print("Codigo de Temperatura Incorrecto")
elif scale == 'C':
    if change == 'K':
        new_temperature = temperature+273.15
    elif change == 'F':
        new_temperature = (temperature*(9/5))+32
    else:
        print("Codigo de Temperatura Incorrecto")
elif scale == 'F':
    if change == 'C':
        new_temperature = (temperature-32)*(5/9)
    elif change == 'K':
        new_temperature = (temperature-32)*(5/9)+273.15
    else:
        print("Codigo de Temperatura Incorrecto")
else:
    print("Codigo de Temperatura Incorrecto")

if 'new_temperature' in globals():
    print("La nueva temperatura es", round(new_temperature,3), change)
