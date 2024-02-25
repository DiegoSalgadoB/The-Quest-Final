from .utils import *

class Asteroide:
    def __init__(self, width, height):
        escala = LBranndom.uniform(0.2,1.2)
        self.image = pg.image.load(IMG_ASTEROID).convert()
        self.image.set_colorkey('BLACK')

        self.image = pg.transform.scale(self.image, (int(50*escala),int(50*escala)))  # Ajustar tamaño
        self.image = pg.transform.rotate(self.image,LBranndom.randint(0,180))

        #hitbox
        self.rect = self.image.get_rect()
        #self.rect.width = int(self.rect.width*.8)
        #self.rect.height = int(self.rect.height*.8)
        self.color = (255,0,0)

        #posicion inicial
        self.rect.x=width
        self.rect.y=LBranndom.randint(0, height - self.rect.height)     
               
        # Velocidad aleatoria en dirección x
        self.velocidad_x = LBranndom.randint(1, 5)
        self.velocidad_x2 = LBranndom.randint(4, 8)
        
    def dibujarA(self, screen):
       
        screen.blit(self.image, self.
        rect.topleft)
        pg.draw.rect(screen, self.color, self.rect, 2)  # Dibujar borde d

    def mover(self):
        self.rect.x -= self.velocidad_x
        if self.rect.x < -self.rect.width:
            self.rect.x = width
            self.rect.y = LBranndom.randint(0, height - self.rect.height)
            self.velocidad_x = LBranndom.randint(1, 5)
        # Reinicio del asteroide 
        if self.rect.x < -150:
            self.rect.x = width
            self.rect.y = LBranndom.randint(0, height - 50)
            self.velocidad_x = LBranndom.randint(1, 5)  # Actualizar velocidad al reiniciar
    
    def mover2(self):
        self.rect.x -= self.velocidad_x2
        if self.rect.x < -self.rect.width:
            self.rect.x = width
            self.rect.y = LBranndom.randint(0, height - self.rect.height)
            self.velocidad_x2 = LBranndom.randint(4, 7)
        # Reinicio del asteroide 
        if self.rect.x < -150:
            self.rect.x = width
            self.rect.y = LBranndom.randint(0, height - 50)
            self.velocidad_x2 = LBranndom.randint(4, 7)  # Actualizar velocidad al reiniciar

class Score:
    def __init__(self,FSize=25,color=(255,255,255)):
        self.font_puntajes = pg.font.Font(None, FSize)
        self.color =color
        #self.lvlcount=0
        #self.puntos=AUXPUNTOS
        #self.vidas=AUXVIDAS

    def mostrar (self, screen, variable1,variable2):
        texto = f"Marcador: {variable1}, Vidas: {variable2}"
        texto_superficie = self.font_puntajes.render(texto, True, self.color)
        texto_rect = texto_superficie.get_rect(topleft=(10, 10))  # Ajusta la posición según tu preferencia
        screen.blit(texto_superficie,texto_rect.topleft)
    
    def bonof(variable1):
        variable1 +=1000

class Nave:
    def __init__(self):
        self.image = pg.image.load(IMG_NAVE).convert()
        self.image.set_colorkey(pg.Color('BLACK'))
        self.image = pg.transform.scale(self.image, (50, 50))
        self.image = pg.transform.rotate(self.image,- 90)
        self.inmune=False

        self.fondo = pg.image.load(IMG_FONDOIG).convert()
        
        ##self.fondo = pg.transform.scale(self.fondo, (width, height))
        
        # posicion inicial
        self.x = width -790
        self.y = height // 2 - 25  #division entera entre2 -25
        self.color = (255,0,0)

    def mover_arriba(self):
        self.y -= 5
        if self.y < 0:
            self.y = 0

    def mover_abajo(self):
        self.y += 5
        if self.y > height - 50:  
            self.y = height - 50

    def HitBoxN (self):
        if self.inmune==False:
           return pg.Rect(self.x, self.y, 50, 50)#genera la hitbox sin inmune
        elif self.inmune==True:
           ##screen.blit(self.image,(self.
           # x, self.y))
            #MOVER
            print("HTBX")
    
    def DibujarN(self,screen):
        if self.inmune==False:
            self.rect = self.image.get_rect()
            screen.blit(self.image,(self.x, self.y))
            #pg.draw.rect(screen, self.color, self.HitBoxN(),2)  # Dibujar borde 
        elif self.inmune==True:
            screen.blit(self.image,(self.
            x, self.y))

    ##secuencia Final
    def moverF(self, screen,vidas,pPuntos):
        #pPuntos=auxPuntaje
        #vidas=auxVIDAS
        #self.fondo = pg.image.load(IMG_FONDOIG).convert()
        self.fondo = pg.image.load(IMG_FONDOIG).convert()
        self.fondo = pg.transform.scale(self.fondo, (width, height))
        
        Marcador=Score()        
        planeta = Planeta(width,height)
        velocidad_desplazamiento = 3
        velocidad_rotacion = 1  
        centro_y = height // 2 - 25
        rotated_angle=0
        angulo_maximo = 180
        
        
        self.velocidad = 2
        #auxFondo((width,height))
        screen.blit(self.fondo,(0,0))
        Marcador.mostrar(screen, pPuntos, vidas)
        screen.blit(self.image, (self.x, self.y))
        planeta.moverPF(screen)
        
        animacion=True
        while animacion:
            for evento in pg.event.get():
                if evento.type == pg.QUIT:
                    animacion=False
            screen.fill((0,0,0))
            screen.blit(self.fondo,(0,0))
            Marcador.mostrar(screen, pPuntos, vidas)
            planeta.dibujar(screen)

            if self.y < centro_y:
                self.y += velocidad_desplazamiento
                screen.blit(self.image, (self.x, self.y))
        
            if self.y > centro_y:
                self.y -= velocidad_desplazamiento
                screen.blit(self.image, (self.x, self.y))
        
        # Si     ha llegado al centro en el eje y, mover hacia la derecha en el eje x
            if  self.x < 700:
                self.x += velocidad_desplazamiento
                screen.blit(self.image, (self.x, self.y))
        
    # Rotación gradual a 180 grados después del movimiento en x
            #rotated_angle = 0
            elif rotated_angle < 180:
                rotated_angle += velocidad_rotacion
                rotated_image = pg.transform.rotate(self.image, rotated_angle)
                screen.blit(rotated_image, (self.x, self.y))
                pg.display.flip()

            else:
                return "Partida"
                

            pg.display.flip()
            pg.time.Clock().tick(60)
            

class Planeta:
    def __init__(self, width, height):
        self.image = pg.image.load(IMG_PLANETA)
        self.image = pg.transform.scale(self.image, (600, 600))  # Ajustar tamaño

        # Posicionar en el borde derecho centrado verticalmente
        self.x = width - 1200
        self.y = height // -50  # Centrar verticalmente
        self.velocidad = 1 

    def dibujar(self, screen):
        screen.blit(self.image, (self.x, self.y))
        
    def mover(self):
        self.x -=self.velocidad

    def moverPF(self,screen):
        self.x = width
        self.y = height // 2 - 300  # Centrar verticalmente
        self.velocidad = 1 
        
        while self.x > width- 300:
            # Dibujar la animación en cada iteración
            self.mover()
            self.dibujar(screen)
            pg.display.flip()
            pg.time.Clock().tick(60)
