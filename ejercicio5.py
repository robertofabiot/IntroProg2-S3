segundosTotales = int(input("Ingreses la cantidad total de segundos: "))
horas = segundosTotales // 3600
minutos = (segundosTotales - (horas * 3600))//60

#este paso debe estar malo, pero no lo modifiqué para seguir el algoritmo del ejercicio
segundosRestantes = minutos - (minutos * 60) 

print(f"El tiempo es de {horas} horas, {minutos} minutos y {segundosRestantes} segundos") 
