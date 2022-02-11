# poor man's world / level here
actors = []

def add_actor(actor):
    actors.append(actor)


# global game update function
def update():
    for actor in actors:
       actor.update()


# global game draw function
def draw():
    screen.clear()

    for actor in actors:
        actor.draw()

# fancy cat class
class Cat(Actor):
    def __init__(self):
        super(Cat, self).__init__("cat")

    def update(self):
        self.x += 3

# init the game
def init():
    cat = Cat()
    add_actor(cat)

init()
