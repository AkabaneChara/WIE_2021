#Dada una tupla de tuplas de la forma: tuple1 = (('a', 23),('b', 37),('c', 11),('d', 29)),
#Imprima la misma en orden ascendente de acuerdo al segundo valor de cada tupla. Entonces,
#la salida esperada sería.

string = input("Ingrese La Tupla A Invertir : ")
string = string[string.find("(")+2:len(string)-3].split("),(")

for x in range(len(string)):
    string[x] = string[x].split(", ")

list_tuples = []

for x in range(len(string)):
    aux_0 = string[x][0][1:len(string[x][0])-1]
    aux_1 = int(string[x][1])
    aux = (aux_0, aux_1)
    list_tuples.append(tuple(aux))

list_tuples.sort(key = lambda x: x[1])
print(list_tuples)