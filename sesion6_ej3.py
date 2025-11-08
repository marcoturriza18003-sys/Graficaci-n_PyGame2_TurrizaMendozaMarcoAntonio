import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Evita los círculos")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)
ROJO = (255, 0, 0)
NEGRO = (0, 0, 0)

# Jugador (rectángulo)
jugador = pygame.Rect(400, 500, 60, 60)
velocidad_jugador = 6

# Círculos enemigos
num_circulos = 5
circulos = []
for _ in range(num_circulos):
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, ALTO // 2)
    velocidad_x = random.choice([-5, 5])
    circulos.append({"x": x, "y": y, "radio": 25, "vel_x": velocidad_x})

# Fuente
fuente = pygame.font.Font(None, 50)

# Reloj
reloj = pygame.time.Clock()
corriendo = True

def reiniciar_juego():
    """Reinicia posiciones del jugador y enemigos."""
    jugador.x, jugador.y = 400, 500
    for c in circulos:
        c["x"] = random.randint(50, ANCHO - 50)
        c["y"] = random.randint(50, ALTO // 2)
        c["vel_x"] = random.choice([-5, 5])

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Movimiento del jugador
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT]:
        jugador.x -= velocidad_jugador
    if teclas[pygame.K_RIGHT]:
        jugador.x += velocidad_jugador
    if teclas[pygame.K_UP]:
        jugador.y -= velocidad_jugador
    if teclas[pygame.K_DOWN]:
        jugador.y += velocidad_jugador

    # Limitar dentro de la ventana
    jugador.x = max(0, min(ANCHO - jugador.width, jugador.x))
    jugador.y = max(0, min(ALTO - jugador.height, jugador.y))

    # Mover los círculos
    for c in circulos:
        c["x"] += c["vel_x"]
        if c["x"] - c["radio"] <= 0 or c["x"] + c["radio"] >= ANCHO:
            c["vel_x"] = -c["vel_x"]

    # Verificar colisiones
    for c in circulos:
        distancia_x = abs(jugador.centerx - c["x"])
        distancia_y = abs(jugador.centery - c["y"])
        distancia = (distancia_x**2 + distancia_y**2) ** 0.5
        if distancia < c["radio"] + jugador.width / 2:
            # Mostrar mensaje y reiniciar
            texto = fuente.render("¡Colisión! Reiniciando...", True, ROJO)
            ventana.blit(texto, (ANCHO // 2 - 200, ALTO // 2))
            pygame.display.flip()
            pygame.time.wait(1500)
            reiniciar_juego()
            break

    # Dibujar todo
    ventana.fill(BLANCO)
    pygame.draw.rect(ventana, AZUL, jugador)
    for c in circulos:
        pygame.draw.circle(ventana, ROJO, (int(c["x"]), int(c["y"])), c["radio"])

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
