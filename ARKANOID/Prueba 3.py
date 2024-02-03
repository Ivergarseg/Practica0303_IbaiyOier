import pygame
import sys

# Inicializar Pygame
pygame.init()
tiempo = pygame.time.Clock()

# Definir colores
blanco = (255, 255, 255)
negro = (0, 0, 0)
rojo = (255, 0, 0)

# Configuración de la pantalla
ancho_ventana = 800
alto_ventana = 600
ventana = pygame.display.set_mode((ancho_ventana, alto_ventana))
pygame.display.set_caption("Arkanoid")

# Definir la paleta del jugador
paleta_ancho = 100
paleta_alto = 20
paleta_x = (ancho_ventana - paleta_ancho) // 2
paleta_y = alto_ventana - 50
paleta_velocidad = 10

# Definir la bola
bola_radio = 10
bola_x = ancho_ventana // 2
bola_y = alto_ventana // 2
bola_velocidad_x = 5
bola_velocidad_y = 5

# Bucle principal del juego
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Mover la paleta con las teclas izquierda y derecha
    teclas = pygame.key.get_pressed()
    if teclas[pygame.K_LEFT] and paleta_x > 0:
        paleta_x -= paleta_velocidad
    if teclas[pygame.K_RIGHT] and paleta_x < ancho_ventana - paleta_ancho:
        paleta_x += paleta_velocidad

    # Mover la bola
    bola_x += bola_velocidad_x
    bola_y += bola_velocidad_y

    # Rebotar la bola en los bordes de la
    if bola_x <= 0 or bola_x >= ancho_ventana:
        bola_velocidad_x = -bola_velocidad_x
    if bola_y <= 0 or bola_y >= alto_ventana:
        bola_velocidad_y = -bola_velocidad_y
    
    #Color de fondo
    ventana.fill(blanco)
    

    #Actualizar pantalla
    pygame.display.flip()
    tiempo.tick(60)