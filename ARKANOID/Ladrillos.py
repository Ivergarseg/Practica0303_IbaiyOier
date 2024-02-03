import pygame 
blanco = (255,255,255)
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


ladrillo = Ladrillo(5,25,5,15,blanco)
print(ladrillo)