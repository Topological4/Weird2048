import pygame
import sys

pygame.init()

# Screen dimensions
SCREEN_WIDTH = 640
SCREEN_HEIGHT = 480
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Pacman Game")

WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)

class Node(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(YELLOW)
        self.rect = self.image.get_rect(center=(x, y))

nodes = [
    Node(50, 50),
    Node(100, 50),
    Node(150, 50),
    Node(200, 50),
    Node(250, 50),
    Node(300, 50),
    Node(350, 50),
    Node(400, 50),
    Node(450, 50),
    Node(500, 50),
    Node(550, 50),
    Node(600, 50),
    Node(50, 100),
    Node(100, 100),
    Node(150, 100),
    Node(200, 100),
    Node(250, 100),
    Node(300, 100),
    Node(350, 100),
    Node(400, 100),
    Node(450, 100),
    Node(500, 100),
    Node(550, 100),
    Node(600, 100),
    Node(50, 150),
    Node(100, 150),
    Node(150, 150),
    Node(200, 150),
    Node(250, 150),
    Node(300, 150),
    Node(350, 150),
    Node(400, 150),
    Node(450, 150),
    Node(500, 150),
    Node(550, 150),
    Node(600, 150),
    Node(50, 200),
    Node(100, 200),
    Node(150, 200),
    Node(200, 200),
    Node(250, 200),
    Node(300, 200),
    Node(350, 200),
    Node(400, 200),
    Node(450, 200),
    Node(500, 200),
    Node(550, 200),
    Node(600, 200),
    Node(50, 250),
    Node(100, 250),
    Node(150, 250),
    Node(200, 250),
    Node(250, 250),
    Node(300, 250),
    Node(350, 250),
    Node(400, 250),
    Node(450, 250),
    Node(500, 250),
    Node(550, 250),
    Node(600, 250),
    Node(50, 300),
    Node(100, 300),
    Node(150, 300),
    Node(200, 300),
    Node(250, 300),
    Node(300, 300),
    Node(350, 300),
    Node(400, 300),
    Node(450, 300),
    Node(500, 300),
    Node(550, 300),
    Node(600, 300),
]

class Pacman(pygame.sprite.Sprite):
    def __init__(self, nodes):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill(WHITE)
        self.rect = self.image.get_rect(center=(nodes[0].rect.centerx, nodes[0].rect.centery))
        self.nodes = nodes
        self.current_node_index = 0

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_UP]:
            self.move(0, -1)
        elif keys[pygame.K_DOWN]:
            self.move(0, 1)
        elif keys[pygame.K_LEFT]:
            self.move(-1, 0)
        elif keys[pygame.K_RIGHT]:
            self.move(1, 0)

    def move(self, dx, dy):
        new_node_index = self.current_node_index + dx + dy * 2
        if 0 <= new_node_index < len(self.nodes):
            self.current_node_index = new_node_index
            self.rect.centerx = self.nodes[self.current_node_index].rect.centerx
            self.rect.centery = self.nodes[self.current_node_index].rect.centery

pacman = Pacman(nodes)
all_sprites = pygame.sprite.Group(nodes, pacman)

clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    all_sprites.update()

    screen.fill((0, 0, 0))
    all_sprites.draw(screen)
    pygame.display.flip()

    clock.tick(60)

pygame.quit()
sys.exit()
