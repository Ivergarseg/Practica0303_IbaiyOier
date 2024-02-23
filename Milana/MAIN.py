import pygame, sys
import random

#__________  _____   .____     ___________________________              
#\______   \/  _  \  |   |    \_   _____/\__    ___/  _  \             
# |    |   /  /_\  \ |   |      |    __)_   |    |   /_\  \     \           
# |    |__/    |    \|   |___  _|        \  |    |    |    \
# |____|  \____|__  /_______ \/________  /  |____|\___|__  /           
#                 \/        \/         \/                 \/            
#  ________  ___________                                               
#  \______ \ \_   _____/                                               
#   |    |  \ |    __)_                                                
#   |    `   \|        \                                               
#  /_______  /_______  /                                               
#          \/        \/                                                
#_________  ________  .____    ________ _____________________ _________
#\_   ___ \ \_____  \ |    |   \_____  \\______   \_   _____//   _____/
#/    \  \/  /   |   \|    |    /   |   \|       _/|    __)_ \_____  \ 
#\     \____/    |    \    |___/    |    \    |   \|        \/        \
# \______  /\_______  /_______ \_______  /____|_  /_______  /_______  /
#        \/         \/        \/       \/       \/        \/        \/ 
rojo = (255, 0, 0)
rojo_claro = (255, 128, 128)
rojo_medio = (255, 64, 64)
rojo_oscuro = (128, 0, 0)
rojo_muy_oscuro = (64, 0, 0)

verde = (0, 255, 0)
verde_claro = (128, 255, 128)
verde_medio = (64, 255, 64)
verde_oscuro = (0, 128, 0)
verde_muy_oscuro = (0, 64, 0)

azul = (0, 0, 255)
azul_claro = (128, 128, 255)
azul_medio = (64, 64, 255)
azul_oscuro = (0, 0, 128)
azul_muy_oscuro = (0, 0, 64)

amarillo = (255, 255, 0)
amarillo_claro = (255, 255, 128)
amarillo_medio = (255, 255, 64)
amarillo_oscuro = (128, 128, 0)
amarillo_muy_oscuro = (64, 64, 0)

magenta = (255, 0, 255)
magenta_claro = (255, 128, 255)
magenta_medio = (255, 64, 255)
magenta_oscuro = (128, 0, 128)
magenta_muy_oscuro = (64, 0, 64)

cian = (0, 255, 255)
cian_claro = (128, 255, 255)
cian_medio = (64, 255, 255)
cian_oscuro = (0, 128, 128)
cian_muy_oscuro = (0, 64, 64)

marrón = (128, 64, 0)
marrón_claro = (192, 128, 0)
marrón_medio = (160, 96, 0)
marrón_oscuro = (64, 32, 0)
marrón_muy_oscuro = (32, 16, 0)

naranja = (255, 165, 0)
naranja_claro = (255, 192, 128)
naranja_medio = (255, 176, 64)
naranja_oscuro = (128, 82, 0)
naranja_muy_oscuro = (64, 41, 0)

rosa = (255, 192, 203)
rosa_claro = (255, 218, 225)
rosa_medio = (255, 205, 210)
rosa_oscuro = (255, 182, 193)
rosa_muy_oscuro = (255, 160, 177)

violeta = (148, 0, 211)
violeta_claro = (186, 85, 211)
violeta_medio = (164, 66, 211)
violeta_oscuro = (128, 0, 128)
violeta_muy_oscuro = (85, 0, 85)

blanco = (255, 255, 255)
gris_claro = (192, 192, 192)
gris_medio = (128, 128, 128)
gris_oscuro = (64, 64, 64)
negro = (0, 0, 0)


# ________                .__                             .__                    .___               __               
#\______ \   ____   ____ |  | _____ ____________    ____ |__| ____   ____     __| _/____     _____/  |_  ______     
# |    |  \_/ __ \_/ ___\|  | \__  \\_  __ \__  \ _/ ___\|  |/  _ \ /    \   / __ |/ __ \  _/ ___\   __\/  ___/     
# |    `   \  ___/\  \___|  |__/ __ \|  | \// __ \\  \___|  (  <_> )   |  \ / /_/ \  ___/  \  \___|  |  \___ \      
#/_______  /\___  >\___  >____(____  /__|  (____  /\___  >__|\____/|___|  / \____ |\___  >  \___  >__| /____  > /\  
#       \/     \/     \/          \/           \/     \/               \/       \/    \/       \/          \/  \/ 



