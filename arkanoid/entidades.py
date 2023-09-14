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
    velocidad_x = -15
    velocidad_y = -15
    control_animacion = 1

    def __init__(self, raqueta):
        super().__init__()
        self.imagenes = []
        for i in range(5):
            ruta_img = os.path.join("resources", "images", f"ball{i+1}.png")
            self.imagenes.append(pg.image.load(ruta_img))
        self.contador = 0
        self.image = self.imagenes[self.contador]
        self.raqueta = raqueta
        self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)

    def update(self, partida_empezada):
        # Animación de la pelota

        # Mover pelota
        if partida_empezada:
            self.rect.x += self.velocidad_x
            if self.rect.left <= 0 or self.rect.right > ANCHO:
                # self.rebote()
                self.velocidad_x = -self.velocidad_x

            self.rect.y += self.velocidad_y
            if self.rect.top <= 0:
                # self.rebote()
                self.velocidad_y = -self.velocidad_y
        else:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)

    def rebote(self):
        self.contador += self.control_animacion
        if self.contador in (0, 4):
            self.control_animacion = -self.control_animacion
        self.image = self.imagenes[self.contador]


class Ladrillo(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        ruta_verde = os.path.join("resources", "images", "greenTile.png")
        self.image = pg.image.load(ruta_verde)
        self.rect = self.image.get_rect()

    def update():
        pass
