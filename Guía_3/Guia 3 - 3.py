#Escriba un programa que elimine de una lista todos los elementos repetidos.
#El formato de las listas usado en este programa es encerrado por corchetes
#rectangulares y los elementos separados solo por una coma: [ab,c,de,f,gh,i]

list_1 = input("Ingrese La Lista Con Corchetes Rectangulares y Separados Por Comas : ")
list_1 = list_1[1:len(list_1)-1].split(",")

list_1 = list(set(list_1))

print(list_1)