import pygame
from pathlib import Path


SCREEN_RESOLUTION = (1000, 1000)

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREY = (160, 160, 160)
DARKGREY = (13, 13, 13)
RED = (200, 0, 0)
GREEN = (0, 200, 0)

BRED = (255, 0, 0)
BGREEN = (0, 255, 0)

ROOT_DIR = Path('__name__').resolve().parent

FAMILY_FONT_NAME = 'hack.ttf'
CALC_BG_IMG = pygame.image.load(ROOT_DIR / 'images/background.png')
BUTTON_IMG = pygame.image.load(ROOT_DIR / 'images/button.png')