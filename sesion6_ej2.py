import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Recoge los círculos")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Fuente para mostrar el contador
fuente = pygame.font.Font(None, 40)

# Rectángulo del jugador
jugador = pygame.Rect(400, 300, 60, 60)
velocidad = 6

# Círculo (objetivo)
radio = 20
circulo_x = random.randint(radio, ANCHO - radio)
circulo_y = random.randint(radio, ALTO - radio)

# Contador
puntos = 0

# Reloj
reloj = pygame.time.Clock()
corriendo = True

# Bucle principal
while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad

    # Limitar dentro de la ventana
    jugador.x = max(0, min(ANCHO - jugador.width, jugador.x))
    jugador.y = max(0, min(ALTO - jugador.height, jugador.y))

    # Detección de colisión (rectángulo vs círculo)
    distancia_x = abs(jugador.centerx - circulo_x)
    distancia_y = abs(jugador.centery - circulo_y)
    distancia = (distancia_x**2 + distancia_y**2) ** 0.5

    if distancia < radio + jugador.width // 2:
        puntos += 1
        circulo_x = random.randint(radio, ANCHO - radio)
        circulo_y = random.randint(radio, ALTO - radio)

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, AZUL, jugador)
    pygame.draw.circle(ventana, ROJO, (circulo_x, circulo_y), radio)

    # Mostrar contador
    texto = fuente.render(f"Puntos: {puntos}", True, NEGRO)
    ventana.blit(texto, (20, 20))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
