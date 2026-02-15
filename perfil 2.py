
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
