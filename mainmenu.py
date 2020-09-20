import pygame
import sys
import pygame_widgets as pw
import os
from main import main_game


game1 = main_game()
os.environ['SDL_VIDEO_CENTERED'] = '1'
pygame.mixer.init()


pygame.init()

display_width = 480
display_height = 600
# Loading Screen
background = pygame.image.load("img1.png")

screen = pygame.display.set_mode((display_width, display_height))
running = True
pygame.display.set_caption("Kaleb's game")

black = (0, 0, 0)
white = (255, 255, 255)
pygame.mixer_music.set_volume(0.7)
pygame.mixer_music.load("L'indecis - Soulful.mp3")
pygame.mixer_music.play()

def resume():
    pygame.mixer_music.unpause()


def pause_music():
    if pygame.mixer.music.get_busy():
        pygame.mixer.music.pause()


characterImg = pygame.image.load("person.png")
button = pw.Button(
    screen, 100, 100, 300, 150, text="Play",
    fontSize=50, margin=20,
    inactiveColour=(0, 255, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: game1.new_window()
)
button1 = pw.Button(
    screen, 100, 300, 300, 150, text="Quit",
    fontSize=50, margin=20,
    inactiveColour=(250, 0, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: sys.exit()
)
button2 = pw.Button(
    screen, 300, 20, 150, 75, text="Resume Music",
    fontSize=25, margin=20,
    inactiveColour=(125, 0, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: resume()
)
button3 = pw.Button(
    screen, 50, 20, 150, 75, text="Pause Music",
    fontSize=25, margin=20,
    inactiveColour=(125, 0, 0),
    pressedColour=(0, 255, 0), radius=20,
    onClick=lambda: pause_music()
)


def car(x1, y1):
    screen.blit(characterImg, (x1, y1))


x = (display_width * 0.45)
y = (display_height * 0.8)
x_change = 0
y_change = 0

while True:
    mouse = pygame.mouse.get_pos()
    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x_change = -5
            elif event.key == pygame.K_RIGHT:
                x_change = 5
            elif event.key == pygame.K_UP:
                y_change = -5
            elif event.key == pygame.K_DOWN:
                y_change = 5
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                x_change = 0
            if event.key == pygame.K_DOWN or event.key == pygame.K_UP:
                y_change = 0

    x += x_change
    y += y_change

    screen_rect = screen.get_rect()
    rect_center = screen_rect.center
    screen.blit(background, (0, 0))
    button.listen(events)
    button.draw()
    button1.listen(events)
    button1.draw()
    button2.listen(events)
    button2.draw()
    button3.listen(events)
    button3.draw()
    pygame.display.update()
