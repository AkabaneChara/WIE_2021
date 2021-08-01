#Realice un programa que reciba 3 valores enteros correspondientes a los tres las longitudes
#de los lados de un triángulo. A continuación, imprima si el triángulo es equilátero, isósceles
#o escaleno.

side_1 = input("Ingrese El Primer Lado Del Triangulo : ")
side_2 = input("Ingrese El Segundo Lado Del Triangulo : ")
side_3 = input("Ingrese El Tercer Lado Del Triangulo : ")

if side_1 != side_2 != side_3:
    print("El triangulo es escaleno")
elif side_1 == side_2 == side_3:
    print("El triangulo es equilatero")
else:
    print("El triangulo es isósceles")
