#Escriba un programa que concatene dos listas de strings de la siguiente manera.

list_1 = input("Ingrese La Primer Lista : ")
list_2 = input("Ingrese La Segunda Lista : ")

list_1 = list_1[list_1.find("[")+2:len(list_1)-2].split('", "')
list_2 = list_2[list_2.find("[")+2:len(list_2)-2].split('", "')
new_list = []

for x in range(len(list_1)):
    new_list.append(str(list_1[x]) + str(list_2[x]))

print(new_list)