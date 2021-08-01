#Escriba un código en el que se pida una cantidad entera de horas, a partir de las cuales debe
#calcular el número de años, meses, semanas, días y horas que equivalen al número dado. Suponga
#que los meses tienen exactamente 30 días e ignore los años bisiestos.

hours = int(input("Ingrese El Número de Horas : "))

print("Años : ", hours//8760)
hours %= 8760
print("Meses : ", hours//720)
hours %= 720
print("Semanas : ", hours//168)
hours %= 168
print("Días : ", hours//24)
hours %= 24
print("Horas : ", hours)
