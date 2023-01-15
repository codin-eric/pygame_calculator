import pygame
from calculator import Calculator
from constants import (
    SCREEN_RESOLUTION,
    DARKGREY,
)


pygame.init()
screen = pygame.display.set_mode(SCREEN_RESOLUTION)
pygame.display.set_caption('garden')
clock = pygame.time.Clock()


def quitgame() -> None:
    pygame.quit()
    quit()


def main() -> None:
    calcu = Calculator()

    while True:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    quitgame()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos
                calcu.check_btn_press(mouse_pos)

        # Draw
        screen.fill(DARKGREY)
        calcu.draw(screen)

        pygame.display.update()
        clock.tick(60)


if __name__ == "__main__":
    main()
