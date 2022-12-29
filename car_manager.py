from turtle import Turtle
import random

LEFT_SPAWNS = [(-300, -240), (-300, -210), (-300, -180), (-300, -150),
               (-300, 80), (-300, 110), (-300, 140), (-300, 170)]
RIGHT_SPAWNS = [(300, -90), (300, -60), (300, -30), (300, 0)]
COLORS = ["brown", "orange", "yellow", "cyan", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.left_cars = []
        self.right_cars = []
        self.move_speed = 0.1

    def move_left_cars(self):
        for car in self.left_cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def spawn_car_left(self):
        random_change = random.randint(1, 3)
        lane_is_free = True

        for car in self.left_cars:
            if car.xcor() > -250:
                lane_is_free = True
            else:
                lane_is_free = False

        if random_change == 1 and lane_is_free:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_spawn = random.choice(LEFT_SPAWNS)
            new_car.goto(random_spawn)
            self.left_cars.append(new_car)

    def move_right_cars(self):
        for car in self.right_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def spawn_car_right(self):
        random_change = random.randint(1, 6)
        lane_is_free = True

        for car in self.right_cars:
            if car.xcor() < 250:
                lane_is_free = True
            else:
                lane_is_free = False

        if random_change == 1 and lane_is_free:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_spawn = random.choice(RIGHT_SPAWNS)
            new_car.goto(random_spawn)
            self.right_cars.append(new_car)

    def increase_difficulty(self):
        self.move_speed *= 0.7


