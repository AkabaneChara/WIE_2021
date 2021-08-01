#En un rango del 1 – 10, imprima los números con el siguiente patrón.

for x in reversed(range(1, 11)):
    for y in reversed(range(1, x+1)):
        print(y, end=" ")
    print(end="\n")
