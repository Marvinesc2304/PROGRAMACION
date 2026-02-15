

numero_secreto = 7

print("--- Adivina el número ---")
# CORRECCIÓN: Convertimos el input a entero (int)
intento = int(input("Ingresa un número del 1 al 10: "))

if intento == numero_secreto:
    print("¡Felicidades! Adivinaste el número.")
else:
    print("Incorrecto. Intenta de nuevo.")