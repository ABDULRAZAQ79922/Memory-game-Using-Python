import pygame
import random

# Initialize Pygame
pygame.init()

# Constants
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
GRID_SIZE = 4
TILE_SIZE = SCREEN_WIDTH // GRID_SIZE
FPS = 30

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Set up the display
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Memory Game")

# Clock
clock = pygame.time.Clock()

# Load images
def load_images():
    images = []
    for i in range(1, 9):
        img = pygame.image.load(f'images/img{i}.png')
        img = pygame.transform.scale(img, (TILE_SIZE, TILE_SIZE))
        images.append(img)
    return images

images = load_images()
