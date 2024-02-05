import pygame,sys
# Paleta de colores
azul = (  0,  0,  255)
negro = (  0,  0,  0)
verde = (  0,  255,  0)
cian = (  0,  255,  255)
rojo = (  255,  0,  0)
magenta = (  255,  0,  255)
amarillo = (  255,  255,  0)
blanco = ( 255, 255, 255)

lista_colores = (azul, negro, verde, cian, rojo, magenta, amarillo, blanco)
class Ladrillo:
    def __init__(self,dist_x,dist_l,dist_y,dist_h,color):
#                                                                           (0,0)
  #                                                                         (x,y)                          (l)
# dist_x   (EJE X, pto x respecto del del origen de pantalla)                |---------------------------------------------------------------|
# dist_l  (EJE X, largo del ladrillo)                                        |                                                               |                                                              
# dst_y  (EJE Y , valor del eje y, respecto del origen de pantalla)       (h)|                                                               |   
# dist_h  (EJE Y , altura del propio rectángulo)                             |---------------------------------------------------------------|
# color (color del ladrillo)  
        
        self.dist_x = dist_x
        self.dist_l = dist_l
        self.dist_y = dist_y
        self.dist_h = dist_h
        self.color = color

    def draw(self,ventana):
        pygame.draw.rect(ventana, self.color, (self.dist_x, self.dist_y, self.dist_l, self.dist_h))
    


ladrillo = Ladrillo(5,30,5,15,blanco)
    


