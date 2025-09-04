import pygame
import sys
import random

pygame.init()

# Screen setup
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circuit Builder Game")

clock = pygame.time.Clock()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

class Resistor(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((60, 20))
        self.image.fill((200, 100, 100))
        self.rect = self.image.get_rect(center=(x, y))

all_sprites = pygame.sprite.Group()
resistor = Resistor(WIDTH // 2, HEIGHT // 2)
all_sprites.add(resistor)

# sounds (basic)
def play_sound():
    freq = random.randint(200, 1000)
    duration = 200  # milliseconds
    sound = pygame.mixer.Sound(buffer=pygame.sndarray.make_sound(
        pygame.surfarray.array2d(pygame.Surface((1, 1)))
    ))
    sound.play()

# loop
running = True
while running:
    screen.fill(WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            play_sound()

    all_sprites.draw(screen)

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
sys.exit()