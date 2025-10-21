from idlelib.debugobj_r import remote_object_tree_item
from turtle import Turtle

starting_position = (0, -280)
move_distance = 10
finish_line= 280




class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.shape("turtle")
        self.penup()
        self.goto_start()
        self.setheading(90)
        self.showturtle()
        
    def move(self):
        new_y = self.ycor() + move_distance
        self.goto(0, new_y)

    def at_finish_line(self):
        if self.ycor() > finish_line:
            return True
        else:
            return False

    def goto_start(self):
        self.goto(starting_position)
