import pygame

class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, size, row, col):
        super().__init__()
        self.image = pygame.Surface((size, size))
        self.image.fill((9, 99, 126))
        self.rect = self.image.get_rect(topleft=(x, y))

        self.row = row
        self.col = col
        self.value = 0  # 0 empty, 1 X, -1 O

    def update(self):
        pass
