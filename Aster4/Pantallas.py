from .utils import*
from .Figuras import*

class Partida:
    def __init__(self):
        pPuntos =  0
        self.auxVIDAS = 0
        
    def MainGame(self):
        # Configuración de la ventana
        PanGO = PantallaGameOver()
        screen = pg.display.set_mode((width, height))
        pg.display.set_caption("The Quest")
        # Crear instancia de la clase Nave
        nave = Nave()

        # Cargar fondo
        fondo = pg.image.load(IMG_FONDOIG)
        fondo = pg.transform.scale(fondo, (width, height))

        # Crear instancias de la clase Asteroide
        asteroides = [Asteroide (width, height) for i in range(10)]

        #cargar sonidos
        imgExplo = pg.image.load(IMG_EXP)
        SoundExplo = pg.mixer.Sound(SONIDO_EXPLOCION)
        SoundExplo.set_volume(.9)
        SoundFondo = pg.mixer.Sound(SONIDO_AMBIENTE)
        SoundExplo.set_volume(.025)
        SoundFondo.play()

        # Instancia Marcador
        Marcador = Score()
        pPuntos = 0
        vidas = 3

        #Planeta de salida
        planeta = Planeta(width, height)

        # Bucle principal
        duracion_inmunidad=3000
        tiempo_inmunidad=0
        SoundFondo.set_volume(.05)    
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                nave.mover_arriba()
            if keys[pg.K_DOWN]:
                nave.mover_abajo()

            # Mover planeta inicio
            planeta.mover()

            # Limpiar la pantalla
            screen.fill((0, 0, 0))

            # Dibujar fondo
            screen.blit(fondo, (0, 0))

            # Dibujar el planeta
            planeta.dibujar(screen)

            # Mover y dibujar la nave
            nave.DibujarN(screen)

            ##aumentar puntaje2daopcion
            Marcador.mostrar(screen, pPuntos, vidas)

            ###final de nivel
            if pPuntos % 5 ==0 and pPuntos >= 100:
                print("animacion final")

                pPuntos=pPuntos+1000
                AUXPUNTOS = pPuntos
                self.auxVIDAS=vidas
                AUXVIDAS=self.auxVIDAS
                #print(AUXVIDAS)
                #print(AUXPUNTOS)
                
                nave.moverF(screen,AUXVIDAS,AUXPUNTOS)#ANIMACION   
                PanGO.bucle_win()
                return Partida.MainGame2(self,vidas,pPuntos) 


            #Mover y dibujar cada asteroide/-+

            for asteroide in asteroides:
                asteroide.mover()
                asteroide.dibujarA(screen)
                if asteroide.rect.x < 10:
                    pPuntos += 1   

                if nave.inmune == False:
                    if nave.HitBoxN().colliderect(asteroide.rect):
                        print("¡Colisión! El juego se detiene.")
                        screen.blit(imgExplo, (nave.x - 25, nave.y -25))
                        # Reproducir el sonido de explosión
                      
                        SoundExplo.play()
                        vidas -=1
                        print(vidas)      
                        if not nave.inmune:
                            nave.inmune = True
                            #print("inmune")
                            tiempo_inmunidad=pg.time.get_ticks()

                        if vidas == 0:
                            print("pantalla de game over")
                            PanGO.bucledepantalla()
                            return #muestra game over

                        #pass       

                tiempo_trans = pg.time.get_ticks()-tiempo_inmunidad
                if tiempo_trans >= duracion_inmunidad:
                    nave.inmune=False
                    #print("fin de inmune")

            pg.display.flip()
            # Controlar la velocidad del bucle
            pg.time.Clock().tick(30)

    def MainGame2(self,vidas,pPuntos):            
        # Configuración de la ventana

        PanGO = PantallaGameOver()
        screen = pg.display.set_mode((width, height))
        pg.display.set_caption("The Quest")
        # Crear instancia de la clase Nave
        nave = Nave()
        # Cargar fondo
        fondo = pg.image.load(IMG_FONDOIG)
        fondo = pg.transform.scale(fondo, (width, height))

        # Crear instancias de la clase Asteroide
        asteroides = [Asteroide (width, height) for i in range(10)]

        #cargar sonidos
        imgExplo = pg.image.load(IMG_EXP)
        SoundExplo = pg.mixer.Sound(SONIDO_EXPLOCION)   
        SoundExplo.set_volume(.5)     

        # Instancia Marcador
        Marcador = Score()

        #Planeta de salida
        planeta = Planeta(width, height)

        # Bucle principal
        duracion_inmunidad=3000
        tiempo_inmunidad=0
        
        while True:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    #sys.exit()

            keys = pg.key.get_pressed()
            if keys[pg.K_UP]:
                nave.mover_arriba()
            if keys[pg.K_DOWN]:
                nave.mover_abajo()

            # Mover planeta inicio
            planeta.mover()

            # Limpiar la pantalla
            screen.fill((0, 0, 0))

            # Dibujar fondo
            screen.blit(fondo, (0, 0))

            # Dibujar el planeta
            planeta.dibujar(screen)

            # Mover y dibujar la nave
            nave.DibujarN(screen)

            ##aumentar puntaje2daopcion
            Marcador.mostrar(screen, pPuntos, vidas)


            ###final de nivel
            if pPuntos % 100 ==0 and pPuntos >= 2100:
                print("animacion final")

                pPuntos=(pPuntos+1000)*vidas
                AUXPUNTOS = pPuntos
                self.auxVIDAS=vidas
                AUXVIDAS=self.auxVIDAS
                print(AUXVIDAS)
                print(AUXPUNTOS)
                
                nave.moverF(screen,AUXVIDAS,AUXPUNTOS)#ANIMACION 
                PanGO.bucledepantalla()
                pg.mixer.stop()
                return  InputBox(300, 300, 140, 32, max_length=3).bucle_pantalla(pPuntos)

            
            #Mover y dibujar cada asteroide/-+

            for asteroide in asteroides:
                asteroide.mover2()
                asteroide.dibujarA(screen)
                if asteroide.rect.x < 10:
                    pPuntos += 1   

                if nave.inmune == False:
                    if nave.HitBoxN().colliderect(asteroide.rect):
                        print("¡Colisión! El juego se detiene.")
                        screen.blit(imgExplo, (nave.x - 25, nave.y -25))
                        # Reproducir el sonido de explosión
                        SoundExplo.play()
                        vidas -=1
                        print(vidas)      
                        if not nave.inmune:
                            nave.inmune = True
                            #print("inmune")
                            tiempo_inmunidad=pg.time.get_ticks()

                        if vidas == 0:
                            print("pantalla de game over")
                            PanGO.bucledepantalla()
                            #pg.time.wait(2000)
                            return 
                            #topten

                        #pass       

                tiempo_trans = pg.time.get_ticks()-tiempo_inmunidad
                if tiempo_trans >= duracion_inmunidad:
                    nave.inmune=False
                    #print("fin de inmune")

            pg.display.flip()
            # Controlar la velocidad del bucle
            pg.time.Clock().tick(30)


