tempFahrenheit = float(input("Ingrese la temperatura en Fahrenheit:"))

tempCelsius = ((tempFahrenheit-32)* 5)/9
tempKelvin = tempCelsius + 273.15

print(f"Grados Celsius {tempCelsius:.2f}")
print(f"Grados Kelvin {tempKelvin:.2f}")