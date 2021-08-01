def comprobation(proposition):
    if proposition == 'F' or proposition == 'V':
        return True
    else:
        return False

P = input("Ingrese El Valor De P : ")
Q = input("Ingrese El Valor De Q : ")

if comprobation(P) and comprobation(Q):
    if P != Q:
        print("P XOR Q : V")
    else:
        print("P XOR Q : F")
else:
    print("Valor De Verdad Incorrecto")