class Portada:
    def __init__(self):
        self.screen = pg.display.set_mode((width, height))
        pg.display.set_caption("The Quest") 
        self.tasa_refresco= pg.time.Clock()
        self.BGfondo=pg.image.load(IMG_FONDO)
        self.BGfondo= pg.transform.scale(self.BGfondo, (width, height))
        self.sonido = pg.mixer.Sound(SONIDO_AMBIENTE)

        self.fuente=pg.font.Font(FUENTE1,25)

        self.historia = historia_texto
        self.font_historia = pg.font.Font(None, 22)
        #TheQuest
        self.font_titulo = pg.font.Font(FUENTE2,72)
        self.titulo = self.font_titulo.render("The Quest", True, (255, 255, 255))
        self.titulo_rect = self.titulo.get_rect(center=(width// 2,height//2 - 100))

        #instruccion Presiona tecla
        self.font = pg.font.Font(FUENTE1,22)
        self.text = self.font.render("Presiona cualquier tecla para iniciar",True,(255,255,255))
        self.text_rect = self.text.get_rect(center=(width//2, height // 2))


    def bucle_pantalla(self):
        
        game_over=True
        tiempo_inicio1 = pg.time.get_ticks()
        duracion_portada = 3000
        while game_over:
            self.sonido.set_volume(0.015)
            self.sonido.play()
            
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    return True 
                if event.type==pg.KEYDOWN:
                   self.sonido.stop()
                   return Partida.MainGame(self)
                
            tiempo_actual1 = pg.time.get_ticks()
            tiempo_transcurrido1 = tiempo_actual1 - tiempo_inicio1
            #print(tiempo_transcurrido1)   
           
            if tiempo_transcurrido1>=duracion_portada:
               return "Records"
                 
           
            # Actualizar fondo
            self.screen.blit(self.BGfondo,(0,0)) 
            #historia linea por linea
            lineas_texto = historia_texto.split('\n')
            y_offset = 0

            for linea in lineas_texto:
                texto_renderizado = self.font_historia.render(linea, True, (255, 255, 255))
                texto_rect = texto_renderizado.get_rect(center=(width // 2, height // 2 + 150 + y_offset))
                self.screen.blit(texto_renderizado, texto_rect)
                y_offset += 30 

            self.screen.blit(self.titulo, self.titulo_rect)  # título
            self.screen.blit(self.text, self.text_rect)  # texto

            pg.display.flip()    
    
    

class PantallaGameOver:
    def __init__(self):
        self.screen=pg.display.set_mode((width,height))
        self.screen.fill(FONDO_NEGRO)  # Fondo negro
        pg.display.set_caption("The Quest")
        self.tasa_refresco= pg.time.Clock()

        #gameover
        self.font_titulo = pg.font.Font(FUENTE2, 72)
        self.titulo = self.font_titulo.render("Game Over", True, (244, 244, 244))
        self.titulo_rect = self.titulo.get_rect(center=(width // 2, height // 2))
           
        #instrucciones
        self.font_instrucciones = pg.font.Font(FUENTE1,16)
        self.instrucciones = self.font_instrucciones.render("Presiona cualquier tecla para continuar", True, (255, 255, 255))
        self.instrucciones_rect = self.instrucciones.get_rect(center=(width // 2, height // 2 + 100))

        #victoria
        self.font_win=pg.font.Font(FUENTE2,72)
        self.win = self.font_win.render("VICTORIA",True,(COLOR_BLANCO))
        self.win_rect=self.win.get_rect(center=(width//2, height //2))

    def bucledepantalla(self):
        volver_portada=False
        while not volver_portada:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.KEYDOWN:
                    pg.mixer.stop()
                    volver_portada=True
                    return "Portada"

            # Mostrar el título "Game Over"
            self.screen.blit(self.titulo, self.titulo_rect)
            # Mostrar instrucciones
            self.screen.blit(self.instrucciones, self.instrucciones_rect)     
            pg.display.flip()    

    def bucle_win(self):
        volver_portada=False
        while not volver_portada:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()

                if event.type == pg.KEYDOWN:
                    volver_portada=True
                    return 

            # Mostrar el título "Game Over"
            self.screen.blit(self.win, self.win_rect)
            # Mostrar instrucciones
            self.screen.blit(self.instrucciones, self.instrucciones_rect)     
            pg.display.flip()    



class DBrec:
########BASE de Datos##########
    def __init__(self):
        self.con = LBsqlt3.connect("Records.db")   
        self.cursor = self.con.cursor()

        self.cursor.execute('''CREATE TABLE IF NOT EXISTS Puntajes (
                                id INTEGER PRIMARY KEY,
                                nombre TEXT,
                                puntos INTEGER
                              )''')
        
    def agregar_puntaje(self, nombre, puntos):
        self.cursor.execute("INSERT INTO Puntajes (nombre, puntos) VALUES (?, ?)", (nombre, puntos))
        self.con.commit()
    
    def obtener_puntajes(self):
        self.cursor.execute("SELECT * FROM Puntajes ORDER BY puntos DESC")
        return self.cursor.fetchall()
    
    def mostrar_tabla(self):

        screen=pg.display.set_mode((width,height))
        #puntajes=[10,20,3,4,5,6,7,8,9,1]
     
        # Obtener los puntajes desde la base de datos
        puntajes = self.obtener_puntajes()[:10]

        # Limpiar la pantalla
        screen.fill((0, 0, 0))

        # Configurar la fuente para mostrar los puntajes
        font = pg.font.Font(FUENTE1, 20)
        y_pos = 50
        font2=pg.font.Font(FUENTE2,62)
        # Mostrar encabezado
        encabezado_texto = font2.render("TOP PLAYERS", True, (COLOR_BLANCO))
        screen.blit(encabezado_texto, (width // 2 - 190, y_pos))
        
        
        y_pos += 80
        # Mostrar los puntajes
        for i,puntaje in enumerate(puntajes, start=1):
            texto = f"{i}. {puntaje[1]}: {puntaje[2]}"
            puntaje_texto = font.render(texto, True, (COLOR_BLANCO))
            screen.blit(puntaje_texto, (width // 2 - 100, y_pos))
            y_pos += 30

        #Bucle de tiempo o tecla para records
        Trecords = pg.time.get_ticks()
        while  pg.time.get_ticks() - Trecords <=5000:
            AuxTrecords =(pg.time.get_ticks()-Trecords)
            #print(AuxTrecords)
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    LBsys.exit()
                elif event.type == pg.KEYDOWN:
                    return "portada"
            pg.display.flip()
    
############################
    
class InputBox:
    def __init__(self, x, y, width, height, max_length):
        self.rect = pg.Rect(x, y, width, height)
        self.color_inactive = pg.Color('lightskyblue3')
        self.color_active = pg.Color('dodgerblue2')
        self.color = self.color_inactive
        self.text = ''
        self.font = pg.font.Font(None, 32)
        self.active = False
        self.max_length = max_length
        self.nombre=NOMBRE_INGRESADO
        self.DBrecords=DBrec()

    
    def handle_event(self,event,puntos):
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = self.color_active if self.active else self.color_inactive
        if event.type == pg.KEYDOWN:
            if self.active:
                if event.key == pg.K_RETURN:
                    # Limitar la longitud del texto a self.max_length
                    self.text = self.text[:self.max_length]
                    self.active = False  # Desactivar la caja después de presionar Enter
                    # Asignar el valor de self.text a la variable global nombre_ingresado
                    self.nombre = self.text
                    NOMBRE_INGRESADO = self.nombre
                    
                    #print(NOMBRE_INGRESADO)
                    self.DBrecords.agregar_puntaje(NOMBRE_INGRESADO,puntos)#1000PTS PENDIENTE

                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    # Limitar la longitud del texto a self.max_length
                    if len(self.text) < self.max_length:
                        self.text += event.unicode

    def update(self):
        width = max(200, self.font.render(self.text, True, self.color).get_width()+10)
        self.rect.w = width

    def draw(self, screen):
        txt_surface = self.font.render(self.text, True, self.color)
        width = max(200, txt_surface.get_width()+10)
        self.rect.w = width
        screen.blit(txt_surface, (self.rect.x+5, self.rect.y+5))
        pg.draw.rect(screen, self.color, self.rect, 2)

    def bucle_pantalla(self,pPuntos):
        screen=pg.display.set_mode((width,height))
        clock = pg.time.Clock()
        input_box = InputBox(300, 300, 140, 32, max_length=3)
        input_boxes = [input_box]
        puntos=pPuntos
        done = False

        while not done:
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    done = True
                for box in input_boxes:
                    box.handle_event(event,puntos)

            for box in input_boxes:
                box.update()

            screen.fill((FONDO_NEGRO))

            font = pg.font.Font(None, 36)
            titulo_texto = font.render("Ingresa tus iniciales y presiona enter", True, (255, 255, 255))
            screen.blit(titulo_texto, (width // 2 - 200, 50))

            for box in input_boxes:
                box.draw(screen)

            pg.display.flip()
            clock.tick(30)

            keys = pg.key.get_pressed()
            if keys[pg.K_RETURN]:
                done = True
                return 