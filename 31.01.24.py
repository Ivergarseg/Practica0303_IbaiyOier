import pygame 

#PARÁMETROS 
largo_pantalla = 500
alto_pantalla = 400

#COLORES   
rojo = (255, 0, 0),    # Rojo
verde = (0, 255, 0),    # Verde
azul = (0, 0, 255),    # Azul
amarillo = (255, 255, 0),  # Amarillo
magenta = (255, 0, 255),  # Magenta
cian = (0, 255, 255),  # Cian
naranja = (255, 128, 0),  # Naranja
morado = (128, 0, 255),  # Morado
azul_claro = (0, 128, 255),  # Azul claro
verde_claro = (128, 255, 0)   # Verde claro
lavanda_suave = (220, 180, 220),  # Lavanda suave

#FIGURAS
bola = 
pygame.init()           #inicio la libreria pygame
pant = pygame.display.set_mode((largo_pantalla,alto_pantalla))          #declaro pant como mi pantalla y le doy medidas
play = True

while play:         #bucle principal del juego
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        
        
    pant.fill(lavanda_suave)         #rellenar pantalla(color)
    pygame.display.flip()           #actualizo la pantalla 
    
