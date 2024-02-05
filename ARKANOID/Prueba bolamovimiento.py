import pygame, sys
pygame.init()
blanco = ( 255, 255, 255)
azul = (  0,  0,  255)


#defino el tamaño de la ventana y la inicio
tamaño_ventana = (800, 500)
ventana = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption(" ARKANOID        PRUEBA")
tiempo = pygame.time.Clock()

### BOLA ###
#coordenadas de la bola
coor_b_x = 400
coor_b_y = 300
coord_bola = (coor_b_x,coor_b_y)
#velociadad bola
vel_b_x = 2
vel_b_y = 2
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    coord_bola = (coor_b_x,coor_b_y)
    coor_b_x += vel_b_x
    coor_b_y += vel_b_y

    #delimitacion pantalla-bola (teniendo en cuenta el diametro de la pelota)
    if coor_b_x < 15 or coor_b_x > 785:
        vel_b_x *= -1
    if coor_b_y < 15 or coor_b_y > 485:
        vel_b_y *= -1

    #Color de fondo
    ventana.fill(blanco)

    #Zona de dibujo
    bola = pygame.draw.circle(ventana, azul,coord_bola, 15)

    #Actualizar pantalla
    pygame.display.flip()
    tiempo.tick(60)