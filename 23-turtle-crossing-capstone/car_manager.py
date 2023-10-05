from turtle import Turtle
import random
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_len=2)
            new_car.color(random.choice(COLORS))
            new_car.penup()
            y_pos = random.randint(-250, 250)
            new_car.goto(x=300, y=y_pos)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            if car.xcor() < -320:
                self.all_cars.remove(car)
                car.hideturtle()
            else:
                car.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT