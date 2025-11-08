import pygame
import random

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Mini Juego - Sesión 6")

# Colores
BLANCO = (255, 255, 255)
NEGRO = (0, 0, 0)
VERDE = (0, 255, 0)
ROJO = (255, 0, 0)
AMARILLO = (255, 255, 0)

# Fuente para el contador
fuente = pygame.font.Font(None, 40)

# Cargar sprite del jugador 
nave_img = pygame.image.load("nave.png") 
nave_img = pygame.transform.scale(nave_img, (60, 60))

# Sprite del jugador
jugador = pygame.Rect(400, 500, 60, 60)
velocidad = 7

# Lista de objetos (puntos a recoger)
puntos = []
for _ in range(5):
    x = random.randint(20, ANCHO - 20)
    y = random.randint(20, ALTO - 200)
    puntos.append(pygame.Rect(x, y, 20, 20))

# Lista de obstáculos
obstaculos = []
for _ in range(4):
    x = random.randint(50, ANCHO - 50)
    y = random.randint(50, ALTO // 2)
    velocidad_y = random.choice([3, 4, 5])
    obstaculos.append({"rect": pygame.Rect(x, y, 40, 40), "vel_y": velocidad_y})

# Contador de puntos
score = 0

# Reloj del juego
reloj = pygame.time.Clock()
corriendo = True

# Función para reiniciar el juego tras colisión
def reiniciar_juego():
    global score
    score = 0
    jugador.x, jugador.y = 400, 500
    for p in puntos:
        p.x = random.randint(20, ANCHO - 20)
        p.y = random.randint(20, ALTO - 200)

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

    # Limitar dentro de la pantalla
    jugador.x = max(0, min(ANCHO - jugador.width, jugador.x))
    jugador.y = max(0, min(ALTO - jugador.height, jugador.y))

    # Mover obstáculos verticalmente (rebotan)
    for obs in obstaculos:
        obs["rect"].y += obs["vel_y"]
        if obs["rect"].top <= 0 or obs["rect"].bottom >= ALTO:
            obs["vel_y"] = -obs["vel_y"]

    # Detección de colisión con puntos
    for p in puntos:
        if jugador.colliderect(p):
            score += 1
            p.x = random.randint(20, ANCHO - 20)
            p.y = random.randint(20, ALTO - 200)

    # Detección de colisión con obstáculos
    for obs in obstaculos:
        if jugador.colliderect(obs["rect"]):
            # Mostrar mensaje y reiniciar
            texto = fuente.render("💥 ¡Colisión! Reiniciando...", True, ROJO)
            ventana.blit(texto, (ANCHO//2 - 180, ALTO//2))
            pygame.display.flip()
            pygame.time.wait(1500)
            reiniciar_juego()
            break

    # Dibujar elementos
    ventana.fill(NEGRO)
    ventana.blit(nave_img, (jugador.x, jugador.y))  # Dibuja la nave

    # Dibujar puntos
    for p in puntos:
        pygame.draw.circle(ventana, AMARILLO, p.center, 10)

    # Dibujar obstáculos
    for obs in obstaculos:
        pygame.draw.rect(ventana, ROJO, obs["rect"])

    # Mostrar el contador de puntos
    texto_puntos = fuente.render(f"Puntos: {score}", True, VERDE)
    ventana.blit(texto_puntos, (20, 20))

    pygame.display.flip()
    reloj.tick(60)

pygame.quit()
