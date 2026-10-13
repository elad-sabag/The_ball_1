import queue

import pygame
import threading
import random
import time

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
RADIUS = 20
BLACK = (0, 0, 0)
MAX_MOVES = 19
MOVE_DELAY_SECONDS = 0.5
CREATION_INTERVAL_MS = 700


def run_ball():
    moves_count = random.randint(1, MAX_MOVES)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(moves_count):
        x = random.randint(RADIUS, SCREEN_WIDTH - RADIUS)
        y = random.randint(RADIUS, SCREEN_HEIGHT - RADIUS)
        pygame.draw.circle(screen, color, (x, y), RADIUS)
        pygame.display.flip()
        time.sleep(MOVE_DELAY_SECONDS)
        pygame.draw.circle(screen, BLACK, (x, y), RADIUS)
        pygame.display.flip()

def run_ball2(q):
    name = threading.current_thread().name
    moves_count = random.randint(1, MAX_MOVES)
    color = (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))
    for _ in range(moves_count):
        x = random.randint(RADIUS, SCREEN_WIDTH - RADIUS)
        y = random.randint(RADIUS, SCREEN_HEIGHT - RADIUS)
        q.put((name, x, y, color))
        time.sleep(MOVE_DELAY_SECONDS)


total_balls = int(input("Enter amount of balls: "))
pygame.init()
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

threads = []
finished_threads = []
created_count = 0
active_count = 0
last_creation_time = 0
running = True
ball_updates = queue.Queue()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # current_time = pygame.time.get_ticks()
    if created_count < total_balls: #and current_time - last_creation_time >= CREATION_INTERVAL_MS:
        thread = threading.Thread(target=run_ball, daemon=True).start()
        threads.append(thread)
        created_count += 1
        active_count += 1
        # last_creation_time = current_time
        print(f"[{thread.name}] Ball created")

    for thread in threads:
        if not thread.is_alive() and thread not in finished_threads:
            finished_threads.append(thread)
            active_count -= 1
            print(f"[{thread.name}] Ball finished")
            print(f"Active balls: {active_count}")

    if created_count == total_balls and active_count == 0:
        running = False

pygame.quit()