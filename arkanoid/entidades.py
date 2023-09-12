import os

import pygame as pg

from . import ANCHO, ALTO, MARGEN


class Raqueta(pg.sprite.Sprite):

    def __init__(self):
        super().__init__()
        self.imagenes = []
        for i in range(3):
            ruta_img = os.path.join("resources", "images", f"electric0{i}.png")
            self.imagenes.append(pg.image.load(ruta_img))
        self.contador = 0
        self.image = self.imagenes[self.contador]

        self.rect = self.image.get_rect(midbottom=(ANCHO/2, ALTO-MARGEN))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]

    def mover(self):
        pass

    def pintar(self):
        pass

    def reset(self):
        pass
