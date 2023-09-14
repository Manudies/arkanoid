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
            self.rect.x += self.velocidad
            if self.rect.x >= ANCHO-self.rect.width:
                self.rect.right = ANCHO
        if teclas[pg.K_LEFT]:
            self.rect.x -= self.velocidad
            if self.rect.x <= 0:
                self.rect.x = 0

    def mover(self):

        pass

    def pintar(self):
        pass

    def reset(self):
        pass


class Pelota(pg.sprite.Sprite):
    velocidad = 15
    margen = 25+30
    control_animacion = 1

    def __init__(self):
        super().__init__()
        self.imagenes = []
        for i in range(5):
            ruta_img = os.path.join("resources", "images", f"ball{i+1}.png")
            self.imagenes.append(pg.image.load(ruta_img))
        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.rect = self.image.get_rect(
            midbottom=(ANCHO/2, ALTO - self.margen))

    def update(self):
        # Animación de la pelota
        # self.contador += self.control_animacion
        # if self.contador in (0, 4):
        #    self.control_animacion = -self.control_animacion
        # self.image = self.imagenes[self.contador]
        # Mover pelota
        for evento in pg.event.get():
            if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                self.rect.x -= self.velocidad
                self.rect.y -= self.velocidad


class Ladrillo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ruta_verde = os.path.join("resources", "images", "greenTile.png")
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()

    def update():
        pass
