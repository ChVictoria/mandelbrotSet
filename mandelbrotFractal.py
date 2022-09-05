import pygame as pg
import numpy as np
import math

pg.init()

# settings
d_size = width, height = 800, 450
name = "*Journey through the Mandelbrot fractal*"
icon_picture = 'images/icon.png'
offset = np.array([1.3 * width, height]) // 2
max_iter = 30
zoom = 2.2 / height

# texture
texture = pg.image.load('images/texture2.jpg')
texture_size = min(texture.get_size()) - 1
texture_array = pg.surfarray.array3d(texture)


class Fractal:
    def __init__(self, game):
        self.game = game
        self.screen_array = np.full((width, height, 3), [0, 0, 0], dtype=np.uint8)

    def render(self):
        for x in range(width):
            for y in range(height):
                c = (x - offset[0]) * zoom + 1j * (y - offset[1]) * zoom
                z = 0
                num_iter = 0
                for i in range(max_iter):
                    z = z ** 2 + c
                    if abs(z) > 2:
                        break
                    num_iter += 1
                col = int(texture_size * num_iter / max_iter)
                self.screen_array[x, y] = texture_array[col, col]

    def update(self):
        self.render()

    def draw(self):
        pg.surfarray.blit_array(self.game.display, self.screen_array)

    def run(self):
        self.update()
        self.draw()


class Game:
    """The standard class that creates a set resolution window."""

    def __init__(self):
        self.display = pg.display.set_mode(d_size, pg.SCALED)
        self.clock = pg.time.Clock()
        self.fractal = Fractal(self)

    pg.display.set_caption(name)
    icon = pg.image.load(icon_picture)
    pg.display.set_icon(icon)

    def run_game(self):
        while True:
            self.display.fill('black')
            self.fractal.run()
            for event in pg.event.get():
                if event.type == pg.QUIT:
                    pg.quit()
                    quit()
            pg.display.update()
            self.clock.tick(60)


game = Game()
game.run_game()
