from sprite import Sprite

class Map:
    WIDTH, HEIGHT = (80, 30)
    sprites = []
    origin = [0,0]

    def __init__(self):
        for i in HEIGHT:
            self.view[i] = ' ' * WIDTH

    def x_range(self):
        return (self.origin[0] - WIDTH/2, self.origin[0] + WIDTH/2)

    def y_range(self):
        return (self.origin[1] - HEIGHT/2, self.origin[1] + HEIGHT/2)

    def draw_sprite(self, sprite):
        x_min, x_max = self.x_range()
        y_min, y_max = self.y_range()
        if sprite.x in range(x_min,x_max) and sprite.y in range(y_min,y_max):
            for i, line in enumerate(sprite.form):

    def draw_map(self,x,y,width,height):
