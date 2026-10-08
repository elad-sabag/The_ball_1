import pygame
import threading
import random
import time

RADIUS = 20

def create_ball():
    times = random.randint(1, 7)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(times):
        x = random.randint(RADIUS, 800 - RADIUS)
        y = random.randint(RADIUS, 600 - RADIUS)
        pygame.draw.circle(screen, color, (x, y), RADIUS)
        pygame.display.flip()
        time.sleep(0.7)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), RADIUS)
        pygame.display.flip()



balls = int(input("enter amount of balls"))

pygame.init()
screen = pygame.display.set_mode((800, 600))

threads = []

for i in range(balls):
    t = threading.Thread(target=create_ball, daemon=True)
    t.start()
    threads.append(t)


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if not any(t.is_alive() for t in threads):
        running = False


pygame.quit()