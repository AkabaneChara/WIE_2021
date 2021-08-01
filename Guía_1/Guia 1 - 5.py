#Escriba un programa que pida al usuario dos números enteros e imprima “<número 1> entre
#<número 2> da un cociente <cociente> y un residuo <residuo>”

numerator = int(input("Ingrese El Primer Número : "))
denominator = int(input("Ingrese El Segundo Número : "))

print(numerator, "entre", denominator, "da un cociente", numerator//denominator, "y un residuo", numerator % denominator)
