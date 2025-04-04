#Cálculo del índice de masa corporal (IMC) 
pesoKg = float(input("Ingrese el peso en Kg: "))
alturaM = float(input("Ingrese la altura en metros: "))
IMC = pesoKg/(alturaM*alturaM)
IMC = (IMC * 100)/100 #Me parecería mejor otra forma de redondeo más clara y confiable

print(f"El peso ingresado es de {pesoKg} kilos, la altura ingresada fue de {alturaM} metros. El IMC calculado es de {IMC}")
print("Su clasificiación según el estándar es:")

if IMC < 18.5:
    print("Bajo peso")
elif IMC >= 18.5 and IMC <= 24.9:
    print("Peso normal")
elif IMC >= 25 and IMC <= 29.9:
    print("Pre-obesidad o Sobrepeso")
elif IMC >= 30 and IMC <= 34.9:
    print("Obesidad clase I")
elif IMC >= 35 and IMC <= 39.9:
    print("Obesidad clase II")
elif IMC > 40:
    print("Obesidad clase III")
