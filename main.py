import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard


screen = Screen()
screen.setup(width=600, height=600)
screen.title("Turtle Roads")
screen.tracer(0)

scoreboard = Scoreboard()

player = Player()
car_manager = CarManager()

screen.listen()

screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")
screen.onkeypress(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.spawn_car_left()
    car_manager.move_left_cars()
    car_manager.spawn_car_right()
    car_manager.move_right_cars()

    if player.ycor() > 280:
        player.reset_position()
        scoreboard.next_level()
        car_manager.increase_difficulty()

    for car in car_manager.left_cars:
        if car.distance(player.pos()) < 20:
            player.game_over()
            scoreboard.game_over()
            game_is_on = False

    for car in car_manager.right_cars:
        if car.distance(player.pos()) < 20:
            player.game_over()
            scoreboard.game_over()
            game_is_on = False


screen.update()

screen.exitonclick()
