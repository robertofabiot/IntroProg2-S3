#Cálculo del salario neto de un empleado
salarioBruto = float(input("Ingrese el salario bruto: "))
impuestoRenta = salarioBruto * 0.1
seguroSocial = salarioBruto * 0.05
fondoPensiones = salarioBruto * 0.03
descuentos = impuestoRenta + seguroSocial + fondoPensiones
salarioNeto = salarioBruto - descuentos
print(f"El salario bruto es {salarioBruto}")
print(f"El total de descuentos es de {descuentos}")
print(f"El salario neto es de {salarioNeto}")
