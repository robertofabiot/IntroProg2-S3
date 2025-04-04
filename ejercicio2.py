#Calculo del área y perímetro de un rectángulo
base = float(input("Ingrese la base del rectángulo: "))
altura = float(input("Ingrese la altura del rectángulo: "))
area = base * altura
perimetro = 2*(base+altura)
print(f"Área del rectángulo{area:.2f}")
print(f"Perímetro del rectángulo{perimetro:.2f}")
