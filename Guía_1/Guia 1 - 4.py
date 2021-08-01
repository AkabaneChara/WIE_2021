#Escriba un programa que pida al usuario su edad actual y un año entre 2022 y 2070. Calcule la
#edad del usuario en el año dado e imprima “su edad en el año <año dado> será <años calculados>
#años”.

age = int(input("Ingrese Su Edad : "))
year = int(input("Ingrese Un Año Entre 2022 y 2070 : "))

if (year<=2070 and year>=2022):
    print("Su edad en el año", year, "será", (year-2021)+age, "años")
else:
    print("Año Fuera Del Rango")
