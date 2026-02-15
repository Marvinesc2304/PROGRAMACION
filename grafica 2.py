import matplotlib.pyplot as plt
import numpy as np

# Datos del sistema
particulas = [
    [0, 2, 4, 'M1', 'gold'],
    [1, 0, 2, 'M2', 'limegreen'],
    [0, -4, 5, 'M3', 'dodgerblue'],
    [-3, 0, 8, 'M4', 'orchid']
]

fig, ax = plt.subplots(figsize=(8, 8))

# 1. Ejes cartesianos base (gris claro)
ax.axhline(0, color='gray', linewidth=1, linestyle='--')
ax.axvline(0, color='gray', linewidth=1, linestyle='--')

# 2. Dibujar el NUEVO eje de rotación a 45 grados (Rojo destacado)
# Línea y=x desde -5 hasta 5
x_vals = np.linspace(-5, 5, 100)
ax.plot(x_vals, x_vals, color='red', linewidth=2.5, label='Nuevo Eje de Rotación (45°)')

# Añadir indicador de ángulo
theta = np.linspace(0, np.pi/4, 50)
r = 1.5
x_arc = r * np.cos(theta)
y_arc = r * np.sin(theta)
ax.plot(x_arc, y_arc, 'r-', linewidth=1)
ax.text(1.7, 0.7, '45°', color='red', fontsize=12, fontweight='bold')


# 3. Dibujar el sistema de partículas
# Barras que conectan las masas
ax.plot([0, 0], [-4, 2], color='black', linewidth=2, zorder=1, alpha=0.6)
ax.plot([-3, 1], [0, 0], color='black', linewidth=2, zorder=1, alpha=0.6)

# Masas
for p in particulas:
    x, y, m, label, color = p
    # Calcular distancia visual al nuevo eje para efecto de análisis
    # Distancia punto a recta y=x es |x-y|/sqrt(2)
    dist = abs(x - y) / np.sqrt(2)
    
    # Dibujar masa
    ax.scatter(x, y, s=m*150, color=color, edgecolors='black', zorder=2)
    
    # Etiquetas
    offset_y = 0.4 if y >= 0 else -0.7
    ax.text(x, y + offset_y, 
            f'{label}\n{m}kg', 
            fontsize=10, ha='center', weight='bold')
    
    # Opcional: líneas punteadas desde las masas al nuevo eje
    # El punto proyectado en y=x es ((x+y)/2, (x+y)/2)
    proj = (x + y) / 2
    ax.plot([x, proj], [y, proj], 'r:', alpha=0.3, linewidth=1)

# Configuración final
ax.grid(True, linestyle=':', alpha=0.6)
ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_title('Rotación del Sistema sobre Eje de 45°\n(Inercia resultante: 85 kg·m²)', fontsize=14)
ax.set_xlabel('Posición X (m)')
ax.set_ylabel('Posición Y (m)')
ax.legend()

plt.tight_layout()
plt.show()