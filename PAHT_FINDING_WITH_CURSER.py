import pygame
WHITE_COLOER = ()



width = 500
pygame.display.set_mode((width, width))
def main():
    run = True
    while run:
        for evn in pygame.event.get():
            if evn.type == pygame.QUIT:
                run = False

    pygame.quit()
main()