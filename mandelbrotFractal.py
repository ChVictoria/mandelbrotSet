import pygame as pg
import numpy as np

pg.init()

d_size = width, height = 180, 120
name = "*Journey through the Mandelbrot fractal*"
icon_picture = 'icon.png'


class Fractal:
    def __init__(self, game):
        self.game = game

    def run(self):
        pass


class Game:
    """The standard class that creates a set resolution window."""

    def __init__(self):
        self.display = pg.display.set_mode(d_size, pg.RESIZABLE, pg.SCALED)
        self.clock = pg.time.Clock()

    pg.display.set_caption(name)
    icon = pg.image.load(icon_picture)
    pg.display.set_icon(icon)

    def run_game(self):
        while True:
            self.display.fill('black')
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            pg.display.update()
            self.clock.tick(60)


game = Game()
game.run_game()
