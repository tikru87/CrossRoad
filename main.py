import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from background import BackGround

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
GAME_TITLE = "Turtle Roads"
BACKGROUND_COLOR = "gray"
GOAL_LINE = 280
COLLISION_DISTANCE = 25


screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.title(GAME_TITLE)
screen.bgcolor(BACKGROUND_COLOR)
screen.tracer(0)

background = BackGround()
scoreboard = Scoreboard()

player = Player()
car_manager = CarManager()

screen.listen()

screen.onkey(player.move_up, "w")

game_is_on = True
while game_is_on:
    time.sleep(car_manager.move_speed)
    screen.update()
    car_manager.spawn_car_left()
    car_manager.move_left_cars()
    car_manager.spawn_car_right()
    car_manager.move_right_cars()

    if player.ycor() > GOAL_LINE:
        player.reset_position()
        scoreboard.next_level()
        car_manager.increase_difficulty()

    for car in car_manager.left_cars:
        if car.distance(player.pos()) < COLLISION_DISTANCE:
            player.game_over()
            scoreboard.game_over()
            game_is_on = False

    for car in car_manager.right_cars:
        if car.distance(player.pos()) < COLLISION_DISTANCE:
            player.game_over()
            scoreboard.game_over()
            game_is_on = False


screen.update()

screen.exitonclick()
