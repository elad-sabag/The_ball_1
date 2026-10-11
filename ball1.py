import pygame
import threading
import random
import time

RADIUS = 20

def create_ball():
    times = random.randint(1, 10)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for i in range(times):
        x = random.randint(RADIUS, 800 - RADIUS)
        y = random.randint(RADIUS, 600 - RADIUS)
        pygame.draw.circle(screen, color, (x, y), RADIUS)
        pygame.display.flip()
        time.sleep(0.5)
        pygame.draw.circle(screen, (0, 0, 0), (x, y), RADIUS)
        pygame.display.flip()




balls = int(input("enter amount of balls"))
pygame.init()
screen = pygame.display.set_mode((800, 600))


threads = []
threads_closed = []
ball_num = 1
balls_alive = 0
running = True
last_created = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    now = pygame.time.get_ticks()
    if ball_num <= balls and now - last_created >= 700:
        t = threading.Thread(target=create_ball, daemon=True)
        t.start()
        balls_alive += 1
        print(f"[{t.name}] Ball created")
        threads.append(t)
        last_created = now
        ball_num += 1


    for t in threads:
        if not t.is_alive() and t not in threads_closed:
            balls_alive -= 1
            threads_closed.append(t)
            print(f"[{t.name}] Ball finished")
            print(f"balls remaining: {balls_alive}")
        if balls_alive == 0 and ball_num - 1 == balls:
            running = False





pygame.quit()