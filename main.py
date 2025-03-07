from turtle import Screen, Turtle
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Ekans Game')

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Direction to move snake
screen.listen()
screen.onkey(snake.up, 'e')
screen.onkey(snake.down, 'd')
screen.onkey(snake.right, 'f')
screen.onkey(snake.left, 's')

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

    #Detext collision with food
    if snake.head.distance(food) < 15:
        scoreboard.increase_score()
        food.refresh()

screen.exitonclick()
