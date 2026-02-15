# adivinanza.py

numero_secreto = 7

print("--- Adivina el número ---")
intento = input("Ingresa un número del 1 al 10: ")

print(f"DEBUG tipo de dato: {type(intento)}")
print(f"DEBUG valor recibido: [{intento}]")

if intento == numero_secreto:  
    print("¡Felicidades! Adivinaste el número.")
else:
    print("Incorrecto. Intenta de nuevo.")