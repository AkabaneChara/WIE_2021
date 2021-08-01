#Realice un programa que pida números al usuario hasta que este ingrese “exit”. Posterior a
#esto imprima la suma de todos los números ingresados.

plus = 0

while (True):
    entry = input("Ingrese Un Número o exit Para Salir : ")

    if entry == 'exit':
        break
    else:
        plus += float(entry)

print(plus)
