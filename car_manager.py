from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
# STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.starting_move_distance = 5
        self.generated_cars = [] # store the car so it persists and can be moved

    def generate_car(self):
        if random.randint(1, 6) == 1: # spanw rate
            new_car = Turtle("square")
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.goto(310, random.randint(-250, 270))
            new_car.setheading(180)
            self.generated_cars.append(new_car)

    def move_car(self):
        for car in self.generated_cars:
            car.fd(self.starting_move_distance)