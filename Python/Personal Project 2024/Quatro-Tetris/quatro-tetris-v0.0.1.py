# Imported modules
import pygame
import random
import time

# Game constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
BLOCK_SIZE = 40
FPS = 60
BG_COLOR = (255, 255, 255)  # White

# Tetromino shapes
SHAPES = [
    [[1]],
    [[1, 1, 1, 1]],
    [[1, 1], [1, 1]],
    [[1, 1, 1], [0, 1, 0]],
    [[1, 1, 1], [1, 0, 0]],
    [[1, 1, 1], [0, 0, 1]],
    [[1, 1, 0], [0, 1, 1]]
]

# Define colors for each tetromino shape
SHAPE_COLORS = [
    (255, 0, 0),    # Red
    (0, 255, 0),    # Green
    (0, 0, 255),    # Blue
    (255, 0, 255),  # Magenta
    (255, 255, 0),  # Yellow
    (0, 255, 255),  # Cyan
    (255, 165, 0)   # Orange
]

# Game easter eggs
EASTER_EGGS = {
    69: "Nice Number",
    690: "Nice Number",
    13: "Death",
    130: "Death",
    2023: "Thanks for playing"
}

class Tetromino:
    def __init__(self, shape, color, x, y):
        self.shape = shape
        self.color = color
        self.x = x
        self.y = y

    def rotate(self):
        self.shape = list(zip(*reversed(self.shape)))

    def move_left(self):
        self.x -= 1

    def move_right(self):
        self.x += 1

    def move_down(self):
        self.y += 1

    def draw(self, screen):
        for i in range(len(self.shape)):
            for j in range(len(self.shape[i])):
                if self.shape[i][j]:
                    pygame.draw.rect(
                        screen,
                        self.color,
                        (self.x * BLOCK_SIZE + j * BLOCK_SIZE,
                         self.y * BLOCK_SIZE + i * BLOCK_SIZE,
                         BLOCK_SIZE,
                         BLOCK_SIZE)
                    )

def generate_random_tetromino():
    shape = random.choice(SHAPES)
    color = random.choice(SHAPE_COLORS)
    return Tetromino(shape, color, 4, 0)

def check_collision(tetromino, grid):
    for i in range(len(tetromino.shape)):
        for j in range(len(tetromino.shape[i])):
            if tetromino.shape[i][j] and (tetromino.y + i >= SCREEN_HEIGHT // BLOCK_SIZE or
                                          tetromino.x + j < 0 or tetromino.x + j >= SCREEN_WIDTH // BLOCK_SIZE or
                                          grid[tetromino.y + i][tetromino.x + j]):
                return True
    return False

def clear_lines(grid):
    lines_cleared = 0
    for i in range(len(grid)):
        if all(grid[i]):
            del grid[i]
            grid.insert(0, [0] * (SCREEN_WIDTH // BLOCK_SIZE))
            lines_cleared += 1
    return lines_cleared

def draw_grid(screen, grid):
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j]:
                pygame.draw.rect(
                    screen,
                    grid[i][j],
                    (j * BLOCK_SIZE, i * BLOCK_SIZE, BLOCK_SIZE, BLOCK_SIZE)
                )

def show_title_screen(screen):
    title_font = pygame.font.SysFont(None, 64)
    title_text = title_font.render("Quatro Tetris", True, (0, 0, 0))
    start_font = pygame.font.SysFont(None, 32)
    start_text = start_font.render("Press Space to Start", True, (0, 0, 0))
    screen.blit(title_text, (SCREEN_WIDTH // 2 - title_text.get_width() // 2, 200))
    screen.blit(start_text, (SCREEN_WIDTH // 2 - start_text.get_width() // 2, 300))

def show_end_screen(screen, score, time_played):
    end_font = pygame.font.SysFont(None, 64)
    score_text = end_font.render("Score: " + str(score), True, (0, 0, 0))
    time_played_text = end_font.render("Time Played: " + time_played + "s", True, (0, 0, 0))
    restart_text = end_font.render("Press Space to Play Again", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))
    screen.blit(time_played_text, (SCREEN_WIDTH // 2 - time_played_text.get_width() // 2, 300))
    screen.blit(restart_text, (SCREEN_WIDTH // 2 - restart_text.get_width() // 2, 400))

def show_pause_screen(screen, score):
    pause_font = pygame.font.SysFont(None, 64)
    score_text = pause_font.render("Score: " + str(score), True, (0, 0, 0))
    easter_egg_text = pause_font.render(EASTER_EGGS.get(score, ""), True, (0, 0, 0))
    resume_text = pause_font.render("Press Space to Resume", True, (0, 0, 0))
    screen.blit(score_text, (SCREEN_WIDTH // 2 - score_text.get_width() // 2, 200))
    screen.blit(easter_egg_text, (SCREEN_WIDTH // 2 - easter_egg_text.get_width() // 2, 300))
    screen.blit(resume_text, (SCREEN_WIDTH // 2 - resume_text.get_width() // 2, 400))

def play_game():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Quatro Tetris")

    clock = pygame.time.Clock()

    is_running = False
    is_paused = False

    time_start = time.time()
    score = 0
    time_played = 0

    grid = [[0] * (SCREEN_WIDTH // BLOCK_SIZE) for _ in range(SCREEN_HEIGHT // BLOCK_SIZE)]

    current_tetromino = generate_random_tetromino()
    next_tetromino = generate_random_tetromino()

    move_timer = 0.0

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if is_running:
                        is_paused = not is_paused
                    elif not is_paused:
                        is_running = True

        if is_running and not is_paused:
            keys = pygame.key.get_pressed()
    
            if keys[pygame.K_LEFT]:
                current_tetromino.move_left()
                if check_collision(current_tetromino, grid):
                    current_tetromino.move_right()
    
            if keys[pygame.K_RIGHT]:
                current_tetromino.move_right()
                if check_collision(current_tetromino, grid):
                    current_tetromino.move_left()
    
            if keys[pygame.K_DOWN]:
                current_tetromino.move_down()
                if check_collision(current_tetromino, grid):
                    current_tetromino.move_up()
    
            if keys[pygame.K_UP]:
                current_tetromino.rotate()
                if check_collision(current_tetromino, grid):
                    current_tetromino.rotate()

            if move_timer >= 1.0:
                move_timer = 0.0
                
                current_tetromino.move_down()
                if check_collision(current_tetromino, grid):
                    current_tetromino.move_up()

                    for i in range(len(current_tetromino.shape)):
                        for j in range(len(current_tetromino.shape[i])):
                            if current_tetromino.shape[i][j]:
                                grid[current_tetromino.y + i][current_tetromino.x + j] = current_tetromino.color

                    lines_cleared = clear_lines(grid)
                    score += lines_cleared * int(time_played * 5)

                    current_tetromino = next_tetromino
                    next_tetromino = generate_random_tetromino()

                    if check_collision(current_tetromino, grid):
                        is_running = False
                        is_paused = False
                        time_played = round(time.time() - time_start)
                        show_end_screen(screen, score, str(time_played))
                        pygame.display.flip()
                        continue

            move_timer += clock.get_rawtime() / 1000.0
            clock.tick(FPS)

        screen.fill(BG_COLOR)
        
        draw_grid(screen, grid)
        current_tetromino.draw(screen)

        if is_paused:
            show_pause_screen(screen, score)
        elif not is_running:
            show_title_screen(screen)
            
        pygame.display.flip()

play_game()