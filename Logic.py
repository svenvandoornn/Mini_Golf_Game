from sprites import Ball

class Game():
    def __init__(self,screen):
        self.screen = screen
        self.player = Ball((0,0), 32, self.screen)

    def __draw__(self):
        self.screen.blit(self.player.image, self.player.pos)

    def run(self):
        self.player.update()
        self.__draw__()