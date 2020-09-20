import pygame, sys



class main_game:

    def new_window(self):
        pygame.init()
        red = (255, 0, 0)
        game = pygame.display.set_mode((800, 800))
        
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()

            pygame.display.update()