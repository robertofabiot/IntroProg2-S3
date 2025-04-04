#Conversión de una cantidad en dólares a distintas monedas
dolares = float(input("Ingrese la cantidad de dólares: "))

print("¿Desea definir la tasa de cambio o usar las tasas sugeridas?")
print("[1]Definirlas")
print("[2]Usar las tasas sugeridas")
opcion = int(input())

if opcion == 1:
    dolaresEuros = float(input("Defina la tasa de cambio de dólares a euros: "))
    dolaresLibras = float(input("Defina la tasa de cambio de dólares a libras: ")) 
    dolaresYenes = float(input("Defina la tasa de cambio de dólares a yenes: "))
elif opcion == 2:
    dolaresEuros = 0.90498
    dolaresLibras = 0.76321
    dolaresYenes = 146.07500
else:
    print("Opción no válida")
    exit()
# No sabía si con "definir" se refería a pedírselas a el usuario o almacenarlas
# como variable directamente, hice las dos

euros = dolares * dolaresEuros
libras = dolares * dolaresLibras
yenes = dolares * dolaresYenes

print(f"En dólares: {dolares}\nEn euros: {euros:.2f}\nEn libras: {libras:.2f}\nEn yenes: {yenes:.2f}")