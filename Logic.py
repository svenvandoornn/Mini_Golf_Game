from sprites import Ball

class Game():
    def __init__(self,screen):
        self.screen = screen
        self.player_texture_path = './Assets/Textures/Ball.png'
        self.player = Ball((0,0), 32, self.screen, self.player_texture_path)

    def __draw__(self):
        self.screen.blit(self.player.image, self.player.pos)

    def run(self):
        self.player.update()
        self.__draw__()