# Definir constantes para el tamaño de la pantalla
ancho_ven = 550
alto_ven = 650

#defino el tamaño de la ventana y la creo
tamaño_ventana = (ancho_ven, alto_ven)
ventana = pygame.display.set_mode(tamaño_ventana)
pygame.display.set_caption("                                                                   ARKANOID        OIER - IBAI")
tiempo = pygame.time.Clock()

# Definir constantes para la velocidad de la bola
min_velocidad = 5
max_velocidad = 10

# Definir constantes para el tamaño del mensaje de enhorabuena
ancho_mensaje = 200
alto_mensaje = 100
# Definir constantes para el tamaño de las serpentinas
ancho_serpentina = 10
alto_serpentina = 20
# Variable para rastrear el número de vidas
vidas = 3
# Definir constantes para el tamaño de los corazones
ancho_corazon = 30
alto_corazon = 30

# Definir constantes para la posición de los corazones
x_corazon = ancho_ven - 40
y_corazon = 10

class Bola:
    def __init__(self, x, y, radio, color, vx, vy):
        self.x = x
        self.y = y
        self.radio = radio
        self.color = color
        self.vx = vx
        self.vy = vy

    def dibujar(self, pantalla):
        pygame.draw.circle(pantalla, self.color, (self.x, self.y), self.radio)

    def actualizar(self): #Actualizo la posición de la bola
        self.x += self.vx
        self.y += self.vy
        #Con estos if hago rebotar a la bola en los bordes de la pantalla
        if self.x + self.radio >= ancho_ven or self.x - self.radio <= 0:
            self.vx *= -1
        if self.y + self.radio >= alto_ven:
            # Si la bola sale de la pantalla por la parte inferior, devuelvo True
            return True
        if self.y - self.radio <= 0:
            self.vy *= -1

class Bate:
    def __init__(self, x, y, ancho, alto, color):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color = color

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color, pygame.Rect(self.x, self.y, self.ancho, self.alto))

    def colision(self, bola):
        if bola.x >= self.x and bola.x <= self.x + self.ancho:
            if bola.y + bola.radio >= self.y and bola.y + bola.radio <= self.y + self.alto:
                bola.vy *= -1
                bola.vx = random.uniform(-1, 1) * 5  # Genera un número aleatorio entre -1 y 1, y lo multiplica por 5
                bola.vy = -random.randint(min_velocidad, max_velocidad)  # Establece la velocidad vertical a -5
                bola.y -= 5  # Mueve la bola hacia arriba 5 píxeles para evitar que se quede atascada
                return True
        return False
    
    def mover(self, direccion):
        if direccion == "izquierda":
            self.x -= 5
            if self.x < 0:
                self.x = 0
        elif direccion == "derecha":
            self.x += 5
            if self.x + self.ancho > ancho_ven:
                self.x = ancho_ven - self.ancho

class Ladrillo:
    def __init__(self, x, y, ancho, alto, color_actual, color_golpeado):
        self.x = x
        self.y = y
        self.ancho = ancho
        self.alto = alto
        self.color_actual = color_actual
        self.color_golpeado = color_golpeado

    def dibujar(self, pantalla):
        pygame.draw.rect(pantalla, self.color_actual, pygame.Rect(self.x, self.y, self.ancho, self.alto))

    def colision(self, bola):
        if (bola.x + bola.radio >= self.x and bola.x - bola.radio <= self.x + self.ancho and
            bola.y + bola.radio >= self.y and bola.y - bola.radio <= self.y + self.alto):
            if self.color_actual == blanco:
                self.color_actual = verde_medio
                self.color_golpeado = verde_medio
            elif self.color_actual == verde_medio:
                self.color_actual = rojo
                self.color_golpeado = rojo
            elif self.color_actual == rojo:
                if self.color_golpeado == blanco:
                    self.color_golpeado = verde_medio
                elif self.color_golpeado == verde_medio:
                    self.color_golpeado = rojo
                else:
                    ladrillos.remove(self)  # Eliminar el ladrillo de la lista ladrillos
            bola.vy *= -1
            return True
