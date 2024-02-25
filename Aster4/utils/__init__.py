import pygame as pg
import sys as LBsys
import random as LBranndom
import sqlite3 as LBsqlt3

pg.init()

width=800
height=600
NOMBRE_INGRESADO= ""
TIEMPO_INMUNE=3000 
ANCHO_MIN=0
ALTO_MIN=0
COLOR_BLANCO=(255,255,255)
FONDO_NEGRO=(0,0,0)
FUENTE1=r'Aster4\Fonts\retro_computer_personal_use.ttf'
FUENTE2=r'Aster4\Fonts\Vermin Vibes 1989.ttf'
TIEMPO_JUEGO=15000
TIEMPO_LIMIT_1=10000
TIEMPO_LIMIT_2=5000
IMG_FONDO= r'Aster4\Images\Background_stars.png'
IMG_FONDOIG= r'Aster4\Images\Back.png'
SIZE_FUENTE_1=15
SIZE_FUENTE_2=30
SIZE_FUENTE_3=72
SONIDO_AMBIENTE=r'Aster4\Songs\NightShade.mp3'
IMG_NAVE=r'Aster4\Images\Ship_3.png'
IMG_EXP=r'Aster4\Images\Explosion.png'
IMG_ASTEROID=r'Aster4\Images\Asteroid.png'
IMG_PLANETA=r'Aster4\Images\Earth.png'
SONIDO_EXPLOCION=r'Aster4\Songs\explote.mp3'
AUXVIDAS=3
AUXPUNTOS=0

historia_texto = (
            "La búsqueda...\n"
            "Comienza en un planeta tierra\n "
            "moribundo por el cambio climático.\n" 
            "Partiremos a la búsqueda de un planeta\n"
            "compatible con la vida humana para colonizarlo\n"
        )