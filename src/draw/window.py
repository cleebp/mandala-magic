"""window.py

PyGame drawing reference:
- (0, 0) Upper Left
- (0, SCREEN_HEIGHT) Lower Left
- (SCREEN_WIDTH, 0) Upper Right
- (SCREEN_WIDTH, SCREEN_HEIGHT) Lower Right
"""
from pygame import font, display

from config import BLACK, WHITE, SCREEN_WIDTH, SCREEN_HEIGHT


class Window:

    def __init__(self, screen, clock):
        self.screen = screen
        self.width = SCREEN_WIDTH
        self.height = SCREEN_HEIGHT

        # for fps counter
        self.font = font.Font(None, 30)
        self.clock = clock

    def update(self):
        self.screen.fill(BLACK)

    def draw(self):
        self.update()
        self._draw_fps()  # draw last

    def _draw_fps(self):
        self.clock.tick(24)
        fps = self.font.render(str(int(self.clock.get_fps())), True, WHITE)
        self.screen.blit(fps, (self.width - 50, 25))  # 25px down, 50px from right edge
        display.flip()
