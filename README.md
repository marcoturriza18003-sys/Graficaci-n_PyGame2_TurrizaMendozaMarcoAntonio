# Graficaci-n_PyGame2_TurrizaMendozaMarcoAntonio

MATERIA: GRAFICACIÓN
ALUMNO: TURRIZA MENDOZA MARCO ANTONIO

Sesión 4: Animación y control de tiempo
Objetivo: Crear animaciones fluidas y controlar el tiempo con pygame.time.Clock.
Ejercicios
1. Rebote con velocidad variable:
○ Modifica el código de la Sesión 4 para que el círculo acelere gradualmente
(incrementa velocidad_x en 0.1 cada vez que rebota).
○ Usa pygame.time.Clock para mantener 60 FPS.

2. Animación de pulsación (Intermedio):
○ Crea un círculo que crezca y se encoja (radio entre 20 y 50 píxeles)
simulando una pulsación.
○ Cambia la dirección del crecimiento cuando alcance los límites.

3. Simulación de gravedad (Avanzado):
○ Crea una animación donde un círculo caiga con gravedad (incrementa y con
una aceleración de 0.5 por frame) y rebote en el suelo con una pérdida de
energía (reduce la velocidad vertical en 20% por rebote).


Sesión 5: Imágenes y sprites
Objetivo: Trabajar con imágenes, sprites y transformaciones como rotación y escalado.
Ejercicios
1. Ajuste de tamaño dinámico (Básico):
○ Modifica el código de la Sesión 5 para que el usuario pueda aumentar o
disminuir el tamaño de la imagen con las teclas + y -.
○ Asegúrate de que la imagen no se distorsione (mantén proporciones si es
necesario).

2. Sprite animado (Intermedio):
○ Carga una hoja de sprites con al menos 4 frames (por ejemplo, un personaje
caminando). Muestra una animación cambiando entre frames cada 100 ms.
○ Usa una imagen de opengameart.org o crea una propia.

Mini-proyecto
● Tarea: Crea un programa donde una imagen (por ejemplo, una nave) rote hacia el
ratón o el joystick y se mueva hacia adelante al presionar una tecla o botón.
Asegúrate de que la imagen tenga un tamaño adecuado (usa
pygame.transform.scale). 


Sesión 6: Colisiones y aplicaciones prácticas
Objetivo: Implementar detección de colisiones y crear aplicaciones interactivas.
Ejercicios
1. Colisión con cambio de color (Básico):
○ Modifica el código de la Sesión 6 para que el rectángulo del jugador cambie
de color (por ejemplo, a verde) cuando colisione con el objetivo.

2. Recolección de objetos (Intermedio):
○ Crea un programa donde el jugador mueva un rectángulo para recoger
círculos que aparezcan en posiciones aleatorias (usa random.randint). Cada
vez que recoge uno, aparece otro.
○ Muestra un contador de objetos recogidos en la pantalla.

3. Evitar obstáculos (Avanzado):
○ Diseña un programa donde el jugador mueva un rectángulo para evitar
círculos móviles (por ejemplo, moviéndose horizontalmente). Si colisiona, el
juego termina o reinicia.

Mini-proyecto
● Tarea: Desarrolla un juego simple donde el jugador controle un sprite (por ejemplo,
una nave) con el teclado o un control, recoja objetos (puntos) y evite obstáculos.
Muestra un contador de puntos en la terminal o en la pantalla (usa pygame.font).




