import pygame
from Utils import load_texture
from levels import *

class Tile(pygame.sprite.Sprite):
    def __init__(self, pos, size):
        super().__init__()
        self.image = pygame.Surface((size,size))
        self.image.fill('white')
        self.rect = self.image.get_rect(topleft = pos)

class Ball(pygame.sprite.Sprite):
    def __init__(self, pos, size, screen, TexturePath):
        super().__init__()
        self.image = load_texture(TexturePath)
        self.rect = self.image.get_rect(topleft = pos)
        self.direction = pygame.math.Vector2(0, 0)
        self.pos = (self.rect.x, self.rect.y)
        self.screen = screen
        self.speed = 15
        self.semi_speedX = 0
        self.semi_speedY = 0
        self.max_speed = 25
        self.m = True

        self.Tiles = pygame.sprite.Group()
        for row_index,row in enumerate(level_1):
            for collumn_index,collumn in enumerate(row):
                print(collumn)
                if collumn == 'X':
                    self.Tiles.add(Tile((collumn_index * 64, row_index * 64), 64))


    def __update_x__(self):
        self.rect.x += self.direction.x * self.semi_speedX
        if self.direction.x > 0:
            self.direction.x -= 0.0250000000000000
        if self.direction.x < 0:
            self.direction.x += 0.0250000000000000

        if self.direction.x > -0.0250000000000000 and self.direction.x < 0.0250000000000000:
            self.direction.x = 0
        if self.direction.x == 0:
            self.semi_speedX = 0
        
        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.semi_speedX < 0:
                    self.rect.left = sprite.rect.right
                    self.semi_speedX -= self.semi_speedX * 2
                elif self.semi_speedX > 0:
                    self.rect.right = sprite.rect.left
                    self.semi_speedX -= self.semi_speedX * 2
        
    def __update_y__(self):
        self.rect.y += self.direction.y * self.semi_speedY

        if self.direction.y > 0:
            self.direction.y -= 0.0250000000000000
        if self.direction.y < 0:
            self.direction.y += 0.0250000000000000

        if self.direction.y > -0.0250000000000000 and self.direction.y < 0.0250000000000000:
            self.direction.y = 0
        if self.direction.y == 0:
            self.semi_speedY = 0

        for sprite in self.Tiles.sprites():
            if sprite.rect.colliderect(self.rect):
                if self.semi_speedY < 0:
                    self.rect.top = sprite.rect.bottom
                    self.semi_speedY -= self.semi_speedY * 2
                elif self.semi_speedY > 0:
                    self.rect.bottom = sprite.rect.top
                    self.semi_speedY -= self.semi_speedY * 2
                elif self.semi_speedX == 0 and self.semi_speedY == 0:
                    while sprite.rect.colliderect(self.rect):
                        self.rect.bottom -= 64
                    

    def __get_input__(self):
        #print((self.direction.x, self.direction.x))
        if not self.direction.x == 0 or not self.direction.y == 0:
            return
        keys = pygame.key.get_pressed()
        LeftMouse,MiddleMouse,RightMouse = pygame.mouse.get_pressed()


        if LeftMouse and self.m:
            self.direction.x = 2
            self.direction.y = 2
            self.m = False
            MouseX,MouseY = pygame.mouse.get_pos()
            Difference_X,Difference_Y = (MouseX - self.rect.x, MouseY - self.rect.y)
            Difference_Y = -round(Difference_Y / self.speed)
            Difference_X = -round(Difference_X / self.speed)
            if Difference_X < 0:
                if Difference_X < -self.max_speed:
                    Difference_X = -self.max_speed
            else:
                if Difference_X > self.max_speed:
                    Difference_X = self.max_speed
            if Difference_Y < 0:
                if Difference_Y < -self.max_speed:
                    Difference_Y = -self.max_speed
            else:
                if Difference_Y > self.max_speed:
                    Difference_Y = self.max_speed
            
            self.semi_speedX = Difference_X
            self.semi_speedY = Difference_Y

            
        elif not LeftMouse and not self.m:
            self.m = True
    
    def __CollideEdge__(self):
        if self.rect.x < 0:
            self.rect.x = 0
            self.direction.x -= self.direction.x * 2
        if self.rect.y < 0:
            self.rect.y = 0
            self.direction.y -= self.direction.y * 2
        if self.rect.x + 32 > 512:
            self.rect.x = 512 - 32
            self.direction.x -= self.direction.x * 2
        if self.rect.y + 32 > 768:
            self.rect.y = 768 - 31
            self.direction.y -= self.direction.y * 2

    def update(self):
        #print(((self.direction.x, self.direction.y), self.pos))
        self.__get_input__()
        self.__update_x__()
        self.__update_y__()
        self.__CollideEdge__()
        self.pos = (self.rect.x, self.rect.y)
        self.Tiles.draw(self.screen)
