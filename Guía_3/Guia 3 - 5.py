#Dada una tupla de n elementos, realice un programa que reverse la tupla e imprima la versión
#original y la versión al revés. El formato de la tupla es de la siguiente forma:
#tuple1 = (('a', 23),(37),('c'),('d', 29)),

string = input("Ingrese La Tupla A Invertir : ")
string = string[string.find("(")+2:len(string)-3].split("),(")

normal_tuple = tuple(string)
inverted_tuple = normal_tuple[::-1]

print("Tupla Original : ", normal_tuple)
print("Tupla Invertida : ", inverted_tuple)