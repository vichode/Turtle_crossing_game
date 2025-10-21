import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

my_player = Player()
My_screen = Screen()
racing_cars = CarManager()
score = Scoreboard()


My_screen.setup(600, 600)
My_screen.title("Turtle Crossing Game")
My_screen.tracer(0)


My_screen.listen()
My_screen.onkeypress(my_player.move, "Up")

game_on = True

while game_on:
    time.sleep(0.1)
    My_screen.update()

    racing_cars.create_car()
    racing_cars.move_cars()

    #detect collision with cars
    for i in racing_cars.all_cars:
        if i.distance(my_player) < 20:
            game_on = False
            score.game_over()


    #detect successful cross
    if my_player.at_finish_line():
        my_player.goto_start()
        racing_cars.level_up()
        score.increase_level()







My_screen.exitonclick()
