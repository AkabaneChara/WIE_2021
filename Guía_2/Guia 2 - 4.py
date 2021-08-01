plus = 0

while (True):
    entry = input("Ingrese Un Número o exit Para Salir : ")

    if entry == 'exit':
        break
    else:
        plus += float(entry)

print(plus)