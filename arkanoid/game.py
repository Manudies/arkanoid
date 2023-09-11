import pygame as pg
from . import ANCHO, ALTO, COLOR_FONDO_PARTIDA, COLOR_FONDO_MEJORES_JUGADORES, COLOR_FONDO_PORTADA
from .escenas import MejoresJugadores, Partida, Portada


class Arkanoid:
    def __init__(self):
        pg.init()
        self.pantalla = pg.display.set_mode((ANCHO, ALTO))

        portada = Portada(self.pantalla)
        partida = Partida(self.pantalla)
        record = MejoresJugadores(self.pantalla)

        self.escenas = [portada, partida, record]

    def jugar(self):
        """Bucle principal"""
        for escena in self.escenas:
            escena.bucle_principal()
        pg.quit()


if __name__ == "__main__":
    juego = Arkanoid()
    juego.jugar()
