import random
from turtle import Turtle



Colours = ["red", "orange", "yellow", "blue", "purple"]
starting_move_distance = 5
move_increment = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = move_increment

    def create_car(self):
        create_randomly = random.randint(1, 5)
        if create_randomly == 2:
            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            car.color(random.choice(Colours))
            car.setheading(180)
            random_y = random.randint(-250, 250)
            car.goto(300, random_y)
            self.all_cars.append(car)

    def move_cars(self):
        for i in self.all_cars:
            i.forward(self.car_speed)


    def level_up(self):
        self.car_speed += move_increment