from turtle import Turtle

# STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_pos = (0, -280) # (x, y)
        self.move_distance = 10
        self.create_player()

    def create_player(self):
        self.shape("turtle")
        self.up()
        self.goto(self.starting_pos)
        self.setheading(90)

    def move_up(self):
        self.fd(self.move_distance)