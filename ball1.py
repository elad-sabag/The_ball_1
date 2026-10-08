import pygame
import threading
import random
RADIUS = 20

def create_ball():
    while True:
        x = random.randint(RADIUS, 800 - RADIUS)
        y = random.randint(RADIUS, 600 - RADIUS)
        color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
        pygame.draw.circle(screen, color, (x, y), RADIUS)
        pygame.display.flip()

pygame.init()
screen = pygame.display.set_mode((800, 600))


balls = int(input("enter amount of balls"))

create_ball()
x = random.randint(RADIUS, 800 - RADIUS)
y = random.randint(RADIUS, 600 - RADIUS)
color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
pygame.draw.circle(screen, color, (x, y), RADIUS)
pygame.display.flip()


# threading.Thread(target=create_ball, daemon=True).start()
# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#
#     for ball in range(balls):
#         pass
#
#
#     pygame.display.flip()

pygame.quit()