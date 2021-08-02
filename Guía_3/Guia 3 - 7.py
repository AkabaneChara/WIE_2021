

keys = input("Inserte Las Llaves Del Diccionario : ")
values = input("Inserte Los Valores Correspondientes A Cada Llave : ")

keys = keys[keys.find("[")+2:len(keys)-2].split("', '")
values = values[values.find("[")+2:len(values)-1].split(", ")
values = [int(x) for x in values]

dicc = dict(zip(keys,values))
print(dicc)