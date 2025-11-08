import pygame

pygame.init()

# Configuración de la ventana
ANCHO, ALTO = 800, 600
ventana = pygame.display.set_mode((ANCHO, ALTO))
pygame.display.set_caption("Círculo con gravedad y rebotes")

# Colores
BLANCO = (255, 255, 255)
AZUL = (0, 0, 255)

# Propiedades del círculo
radio = 30
x = ANCHO // 2
y = 100  # posición inicial
velocidad_y = 0
gravedad = 0.5  # aceleración por frame
factor_rebote = -0.8  # rebote con pérdida del 20%

# Control del tiempo
reloj = pygame.time.Clock()
corriendo = True

while corriendo:
    for evento in pygame.event.get():
        if evento.type == pygame.QUIT:
            corriendo = False

    # Aplicar gravedad
    velocidad_y += gravedad
    y += velocidad_y

    # Detectar colisión con el "suelo"
    if y + radio >= ALTO:
        y = ALTO - radio  # mantener sobre el suelo
        velocidad_y *= factor_rebote  # invertir dirección y reducir energía

        # Si la velocidad es muy pequeña, detener el movimiento
        if abs(velocidad_y) < 0.5:
            velocidad_y = 0

    # Dibujar
    ventana.fill(BLANCO)
    pygame.draw.circle(ventana, AZUL, (x, int(y)), radio)
    pygame.display.flip()

    reloj.tick(60)

pygame.quit()
