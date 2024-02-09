import pygame, sys
from COLORES import (NEGRO, VERDE, CIAN, AZUL)
from random import randint  
import random 
from Ladrillos import Ladrillo 
pygame.init()
ventana = pygame.display.set_mode((640,480))
pygame.display.set_caption("Ejemplo 4")

azul = (  0,  0,  255)
negro = (  0,  0,  0)
verde = (  0,  255,  0)
cian = (  0,  255,  255)
rojo = (  255,  0,  0)
magenta = (  255,  0,  255)
amarillo = (  255,  255,  0)
blanco = ( 255, 255, 255)

ball = pygame.image.load("ball.png")
ballrect = ball.get_rect()
speed = [randint(3,6),randint(3,6)]
ballrect.move_ip(0,0)

barra = pygame.image.load("barra.png")
barrarect = barra.get_rect()
barrarect.move_ip(240,450)

ladrillos = [Ladrillo(x * 80, 50, 60, 30, cian) for x in range(10)]


fuente = pygame.font.Font(None, 36)

jugando = True
while jugando:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            jugando = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        barrarect = barrarect.move(-3,0)
    if keys[pygame.K_RIGHT]:
        barrarect = barrarect.move(3,0)

    if barrarect.colliderect(ballrect):
        speed[1] = -speed[1]

    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > ventana.get_width():
        speed[0] = -speed[0]
    if ballrect.top < 0: 
        speed[1] = -speed[1]
    if ballrect.bottom > ventana.get_height():
        texto = fuente.render("Game Over", True, (125,125,125))
        texto_rect = texto.get_rect()
        texto_x = ventana.get_width() / 2 - texto_rect.width / 2
        texto_y = ventana.get_height() / 2 - texto_rect.height / 2
        ventana.blit(texto, [texto_x, texto_y])
    else:
        ventana.fill((252, 243, 207))
        ventana.blit(ball, ballrect)
        ventana.blit(barra, barrarect)

    for ladrillo in ladrillos:
        
        ladrillorect = ladrillo.draw(ventana)

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()

