#Represente mediante una expresión booleana en Python un O lógico exclusivo (xor). Este se
#caracteriza porque solo es verdad cuando solamente una de las dos proposiciones es
#verdadera.

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
