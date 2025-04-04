primerTramo = float(input("Ingrese la duración del primer tramo del vuelo (en minutos): "))
primeraEscala = float(input("Ingrese la duración de la primera escala (en minutos): "))
segundoTramo = float(input("Ingrese la duración del segundo tramo del vuelo (en minutos): "))
segundaEscala = float(input("Ingrese la duración de la segunda escala (en minutos): "))
tercerTramo = float(input("Ingrese la duración del tercer tramo del vuelo (en minutos): "))
tiempoTotal = primerTramo + primeraEscala + segundoTramo + segundaEscala + tercerTramo
print(f"El tiempo total de viaje es igual a {tiempoTotal}")