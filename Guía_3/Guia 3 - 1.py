#Realice un programa que imprima al revés una lista dada

entry = input("Ingrese La Lista A Invertir : ")
entry = entry[1:len(entry)-1].split(sep=',')
entry = [int(x) for x in entry]
entry = entry[::-1]
print(entry)