import pygame

# Inicializar Pygame
pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Animación con hoja de sprites")
BLANCO = (255, 255, 255)

# Cargar hoja de sprites
sprite_sheet = pygame.image.load("sprite.png").convert_alpha()

# Datos de la hoja de sprites
num_frames = 4  # cantidad de frames
frame_ancho = sprite_sheet.get_width() // num_frames
frame_alto = sprite_sheet.get_height()

# Extraer cada frame en una lista
frames = []
for i in range(num_frames):
    frame = sprite_sheet.subsurface((i * frame_ancho, 0, frame_ancho, frame_alto))
    frames.append(frame)

# Variables para animación
frame_actual = 0
tiempo_cambio = 100  # milisegundos por frame
ultimo_cambio = pygame.time.get_ticks()

# Posición donde se dibujará el personaje
x, y = ANCHO // 2, ALTO // 2

# Bucle principal
corriendo = True
reloj = pygame.time.Clock()

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Tiempo actual
    tiempo_actual = pygame.time.get_ticks()

    # Cambiar de frame cada 100 ms
    if tiempo_actual - ultimo_cambio >= tiempo_cambio:
        frame_actual = (frame_actual + 1) % num_frames
        ultimo_cambio = tiempo_actual

    # Dibujar frame actual
    ventana.fill(BLANCO)
    frame_img = frames[frame_actual]
    ventana.blit(frame_img, (x - frame_ancho // 2, y - frame_alto // 2))
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
