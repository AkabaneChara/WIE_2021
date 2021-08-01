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