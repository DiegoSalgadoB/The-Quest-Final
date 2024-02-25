from .Pantallas import *

class PantallaControlador:
    def __init__(self):
        #instancias 
        self.Resultado_final=""
        self.portada=Portada()
        self.GO=PantallaGameOver()
        self.Records=InputBox(300, 300, 140, 32, max_length=3)
        self.DBrecords=DBrec()
        self.partida=Partida()


    def start(self):
        cerrar=""
        while True:
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    return True
                
                cerrar = self.portada.bucle_pantalla()
                if cerrar==True:
                    break
                
                self.DBrecords.mostrar_tabla()

            
            if cerrar:       
                break
            
            #self.GO.bucledepantalla()
            #self.Records.bucle_pantalla()



        