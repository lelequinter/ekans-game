from turtle import Screen, Turtle
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Ekans Game')

snake = Snake()

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

screen.exitonclick()
