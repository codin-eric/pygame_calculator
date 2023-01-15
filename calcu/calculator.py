import pygame
from helpers import draw_text
from constants import (
    CALC_BG_IMG,
    BUTTON_IMG,
    SCREEN_RESOLUTION,
    BLACK
)


TILE_SIZE=200


class Calculator:
    def __init__(self) -> None:
        self.tile_lst = []
        self.text_size = 50
        self.image = CALC_BG_IMG
       
        img_size = self.image.get_size()

        self.pos = [
            SCREEN_RESOLUTION[0]/2 - img_size[0]/2,
            SCREEN_RESOLUTION[1]/2 - img_size[1]/2]
        
        offset = [100, 300]
        btn_pos = [self.pos[0] + offset[0], self.pos[1] + offset[1]]
        self.buttons = Button(btn_pos)

    def check_btn_press(self, mouse_pos) -> None:
        self.buttons.btn_press(mouse_pos)

    def draw(self, screen) -> None:
        screen.blit(self.image, self.pos)
        self.buttons.draw(screen)


class Button:
    def __init__(self, pos) -> None:
        self.tile_lst = []
        self.text_size = 150
        self.image = pygame.transform.scale(
            BUTTON_IMG, (TILE_SIZE, TILE_SIZE)
        )
        self.img_size = self.image.get_size()

        self.pos = pos
        self.txt_pos = [pos[0] + self.img_size[0] / 2 - self.text_size/4,
                        pos[1] + self.img_size[1] / 2 - self.text_size/4,]

    def btn_press(self, mouse_pos) -> None:
        # self.image.rect.collidepoint(x, y)
        
        if (self.pos[0] + self.img_size[0]) > mouse_pos[0] > self.pos[0] and \
           (self.pos[1] + self.img_size[1]) > mouse_pos[1] > self.pos[1]:
            print('press!')

    def draw(self, screen) -> None:
        screen.blit(self.image, self.pos)
        draw_text(screen, '7', self.text_size, BLACK, self.txt_pos[0], self.txt_pos[1])