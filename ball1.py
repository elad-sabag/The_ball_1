import pygame
import threading
import random
import time

RADIUS = 20

def create_ball():
    times = random.randint(1, 15)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(times):
        x = random.randint(RADIUS, 800 - RADIUS)
        y = random.randint(RADIUS, 600 - RADIUS)
        pygame.draw.circle(screen, color, (x, y), RADIUS)
        pygame.display.flip()
        time.sleep(0.7)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), RADIUS)
        pygame.display.flip()

def checkAmountOfBalls(threads):
    ball_alive = 0
    for t in threads:
        if t.is_alive():
            ball_alive += 1
    return ball_alive


balls = int(input("enter amount of balls"))

pygame.init()
screen = pygame.display.set_mode((800, 600))

threads = []

for i in range(balls):
    t = threading.Thread(target=create_ball, daemon=True)
    t.start()
    threads.append(t)


running = True
alive = balls
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    balls_alive = checkAmountOfBalls(threads)
    if alive != balls_alive:
        alive = balls_alive
        if alive == 0:
            running = False
        else:
            print(f"balls remaining: {alive}")



pygame.quit()