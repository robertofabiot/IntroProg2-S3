# Cálculo del volumen de un cilindro y su área superficial

radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

areaBase = (3.1416*(radio**2))
volumen = areaBase * altura

areaLateral = (2*3.1416*radio*altura)
areaSuperficial = areaLateral + 2 * areaBase

print(f"Radio: {radio}\nAltura: {altura}\nVolumen: {volumen:.2f}\nÁrea superficial: {areaSuperficial:.2f}") 