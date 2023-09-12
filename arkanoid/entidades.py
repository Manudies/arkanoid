import os

import pygame as pg

from . import ANCHO, ALTO, MARGEN


class Raqueta(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        ruta_img = os.path.join("resources", "images", "electric00.png")
        self.image = pg.image.load(ruta_img)
        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-MARGEN))

    def update(seld):
        pass

    def mover(self):
        pass

    def pintar(self):
        pass

    def reset(self):
        pass
