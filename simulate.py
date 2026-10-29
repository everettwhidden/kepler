import numpy as np
import pygame
from physics import step

# window setup
WIDTH, HEIGHT = 800, 800
FPS = 60

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Orbit sim")
clock = pygame.time.Clock()

R0 = np.array([1.471e11, 0.0])
V0 = np.array([0.0, 20000.0])
DT = 3600
STEPS_PER_FRAME = 10

r, v = R0, V0
trail = []

SCALE = 300 / 1.496e11   # pixels per meter (1 AU = 300 px)
steps_in_wedge = 0
STEPS_PER_WEDGE = 400

def to_screen(r):
    px = WIDTH / 2 + r[0] * SCALE
    py = HEIGHT / 2 - r[1] * SCALE
    return int(px), int(py)

running = True
while running:
    # handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # call step some number of times
    for i in range(STEPS_PER_FRAME):
        r, v = step(r, v, DT)
        if steps_in_wedge < STEPS_PER_WEDGE:
            steps_in_wedge += 1
        else:
            steps_in_wedge = 0    

    # draw
    screen.fill((0, 0, 0))
    #sun
    pygame.draw.circle(screen, (255, 200, 0), (WIDTH // 2, HEIGHT // 2), 15)

    px, py = to_screen(r)
    pygame.draw.circle(screen, (80, 150, 255), (px, py), 5)

    pygame.display.flip()
    clock.tick(FPS)

pygame.quit()