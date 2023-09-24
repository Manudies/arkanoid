import os
from random import randint, choice

import pygame as pg

from . import ANCHO, ALTO, VIDAS, ALTO_MARCADOR, VEL_MAX, VEL_MIN_Y


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

    def reset(self):
        pass


class Pelota(pg.sprite.Sprite):
    vel_x = -15
    vel_y = -15

    def __init__(self, raqueta):
        super().__init__()
        self.imagenes = []
        for i in range(5):
            ruta_img = os.path.join("resources", "images", f"ball{i+1}.png")
            self.imagenes.append(pg.image.load(ruta_img))
        self.contador = 0
        self.control_animacion = 1
        self.image = self.imagenes[self.contador]
        self.raqueta = raqueta
        self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
        self.he_perdido = False

    def inicializar_velocidades(self):
        self.vel_x = randint(-VEL_MAX, VEL_MAX)
        self.vel_y = randint(-VEL_MAX, VEL_MIN_Y)

    def update(self, se_mueve_la_pelota):
        # Mover pelota
        if se_mueve_la_pelota == False:
            self.rect = self.image.get_rect(midbottom=self.raqueta.rect.midtop)
            return False, False
        else:
            self.rect.x += self.vel_x
            if self.rect.left <= 0 or self.rect.right >= ANCHO:
                self.vel_x = -self.vel_x
            self.rect.y += self.vel_y

            if self.rect.top <= ALTO_MARCADOR:
                # self.rebote()
                self.vel_y = -self.vel_y

            if pg.sprite.collide_mask(self, self.raqueta):
                self.inicializar_velocidades()

            # FIXME Devolver pelota el centro de la pala si sale por abajo
            if self.rect.top >= ALTO:
                self.inicializar_velocidades()
                self.he_perdido = True

        # Rebote Pala
        # if self.rect.colliderect(self.raqueta):
            # Opción con mask "PYgame crea las mascaras" Colisión mas precisa
            # rebota a 90º aleatoriamente a derechas o izquierdas (Posible modo FACIL)
            # self.velocidad_y = -self.velocidad_y
            # self.velocidad_x = choice([self.velocidad_x, -self.velocidad_x])
            # rebota aleatoriamente con un velocidad MIN en Y

    def rebote_animacion(self):
        self.contador += self.control_animacion
        if self.contador == 4:
            self.control_animacion = -self.control_animacion
        if self.contador == 0:
            self.rect.y -= self.vel_y
        self.image = self.imagenes[self.contador]


class Ladrillo(pg.sprite.Sprite):
    VERDE = 0
    ROJO = 1
    ROJO_ROTO = 2
    IMG_LADRILLO = ["greenTile.png", "redTile.png", "redTileBreak.png"]

    def __init__(self, puntos, color=VERDE):
        super().__init__()
        self.tipo = color
        self.imagenes = []
        for img in self.IMG_LADRILLO:
            ruta = os.path.join(
                'resources', 'images', img)
            self.imagenes.append(pg.image.load(ruta))
        self.image = self.imagenes[color]
        self.rect = self.image.get_rect()
        self.puntos = puntos

    def update(self, muro):
        """
        Según el tipo de ladrillo, se fragmenta en el primer golpe
        o se elimina directamente.
        Devuelve True si el ladrillo se ha eliminado del muro
        Devuelve False en caso contrario.
        """
        if self.tipo == Ladrillo.ROJO:
            self.tipo = Ladrillo.ROJO_ROTO
            self.image = self.imagenes[self.tipo]
            return False
        else:
            muro.remove(self)
            return True


class ContadorVidas:
    def __init__(self, vidas_iniciales):
        self.vidas = vidas_iniciales

    def perder_vida(self):
        self.vidas -= 1
        return self.vidas < 0

    def pintar(self):
        pass


class Marcador:
    def __init__(self):
        self.valor = 0
        self.puntos = "Puntos:"
        fuente = 'LibreFranklin-VariableFont_wght.ttf'
        ruta = os.path.join('resources', 'fonts', fuente)
        self.tipo_letra = pg.font.Font(ruta, 30)

    def aumentar(self, incremento):
        self.valor += incremento

    def pintar(self, pantalla):
        r = pg.rect.Rect(0, 0, ANCHO, ALTO_MARCADOR)
        pg.draw.rect(pantalla, (0, 0, 0), r)
        cadena = str(self.valor)
        fijo = str(self.puntos)
        texto = self.tipo_letra.render(cadena, True, (230, 189, 55))
        texto_fijo = self.tipo_letra.render(fijo, True, (230, 189, 55))
        pos_x = 20
        pos_y = (ALTO_MARCADOR-30)/2
        pantalla.blit(texto_fijo, (pos_x, pos_y))
        pantalla.blit(texto, (pos_x + 110, pos_y))
