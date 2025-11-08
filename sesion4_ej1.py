import pygame
import random

pygame.init()

# Dimensiones de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Círculo que acelera y cambia de color al rebotar")

# Colores
BLANCO = (255, 255, 255)

# Propiedades del círculo
radio = 30
x, y = 400, 300
velocidad_x = 3
velocidad_y = 3
color_pelota = (0, 0, 0)  # Color inicial negro

# Reloj
reloj = pygame.time.Clock()

corriendo = True
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Mover el círculo
    x += velocidad_x
    y += velocidad_y

    # Detectar colisiones con los bordes
    rebote = False

    if x - radio <= 0 or x + radio >= ANCHO:
        velocidad_x = -velocidad_x
        rebote = True
        # Aumenta gradualmente la velocidad en X
        if velocidad_x > 0:
            velocidad_x += 0.1
        else:
            velocidad_x -= 0.1

    if y - radio <= 0 or y + radio >= ALTO:
        velocidad_y = -velocidad_y
        rebote = True
        # Aumenta gradualmente la velocidad en Y
        if velocidad_y > 0:
            velocidad_y += 0.1
        else:
            velocidad_y -= 0.1

    # Si rebotó, cambia de color
    if rebote:
        color_pelota = (
            random.randint(0, 255),
            random.randint(0, 255),
            random.randint(0, 255)
        )

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.circle(ventana, color_pelota, (int(x), int(y)), radio)
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()

