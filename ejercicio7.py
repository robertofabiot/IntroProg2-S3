#Cálculo del precio final de un producto con impuestos y descuentos
precioOriginal = float(input("Ingrese el precio original: "))

porcentajeDescuento = float(input("Ingrese el porcentaje de descuento: "))
descuentoAplicado = (precioOriginal * porcentajeDescuento) / 100
precioConDescuento = precioOriginal - descuentoAplicado

porcentajeIva = float(input("Ingrese el porcentaje de IVA: "))
ivaCalculado = (precioConDescuento * porcentajeIva) / 100
precioFinal = precioConDescuento + ivaCalculado

print(f"Precio original: {precioOriginal}\nDescuento aplicado: {descuentoAplicado}\nPrecio con descuento: {precioConDescuento}\nIVA calculado: {ivaCalculado}\nPrecio final: {precioFinal}")