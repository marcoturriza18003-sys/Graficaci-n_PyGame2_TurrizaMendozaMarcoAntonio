import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Colisión con cambio de color y movimiento aleatorio")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)
VERDE = (0, 255, 0)
AZUL = (0, 0, 255)

# Rectángulo del jugador
jugador = pygame.Rect(100, 100, 60, 60)
color_jugador = AZUL

# Rectángulo objetivo (se moverá aleatoriamente)
objetivo = pygame.Rect(500, 300, 80, 80)
vel_x = random.choice([-4, 4])
vel_y = random.choice([-4, 4])

# Velocidad del jugador
velocidad_jugador = 5

# Bucle principal
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador con las flechas
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad_jugador
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad_jugador
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad_jugador

    # Movimiento aleatorio del objetivo (rebota en los bordes)
    objetivo.x += vel_x
    objetivo.y += vel_y

    if objetivo.left <= 0 or objetivo.right >= ANCHO:
        vel_x = -vel_x
    if objetivo.top <= 0 or objetivo.bottom >= ALTO:
        vel_y = -vel_y

    # Detectar colisión
    if jugador.colliderect(objetivo):
        color_jugador = VERDE
    else:
        color_jugador = AZUL

    # Dibujar en pantalla
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, color_jugador, jugador)
    pygame.draw.rect(ventana, ROJO, objetivo)
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