class ladrillo_indestructible(Ladrillo):
    def __init__(self, x, y, ancho, alto, color_actual, color_golpeado):
         self.x = x
         self.y = y
         self.ancho = ancho
         self.alto = alto
         self.color_actual = color_actual
         self.color_golpeado = color_golpeado
    def colision(self, bola):
         if (bola.x + bola.radio >= self.x and bola.x - bola.radio <= self.x + self.ancho and
            bola.y + bola.radio >= self.y and bola.y - bola.radio <= self.y + self.alto):
            if self.color_actual == blanco:
                self.color_actual = verde_medio
                self.color_golpeado = verde_medio
            elif self.color_actual == verde_medio:
                self.color_actual = rojo
                self.color_golpeado = rosa
            elif self.color_actual == rojo:
                self.color_actual == rosa
            bola.vy *= -1
    
        
        
        
    
#INICIO EL PROGRAMA
pygame.init()

#Creo la bola
# Obtengo una velocidad aleatoria para la pelota
velocidad_x = random.randint(min_velocidad, max_velocidad)
velocidad_y = random.randint(min_velocidad, max_velocidad)
bola = Bola(ancho_ven // 2, alto_ven // 2, 10, magenta, velocidad_x, -velocidad_y)
# Crear un rectángulo de rebote
bate = Bate(ancho_ven // 2 - 50, alto_ven - 35, 100, 20, azul)

#Defino el número de ladrillos que habra en la pantalla
num_lad_ancho = 10
num_lad_alto = 9
# Defino las constantes para el tamaño de los ladrillos
ancho_lad = 55
alto_lad = 20
# Creo una lista para los ladrillos
ladrillos = []
ladrillo_indestruc=[]

# Matriz 10x9 de colores
matriz_colores = [
    [verde_medio, rojo, rojo, rojo, blanco, rojo, rojo, rojo, verde_medio],
    [rojo, verde_medio, rojo, rojo, blanco, rojo, rojo, verde_medio, rojo],
    [rojo, rojo, verde_medio, rojo, blanco, rojo, verde_medio, rojo, rojo],
    [rojo, rojo, rojo, verde_medio, blanco, verde_medio, rojo, rojo, rojo],
    [blanco, blanco, blanco, blanco, blanco, blanco, blanco, blanco, blanco],
    [rojo, rojo, rojo, verde_medio, blanco, verde_medio, rojo, rojo, rojo],
    [rojo, rojo, verde_medio, rojo, blanco, rojo, verde_medio, rojo, rojo, rojo],
    [rojo, verde_medio, rojo, rojo, blanco, rojo, rojo, verde_medio, rojo, rojo],
    [verde_medio, rojo, rojo, rojo, blanco, rojo, rojo, rojo, verde_medio, rojo]
]
indestruc = ladrillo_indestructible(247,150,ancho_lad,alto_lad,blanco,verde)
ladrillo_indestruc.append(indestruc)

# Bucle para crear los ladrillos
for fila in range(9):
    for columna in range(9):
            if ((columna != 4) or (fila != 4)): 
                # Coordenadas del ladrillo
                x = columna * (ancho_lad + 5)
                y = fila * (alto_lad + 5)
                # Color del ladrillo
                
                color_ladrillo = matriz_colores[fila][columna]
                # Crear el ladrillo y añadirlo a la lista
                ladrillo = Ladrillo(x + 7.5, y + 50, ancho_lad, alto_lad, color_ladrillo, color_ladrillo)
                ladrillos.append(ladrillo)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
    
     # Actualizar la posición de la bola y verificar si la bola sale por abajo
    fin_juego = bola.actualizar()

    # Verificar si la bola colisiona con el rectángulo de rebote
    bate.colision(bola)

    # Mover el rectángulo de rebote si se presionan las teclas de flecha
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT]:
        bate.mover("izquierda")
    if keys[pygame.K_RIGHT]:
        bate.mover("derecha")

    # Verificar si la bola colisiona con algún ladrillo y eliminarlo si es necesario
    for ladrillo in ladrillos:
        if ladrillo.colision(bola):
            if ladrillo.color_actual == amarillo and ladrillo.color_golpeado is None:
                ladrillos.remove(ladrillo)
            break
    
    for indestruc in ladrillo_indestruc:
        if indestruc.colision(bola):
            if indestruc.color_actual == amarillo and indestruc.color_golpeado is amarillo:
                indestruc.color_actual = cian
            break
    
    

    
    if not ladrillos:
        # Mostrar mensaje de enhorabuena
        fuente_mensaje = pygame.font.Font(None, 36)
        mensaje = fuente_mensaje.render("¡Enhorabuena!", True, verde_medio)
        ventana.blit(mensaje, (ancho_ven // 2 - ancho_mensaje // 2, alto_ven // 2 - alto_mensaje // 2))

        # Dibujar serpentinas
        for i in range(30):
            x = random.randint(0, ancho_ven)
            y = random.randint(0, alto_ven)
            color_serpentina = random.choice([rojo, verde, azul, amarillo, magenta, cian, naranja, naranja_claro, rosa, violeta,rojo_claro, magenta_claro, azul_claro, rosa_claro,])
            pygame.draw.rect(ventana, color_serpentina, pygame.Rect(x, y, ancho_serpentina, alto_serpentina))

        pygame.display.flip()

        # Esperar a que se pulse cualquier tecla antes de cerrar la ventana
        esperar_tecla = True
        while esperar_tecla:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    esperar_tecla = False
        
    #Actualizar pantalla
    # Dibujar la bola
    
    ventana.fill(negro)
    # Crear una lista de corazones
    corazones = [pygame.Rect(x_corazon - 100 + i * (ancho_corazon + 5),
                          y_corazon, ancho_corazon, alto_corazon) for i in range(vidas)]
    # Dibujar los corazones
    for corazon in corazones:
        pygame.draw.polygon(ventana, rojo, [(corazon.x + ancho_corazon // 2, corazon.y),
                                             (corazon.x, corazon.y + alto_corazon // 2),
                                             (corazon.x + ancho_corazon // 2, corazon.y + alto_corazon),
                                             (corazon.x + ancho_corazon, corazon.y + alto_corazon // 2)])
    # Verificar si no quedan ladrillos
    bola.dibujar(ventana)
    bate.dibujar(ventana)
    
    indestruc.dibujar(ventana)
    
    for ladrillo in ladrillos:
        ladrillo.dibujar(ventana)
    for indestruc in ladrillo_indestruc: 
        indestruc.dibujar(ventana)
    
    
    pygame.display.flip()
    tiempo.tick(60)

    # Si la bola sale de la pantalla por la parte inferior, restar una vida y reiniciar la posición de la bola y el bate
    if fin_juego and vidas > 0:
        vidas -= 1
        velocidad_x = random.randint(min_velocidad, max_velocidad)
        velocidad_y = random.randint(min_velocidad, max_velocidad)
        bola = Bola(ancho_ven // 2, alto_ven // 2, 10, magenta_claro, velocidad_x, -velocidad_y)
        bate = Bate(ancho_ven // 2 - 50, alto_ven - 35, 100, 20, azul)
    
    
    # Si se pierden todas las vidas, mostrar "Game Over" y esperar a que el jugador presione una tecla para reiniciar
    if vidas == 0:
        fuente = pygame.font.Font(None, 36)
        texto = fuente.render("Game Over", True, rojo_medio)
        texto_rect = texto.get_rect()
        texto_x = ancho_ven // 2 - texto_rect.width // 2
        texto_y = alto_ven // 2 - texto_rect.height // 2
        ventana.blit(texto, [texto_x, texto_y])
        pygame.display.flip()

        esperar_tecla = True
        while esperar_tecla:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    esperar_tecla = False

        # Reiniciar el juego
        vidas = 3
        bola = Bola(ancho_ven // 2, alto_ven // 2, 10, magenta_claro, velocidad_x, -velocidad_y)
        bate = Bate(ancho_ven // 2 - 50, alto_ven - 35, 100, 20, azul)
        ladrillos = []
        for fila in range(9):
            for columna in range(9):
                x = columna * (ancho_lad + 5)
                y = fila * (alto_lad + 5)
                color_ladrillo = matriz_colores[fila][columna]
                ladrillo = Ladrillo(x + 7.5, y + 50, ancho_lad, alto_lad, color_ladrillo, color_ladrillo)
                ladrillos.append(ladrillo) 