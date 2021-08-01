#Diseñe y pruebe un algoritmo que identifique si una cadena de texto es un palíndromo o no.
#Entiéndase por palíndromo que se lee al derecho que al revés.

word = input("Ingrese La Palabra A Comparar : ")
word = word.lower()
comparation = word[::-1]

if word == comparation:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")
