class Sprite:
    form = ''
    x = 0
    y = 0
    
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def load_sprite(self, path):
        self.form = open(path).readlines()

tree1 = Sprite(10,2)
print(tree1.form)

tree1.load_sprite('/Users/selinaveng/Documents/jakobiamedjakob/Jakobia/sprites/tree.txt')

for line in tree1.form:
    print(line)
print(tree1.form)
