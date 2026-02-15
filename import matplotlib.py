import matplotlib.pyplot as plt
import numpy as np

# Configuración de datos del sistema
# [x, y, masa (kg), etiqueta, color]
particulas = [
    [0, 2, 4, 'M1 (4kg)', 'gold'],        # Eje Y positivo
    [1, 0, 2, 'M2 (2kg)', 'limegreen'],   # Eje X positivo
    [0, -4, 5, 'M3 (5kg)', 'dodgerblue'], # Eje Y negativo
    [-3, 0, 8, 'M4 (8kg)', 'orchid']      # Eje X negativo
]

# Crear la figura y los ejes
fig, ax = plt.subplots(figsize=(8, 8))

# 1. Dibujar las barras (Ejes físicos)
# Barra vertical (de M3 a M1)
ax.plot([0, 0], [-4, 2], color='gray', linewidth=3, zorder=1, label='Barras sin masa')
# Barra horizontal (de M4 a M2)
ax.plot([-3, 1], [0, 0], color='gray', linewidth=3, zorder=1)

# 2. Dibujar las masas
for p in particulas:
    x, y, m, label, color = p
    # El tamaño (s) es proporcional a la masa para visualización (m * 100)
    ax.scatter(x, y, s=m*150, color=color, edgecolors='black', zorder=2, label=f'Masa {m}kg')
    
    # Añadir etiquetas de texto
    offset_y = 0.3 if y >= 0 else -0.6
    ax.text(x + 0.2, y + offset_y, 
            f'{label}\nPos: ({x},{y})', 
            fontsize=10, 
            ha='center', 
            weight='bold')

# 3. Configuración estética del gráfico
ax.axhline(0, color='black', linewidth=1, linestyle='--', alpha=0.3) # Eje X cartesiano
ax.axvline(0, color='black', linewidth=1, linestyle='--', alpha=0.3) # Eje Y cartesiano
ax.grid(True, linestyle=':', alpha=0.6)

# Límites del gráfico (con un poco de margen)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

# Títulos y etiquetas
ax.set_title('Sistema de 4 Partículas - Distribución de Masas', fontsize=14)
ax.set_xlabel('Posición X (m)')
ax.set_ylabel('Posición Y (m)')
ax.set_aspect('equal') # Importante para que no se distorsione la geometría

# Mostrar gráfico
plt.tight_layout()
plt.show()