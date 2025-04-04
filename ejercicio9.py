# Cálculo del tiempo total de una película con comerciales 
duracionPelicula = int(input("Ingrese la duración de la película en minutos: "))
comercialesPrevios = int(input("Ingrese la duración de los comerciales previos: "))
cantidadPausasComerciales = int(input("Ingrese cuántas pausas comerciales hay: "))
duracionPausaComecial = int(input("Ingrese la duración de cada pausa comercial: "))

totalPausasComerciales = cantidadPausasComerciales * duracionPausaComecial

duracionTotal = duracionPelicula + comercialesPrevios + totalPausasComerciales

#En la variable totalPausasComerciales no se pedía sumar los comerciales previos, pero los sumé acá
print(f"Duración original: {duracionPelicula}\nDuración comerciales totales: {totalPausasComerciales+comercialesPrevios}\nTiempo total de proyección: {duracionTotal}")