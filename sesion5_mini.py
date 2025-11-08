import pygame
import math

# Inicializar Pygame
pygame.init()
ventana = pygame.display.set_mode((800, 600))
pygame.display.set_caption("Nave que rota y se mueve hacia el ratón")

# Colores
blanco = (255, 255, 255)

# Cargar imagen de la nave
nave_original = pygame.image.load("nave.png").convert_alpha()

# Escalar la imagen a un tamaño adecuado (por ejemplo 80x80)
nave_original = pygame.transform.scale(nave_original, (250, 250))

# Posición inicial de la nave
x, y = 400, 300
velocidad = 5

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Obtener posición del ratón
    mouse_x, mouse_y = pygame.mouse.get_pos()

    # Calcular ángulo entre la nave y el puntero del ratón
    dx = mouse_x - x
    dy = mouse_y - y
    angulo = math.degrees(math.atan2(-dy, dx))  # Pygame rota en sentido contrario al reloj

    # Rotar la imagen de la nave
    nave_rotada = pygame.transform.rotate(nave_original, angulo)
    nave_rect = nave_rotada.get_rect(center=(x, y))

    # Movimiento hacia adelante con tecla W
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_w]:
        x += math.cos(math.radians(angulo)) * velocidad
        y -= math.sin(math.radians(angulo)) * velocidad

    # Dibujar en pantalla
    ventana.fill(blanco)
    ventana.blit(nave_rotada, nave_rect)
    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
