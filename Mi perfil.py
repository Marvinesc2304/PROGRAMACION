# mi_perfil.py - Generador de Tarjetas de Presentación
import os
import sys

# Constantes de configuración
ANCHO_TARJETA = 60
COLOR_BORDE = "\033[96m"  # Cyan
COLOR_TITULO = "\033[93;1m"  # Amarillo Intenso
COLOR_ETIQUETA = "\033[92m"  # Verde
COLOR_TEXTO = "\033[97m"  # Blanco
COLOR_INPUT = "\033[95m"  # Magenta
RESET = "\033[0m"

def limpiar_pantalla():
    """Limpia la consola según el sistema operativo."""
    os.system('cls' if os.name == 'nt' else 'clear')

def centrar_texto(texto, ancho, color=RESET):
    """Devuelve el texto centrado con el ancho dado."""
    # Calcular relleno sin contar los códigos de color
    len_visible = len(texto)
    espacios = (ancho - len_visible) // 2
    return " " * espacios + color + texto + RESET + " " * (ancho - len_visible - espacios)

def mostrar_titulo():
    """Muestra un encabezado estilizado."""
    limpiar_pantalla()
    print(f"\n{COLOR_BORDE}" + "═" * (ANCHO_TARJETA + 2) + f"{RESET}")
    print(centrar_texto(" PERFILES PRO  ", ANCHO_TARJETA + 2, COLOR_TITULO))
    print(f"{COLOR_BORDE}" + "═" * (ANCHO_TARJETA + 2) + f"{RESET}")

def validar_entrada(mensaje, es_edad=False):
    """Solicita input al usuario con validación básica."""
    while True:
        valor = input(f"{COLOR_INPUT}{mensaje}{RESET}").strip()
        if not valor:
            print(f"     {COLOR_TITULO}Este campo no puede estar vacío.{RESET}")
            continue
        
        if es_edad:
            if valor.isdigit() and 0 < int(valor) < 120:
                return valor
            print(f"    {COLOR_TITULO}Por favor ingresa una edad válida.{RESET}")
        else:
            return valor

def obtener_datos():
    """Recopila la información del usuario."""
    print(f"\n{COLOR_TEXTO} Por favor, completa tu perfil:{RESET}\n")
    
    nombre = validar_entrada(" ► ¿nombre completo? ")
    edad = validar_entrada(" ► ¿Edad? ", es_edad=True)
    ciudad = validar_entrada(" ► ¿Residencia actual? ")
    hobby = validar_entrada(" ► ¿Pasatiempo favorito? ")
    
    return nombre, edad, ciudad, hobby

def mostrar_tarjeta(nombre, edad, ciudad, hobby):
    """Imprime la tarjeta de presentación con diseño."""
    print("\n")
    # Borde superior
    print(f"{COLOR_BORDE}╔{'═' * ANCHO_TARJETA}╗{RESET}")
    
    # Espacio y Título
    print(f"{COLOR_BORDE}║{RESET}" + " " * ANCHO_TARJETA + f"{COLOR_BORDE}║{RESET}")
    titulo = "TARJETA DE PRESENTACIÓN"
    print(f"{COLOR_BORDE}║{RESET}" + centrar_texto(titulo, ANCHO_TARJETA, COLOR_TITULO) + f"{COLOR_BORDE}║{RESET}")
    print(f"{COLOR_BORDE}║{RESET}" + " " * ANCHO_TARJETA + f"{COLOR_BORDE}║{RESET}")
    
    # Separador
    print(f"{COLOR_BORDE}╠{'─' * ANCHO_TARJETA}╣{RESET}")
    
    # Contenido
    etiquetas = ["NOMBRE", "EDAD", "CIUDAD", "HOBBY"]
    valores = [nombre.upper(), f"{edad} años", ciudad.title(), hobby.title()]
    
    for etiqueta, valor in zip(etiquetas, valores):
        linea = f"   {COLOR_ETIQUETA}{etiqueta:<10}{RESET}: {COLOR_TEXTO}{valor}{RESET}"
        # Calcular padding considerando que los colores no ocupan espacio visual
        longitud_visible = 3 + 10 + 2 + len(valor) 
        padding = ANCHO_TARJETA - longitud_visible
        print(f"{COLOR_BORDE}║{RESET}{linea}{' ' * padding}{COLOR_BORDE}║{RESET}")

    # Cierre
    print(f"{COLOR_BORDE}║{RESET}" + " " * ANCHO_TARJETA + f"{COLOR_BORDE}║{RESET}")
    print(f"{COLOR_BORDE}╚{'═' * ANCHO_TARJETA}╝{RESET}")

def main():
    """Bucle principal de la aplicación."""
    # Habilitar colores en consola de Windows antigua si es necesario
    if os.name == 'nt':
        os.system('color')
        
    try:
        while True:
            mostrar_titulo()
            datos = obtener_datos()
            mostrar_tarjeta(*datos)
            
            print(f"\n{COLOR_BORDE}" + "─" * (ANCHO_TARJETA + 2) + f"{RESET}")
            opcion = input(f"{COLOR_INPUT}¿Crear otra tarjeta? (s/n): {RESET}").lower()
            
            if opcion not in ['s', 'si', 'sí', 'y', 'yes']:
                print(f"\n{COLOR_TITULO} ¡Gracias por usar el Generador Pro! Hasta luego. 👋{RESET}")
                break
                
    except KeyboardInterrupt:
        print(f"\n\n{COLOR_BORDE} Programa interrumpido por el usuario.{RESET}")

if __name__ == "__main__":
    main()