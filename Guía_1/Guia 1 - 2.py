#Una compañía necesita un programa que permita calcular el valor equivalente en euros y dólares
#estadunidenses de una cantidad dada en pesos colombianos.

COP = int(input("Ingrese La Cantidad de Dinero En COP : "))

print("Valor En Euros : ", round(COP*0.000218,2), "€")
print("Valor En Dolares Americanos : ", round(COP*0.000259,2), "$")
