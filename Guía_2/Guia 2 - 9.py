# Comprobación de Correo
def comprobation_mail(mail):
    if mail[0] == '.' or mail[-1] == '.':
        return False
    elif mail.count('.') == 0:
        return False
    elif mail.count('@') != 1:
        return False
    else:
        return True

# Comprobación de Contraseña
def comprobation_password(password):
    if len(password) < 8:
        return False
    elif len([x for x in password if x.isupper()]) == 0:
        return False
    elif len([x for x in password if x.islower()]) == 0:
        return False
    elif len([x for x in password if x.isdigit()]) == 0:
        return False
    else:
        return True

mail = input("Ingrese Su Correo : ")
password = input("Ingrese Su Contraseña : ")

if comprobation_mail(mail):
    print("Correo Valido")
else:
    print("Correo Invalido")

if comprobation_password(password):
    print("Contraseña Valida")
else:
    print("Contraseña Invalida")