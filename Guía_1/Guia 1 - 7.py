#En una granja se crían gallinas y conejos si se encuentran las cabezas son 50 si se cuentan las
#patas son 134 ¿cuántos animales hay de cada uno? Escriba un programa que resuelva el problema
#anterior.

# C+R=50 y 4R+2C=134

rabbits = int((134-100)/2)
chickens = int(50-rabbits)

print("Hay un total de", chickens, "gallinas y", rabbits, "conejos.")
print("Así teniendo un total de 50 cabezas y 134 patas.")
