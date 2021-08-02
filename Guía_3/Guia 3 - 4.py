#Realice un programa donde se definan dos matrices bidimensionales a modo de lista de listas,
#como se muestra a continuación.

def set_matrix(matrix):
    aux = input()
    aux = aux[aux.find("[")+2:len(aux)-1].split(", ")
    aux = [int(x) for x in aux]
    matrix.append(aux)
    aux = input()
    aux = aux[aux.find("[")+1:len(aux)-1].split(", ")
    aux = [int(x) for x in aux]
    matrix.append(aux)
    aux = input()
    aux = aux[aux.find("[")+1:len(aux)-2].split(", ")
    aux = [int(x) for x in aux]
    matrix.append(aux)

matrix_1 = []
matrix_2 = []
matrix_3 = [[0,0,0],[0,0,0],[0,0,0]]

print("Ingrese La Primer Matriz : ")
set_matrix(matrix_1)
print("Ingrese La Segunda Matriz : ")
set_matrix(matrix_2)

for c in range(3):
    for i in range(3):
        aux = 0
        for j in range(3):
            aux += matrix_1[i][j]*matrix_2[j][c]
        matrix_3[i][c] = aux

print("A*B =", end=" ")
for x in range(3):
    print(matrix_3[x])
    print("     ", end=" ")