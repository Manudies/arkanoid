# Librerias estandar
import os
# Librerias de terceros
import pygame as pg
# Tus dependencias
from . import ANCHO, ALTO, COLOR_FONDO_PARTIDA, COLOR_FONDO_MEJORES_JUGADORES, COLOR_FONDO_PORTADA, FPS
from .entidades import Ladrillo, Pelota, Raqueta


class Escena:
    def __init__(self, pantalla):
        self.pantalla = pantalla
        self.reloj = pg.time.Clock()

    def bucle_principal(self):
        """Este metodo es implementado por todas las escenas, 
        en función de lo que esten esperando hasta la condición de salida """
        print('Método vacío bucle principal de ESCENA')


class Portada(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "arkanoid_name.png")
        self.logo = pg.image.load(ruta)

        ruta = os.path.join("resources", "fonts", "CabinSketch-Bold.ttf")
        self.tipo = pg.font.Font(ruta, 35)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT or (evento.type == pg.KEYUP and evento.key == pg.K_ESCAPE):
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    salir = True
            self.pantalla.fill(COLOR_FONDO_PORTADA)
            self.pintar_logo()
            self.pintar_mensaje()
            pg.display.flip()

    def pintar_mensaje(self):
        mensaje = "Pulsa <ESPACIO> para comenzar la partida"
        texto = self.tipo.render(mensaje, True, (255, 255, 255))
        pos_x = (ANCHO - texto.get_width())/2
        pos_y = ALTO * 3/4
        self.pantalla.blit(texto, (pos_x, pos_y))

    def pintar_logo(self):
        ancho, alto = self.logo.get_size()
        pos_x = (ANCHO-ancho)/2
        pos_y = (ALTO-alto)/2
        self.pantalla.blit(self.logo, (pos_x, pos_y))


class Partida(Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)
        ruta = os.path.join("resources", "images", "background.jpg")
        self.fondo = pg.image.load(ruta)
        self.jugador = Raqueta()
        self.muro = pg.sprite.Group()
        self.pelota = Pelota(self.jugador)

    def bucle_principal(self):
        super().bucle_principal()
        print("Tengo", len(self.muro), "ladrillos")
        self.crear_muro()
        print("Tengo", len(self.muro), "ladrillos")
        salir = False
        juego_iniciado = False
        while not salir:
            self.reloj.tick(FPS)
            for evento in pg.event.get():
                if evento.type == pg.QUIT or (evento.type == pg.KEYUP and evento.key == pg.K_ESCAPE):
                    return True
                if evento.type == pg.KEYDOWN and evento.key == pg.K_SPACE:
                    juego_iniciado = True
            self.pintar_fondo()
            self.jugador.update()
            self.pantalla.blit(self.jugador.image, self.jugador.rect)
            self.muro.draw(self.pantalla)
            self.pelota.update(juego_iniciado)
            self.pantalla.blit(self.pelota.image, self.pelota.rect)
            pg.display.flip()

    def pintar_fondo(self):
        self.pantalla.fill(COLOR_FONDO_PARTIDA)
        # Mejorar este sistema de pintado
        self.pantalla.blit(self.fondo, (0, 0))
        self.pantalla.blit(self.fondo, (600, 0))
        self.pantalla.blit(self.fondo, (0, 800))
        self.pantalla.blit(self.fondo, (600, 800))
        self.pantalla.blit(self.fondo, (1200, 0))

    def crear_muro(self):
        filas = 4
        columnas = 6
        margen_superior = 25
        ladrillo_med = Ladrillo()
        margen_izquierdo = ((ANCHO - ladrillo_med.rect.width*columnas)/2)
        for fil in range(filas):  # 0-3
            for col in range(columnas):
                ladrillo = Ladrillo()
                self.muro.add(ladrillo)
                ladrillo.rect.x = ladrillo.rect.width * col + margen_izquierdo
                ladrillo.rect.y = ladrillo.rect.height * fil + margen_superior


class MejoresJugadores (Escena):
    def __init__(self, pantalla):
        super().__init__(pantalla)

    def bucle_principal(self):
        super().bucle_principal()
        salir = False
        while not salir:
            for evento in pg.event.get():
                if evento.type == pg.QUIT or (evento.type == pg.KEYUP and evento.key == pg.K_ESCAPE):
                    return True
            self.pantalla.fill(COLOR_FONDO_MEJORES_JUGADORES)
            pg.display.flip()
