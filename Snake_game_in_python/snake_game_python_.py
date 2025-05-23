import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 600, 600
CELL_SIZE = 20
GRID_WIDTH = WIDTH // CELL_SIZE
GRID_HEIGHT = HEIGHT // CELL_SIZE

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Snake Game with Alphabet and Dynamic Background")

clock = pygame.time.Clock()
font = pygame.font.SysFont('arial', 24, bold=True)
letter_font = pygame.font.SysFont('arial', 32, bold=True)

# The phrase to display as snake eats letters
phrase = "RENISHMIRANI"
phrase_index = 0

# Colors
SNAKE_COLOR = (0, 255, 0)
FOOD_COLOR = (255, 215, 0)
TEXT_COLOR = (255, 255, 255)

def get_random_color():
    """Generate a random bright-ish color for background."""
    return (random.randint(50, 255), random.randint(50, 255), random.randint(50, 255))

# Initial background color
background_color = (0, 0, 0)

def draw_letter(letter, x, y):
    text = letter_font.render(letter, True, FOOD_COLOR)
    rect = text.get_rect(center=(x + CELL_SIZE // 2, y + CELL_SIZE // 2))
    screen.blit(text, rect)

def draw_snake(snake):
    for segment in snake:
        rect = pygame.Rect(segment[0] * CELL_SIZE, segment[1] * CELL_SIZE, CELL_SIZE, CELL_SIZE)
        pygame.draw.rect(screen, SNAKE_COLOR, rect)
        pygame.draw.rect(screen, (0, 100, 0), rect, 1)  # Border for nicer look

def draw_phrase_progress(phrase, index):
    text_surface = font.render("Collected: " + phrase[:index], True, TEXT_COLOR)
    screen.blit(text_surface, (10, HEIGHT - 30))

def main():
    global phrase_index, background_color

    snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
    direction = (0, -1)  # start moving up
    speed = 10  # initial speed

    # Place first food randomly
    food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

    running = True
    while running:
        clock.tick(speed)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP and direction != (0, 1):
                    direction = (0, -1)
                elif event.key == pygame.K_DOWN and direction != (0, -1):
                    direction = (0, 1)
                elif event.key == pygame.K_LEFT and direction != (1, 0):
                    direction = (-1, 0)
                elif event.key == pygame.K_RIGHT and direction != (-1, 0):
                    direction = (1, 0)

        # Move snake head
        new_head = (snake[0][0] + direction[0], snake[0][1] + direction[1])

        # Wrap around screen (appear from other side)
        new_head = (new_head[0] % GRID_WIDTH, new_head[1] % GRID_HEIGHT)

        # Check self collision
        if new_head in snake:
            # Game over - reset
            phrase_index = 0
            speed = 10
            snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
            direction = (0, -1)
            background_color = (0, 0, 0)
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
            continue

        snake.insert(0, new_head)

        # Check if snake eats food
        if new_head == food:
            phrase_index += 1

            # Increase speed slightly with each letter eaten
            speed = min(speed + 1, 25)

            # Change background color randomly
            background_color = get_random_color()

            # Place new food in a free cell
            while True:
                new_food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))
                if new_food not in snake:
                    food = new_food
                    break
        else:
            snake.pop()  # remove tail if not eating

        # Draw everything
        screen.fill(background_color)
        draw_snake(snake)
        if phrase_index < len(phrase):
            draw_letter(phrase[phrase_index], food[0] * CELL_SIZE, food[1] * CELL_SIZE)
        draw_phrase_progress(phrase, phrase_index)

        # Win condition: collected all letters
        if phrase_index == len(phrase):
            win_text = font.render("You completed the phrase! Congrats!", True, TEXT_COLOR)
            screen.blit(win_text, (WIDTH // 2 - win_text.get_width() // 2, HEIGHT // 2))
            pygame.display.update()
            pygame.time.wait(4000)
            # Reset game
            phrase_index = 0
            speed = 10
            snake = [(GRID_WIDTH // 2, GRID_HEIGHT // 2)]
            direction = (0, -1)
            background_color = (0, 0, 0)
            food = (random.randint(0, GRID_WIDTH - 1), random.randint(0, GRID_HEIGHT - 1))

        pygame.display.update()

if __name__ == "__main__":
    main()
