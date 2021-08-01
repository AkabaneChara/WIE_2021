def es_primo(num):
    for x in range(2, num):
        if num%x == 0:
            print("No es un número primo.")
            return False
    print("Es un número primo")
    return True

number = int(input("Ingrese El Número A Comprobar : "))
es_primo(number)