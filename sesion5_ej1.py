import pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Imagen con control de tamaño (+ / -)")

# Colores
BLANCO = (255, 255, 255)

# Cargar imagen 
imagen = pygame.image.load("imagen.png").convert_alpha()

# Escala inicial
escala = 1.0
ancho_original, alto_original = imagen.get_size()

# Posición (centro)
x, y = ANCHO // 2, ALTO // 2

# Reloj
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Detectar teclas presionadas
    teclas = pygame.key.get_pressed()

    # Aumentar escala con "+" (principal o numpad)
    if teclas[pygame.K_EQUALS] or teclas[pygame.K_PLUS] or teclas[pygame.K_KP_PLUS]:
        escala += 0.01

    # Disminuir escala con "-" (principal o numpad)
    if teclas[pygame.K_MINUS] or teclas[pygame.K_KP_MINUS]:
        escala -= 0.01

    # Limitar la escala entre 0.1x y 2.0x
    escala = max(0.1, min(2.0, escala))

    # Redimensionar imagen manteniendo proporciones
    ancho_img = int(ancho_original * escala)
    alto_img = int(alto_original * escala)
    imagen_escalada = pygame.transform.smoothscale(imagen, (ancho_img, alto_img))

    # Calcular posición centrada
    pos_x = x - ancho_img // 2
    pos_y = y - alto_img // 2

    # Dibujar
    ventana.fill(BLANCO)
    ventana.blit(imagen_escalada, (pos_x, pos_y))
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
