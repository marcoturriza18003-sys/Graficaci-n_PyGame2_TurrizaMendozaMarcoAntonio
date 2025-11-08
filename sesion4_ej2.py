import pygame

pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Círculo pulsante")

# Colores
BLANCO = (255, 255, 255)
ROJO = (255, 0, 0)

# Propiedades del círculo
x, y = ANCHO // 2, ALTO // 2
radio = 20
creciendo = True
velocidad_radio = 0.5  # velocidad de crecimiento/encogimiento

# Control del tiempo
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Cambiar el tamaño del círculo
    if creciendo:
        radio += velocidad_radio
        if radio >= 50:
            creciendo = False  # cambiar a modo encogimiento
    else:
        radio -= velocidad_radio
        if radio <= 20:
            creciendo = True  # cambiar a modo crecimiento

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.circle(ventana, ROJO, (x, y), int(radio))
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
