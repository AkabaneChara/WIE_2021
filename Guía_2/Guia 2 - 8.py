word = input("Ingrese La Palabra A Comparar : ")
word = word.lower()
comparation = word[::-1]

if word == comparation:
    print("La palabra es un palíndromo")
else:
    print("La palabra no es un palíndromo")