class Sprite:
    form = ''
    x = 0
    y = 0

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def load_sprite(self, path):
        self.form = open(path).readlines()
