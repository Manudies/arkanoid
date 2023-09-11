# Librerias estandar
import os
# Librerias de terceros
import pygame as pg
# Tus dependencias
from . import ANCHO, ALTO, COLOR_FONDO_PARTIDA, COLOR_FONDO_MEJORES_JUGADORES, COLOR_FONDO_PORTADA


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla

    def bucle_principal(self):
        """Este metodo es implementado por todas las escenas, 
        en función de lo que esten esperando hasta la condición de salida """


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "arkanoid_name.png")
        self.logo = pg.image.load(ruta)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True
            self.pantalla.fill(COLOR_FONDO_PORTADA)
            self.pintar_logo()
            pg.display.flip()

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO-ancho)/2
        pos_y = (ALTO-alto)/2
        self.pantalla.blit(self.logo, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True
            self.pantalla.fill(COLOR_FONDO_PARTIDA)
            pg.display.flip()


class MejoresJugadores (Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if pg.QUIT == evento.type:
                    salir = True
            self.pantalla.fill(COLOR_FONDO_MEJORES_JUGADORES)
            pg.display.flip()
