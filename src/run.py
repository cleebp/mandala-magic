"""
lets try to paint a mandala

following: https://mathematica.stackexchange.com/questions/136974/code-that-generates-a-mandala
"""
from time import sleep

import pygame
from pygame.locals import *

from draw.window import Window
from config import SCREEN_WIDTH, SCREEN_HEIGHT


class Driver:
    def __init__(self):
        self._running = True
        self.window = None
        self.on_init()

    def on_init(self):
        pygame.init()
        pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT), pygame.DOUBLEBUF)
        pygame.display.set_caption('Mandala Magic')
        self.window = Window(pygame.display.get_surface(), pygame.time.Clock())
        self._running = True

    def on_event(self, event):
        if event.type == pygame.QUIT:
            self._running = False

    def on_loop(self):
        pass

    def on_render(self):
        self.window.draw()

    def on_cleanup(self):
        pygame.quit()

    def on_execute(self):
        while self._running:
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()


if __name__ == "__main__":
    driver = Driver()
    driver.on_execute()
