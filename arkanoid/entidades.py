import os

import pygame as pg

from . import ANCHO, ALTO


class Raqueta(pg.sprite.Sprite):
    margen = 25
    velocidad = 20

    def __init__(self):
        super().__init__()
        self.imagenes = []
        for i in range(3):
            ruta_img = os.path.join("resources", "images", f"electric0{i}.png")
            self.imagenes.append(pg.image.load(ruta_img))
        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO - self.margen))

    def update(self):
        self.contador += 1
        if self.contador > 2:
            self.contador = 0
        self.image = self.imagenes[self.contador]

        teclas = pg.key.get_pressed()
        if teclas[pg.K_RIGHT]:
            if self.rect.x >= ANCHO-self.rect.width:
                self.rect.right = ANCHO
            else:
                self.rect.x += self.velocidad
        if teclas[pg.K_LEFT]:
            if self.rect.x <= 0:
                self.rect.x = 0
            else:
                self.rect.x -= self.velocidad

    def mover(self):

        pass

    def pintar(self):
        pass

    def reset(self):
        pass
