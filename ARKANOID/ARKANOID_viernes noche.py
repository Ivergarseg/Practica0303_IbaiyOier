import pygame, sys
from COLORES import (NEGRO, VERDE, CIAN, AZUL)
from random import randint  
import random  
pygame.init()

# Paleta de colores
azul = (  0,  0,  255)
negro = (  0,  0,  0)
verde = (  0,  255,  0)
cian = (  0,  255,  255)
rojo = (  255,  0,  0)
magenta = (  255,  0,  255)
amarillo = (  255,  255,  0)
blanco = ( 255, 255, 255)

#defino el tamaño de la ventana y la inicio
tamaño_ventana = (800, 500)
ventana = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption("                                                                                        ARKANOID        OIER - IBAI")
tiempo = pygame.time.Clock()

### BOLA ###
#coordenadas de la bola
coor_b_x = 500
coor_b_y = 300
coord_bola = (coor_b_x,coor_b_y)
#velociadad bola
vel_b_x = randint(1,3)  #para que tengan tres posibles velocidades diferentes
vel_b_y = randint(1,3)
#coordenadas del bate           #                       
coor_r_x = 300                  #    (pto x respecto del margen izdo)   |---------------------------------------------------------------|
coor_r_l = 100                  #    (parámetro y, distancia hasta x)   |                                                               |                                                              
coor_r_h = 450                  #    (parámetro h, valor del eje y, respecto del origen de pantalla)   |                                                               |   
coor_r_ancho = 25               #    (altura del propio rectángulo)   |---------------------------------------------------------------|  
coord_rect = (coor_r_x,coor_r_h,coor_r_l, coor_r_ancho)
#velociadad bate
vel_r_x = 2
# Variable para rastrear si la bola está en contacto con el bate
bola_en_contacto_con_bate = False
#tipografia de derrota
fuente = pygame.font.Font(None, 36)



while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
    # Compruebo si se ha pulsado alguna tecla
    keys = pygame.key.get_pressed()
    if  0 < coor_r_x < 800:   
        if keys[pygame.K_LEFT] and coor_r_x > 3:
            coor_r_x -= vel_r_x
            print('<')
        if keys[pygame.K_RIGHT]and coor_r_x + coor_r_l <= 800 :
            coor_r_x += vel_r_x
            print('>')

    #declaro las cordenadas del bate y las de la bola y la pongo en moviento
    coord_rect = (coor_r_x, coor_r_h, coor_r_l, coor_r_ancho)
    coord_bola = (coor_b_x,coor_b_y)
    coor_b_x -= vel_b_x #con los signos aqui decidimos la 
    coor_b_y -= vel_b_y #direccion de la pelota al inicio

    #Choque entre la barra y la bola
    if (
        coor_b_y + 15 == coor_r_h + 3   #este tres es para que cuadren en el plano, si no salen puntos dispares
        and coor_r_x < coor_b_x < coor_r_x + coor_r_l
    ):
        bola_en_contacto_con_bate = True
        vel_b_y *= -1
        vel_b_x = random.choice([vel_b_x, -vel_b_x]) #con esto consigo que rebote aleatoriaamente en un sentido u en otro
    else:
        bola_en_contacto_con_bate = False


    #delimitacion pantalla-bola (teniendo en cuenta el diametro de la pelota)
    if coor_b_x < 15 or coor_b_x > 785:
        vel_b_x *= -1
    if coor_b_y < 15:
        vel_b_y *= -1
    if coor_b_y > 485:
        texto = fuente.render("Game Over", True, rojo)
        texto_rect = texto.get_rect()
        texto_x = 800 / 2 - texto_rect.width / 2
        texto_y = 500 / 2 - texto_rect.height / 2 - 30
        ventana.blit(texto, [texto_x, texto_y])
        texto1 = fuente.render(" Pulse cualquier tecla para reiniciar", True, rojo)
        texto_rect1 = texto1.get_rect()
        texto_x1 = 800 / 2 - texto_rect1.width / 2
        texto_y1 = 500 / 2 - texto_rect1.height / 2 + 30
        ventana.blit(texto1, [texto_x1, texto_y1])
        pygame.display.flip()
        # Esperar a que el jugador presione una tecla
        esperar_tecla = True
        while esperar_tecla:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        sys.exit()
                    if event.type == pygame.KEYDOWN: #aqui digo aue con cualquier tecla rinicas
                        esperar_tecla = False
        
        # Reiniciar la posición de la bola, cada vez en una psoicion diferente
        coor_b_x = randint(15,785)
        coor_b_y = 300
    
    
    #Color de fondo
    ventana.fill(blanco)

    #Zona de dibujo
    bola = pygame.draw.circle(ventana, AZUL,coord_bola, 15)
    bate = pygame.draw.rect(ventana, VERDE, coord_rect)


    #Actualizar pantalla
    pygame.display.flip()
    tiempo.tick(60)