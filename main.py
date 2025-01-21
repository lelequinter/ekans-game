from turtle import Screen, Turtle
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.bgcolor('black')
screen.title('Ekans Game')

snake_body = []

segments = []

# Creating snake body
for index in range(3):
    new_segment = Turtle('square')
    new_segment.penup()

    new_segment.color('white')
    x_position = (20 * index) * (-1)
    new_segment.goto(x_position, 0)
    segments.append(new_segment)

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)

    for seg_num in range(len(segments)-1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)

    segments[0].forward(20)

screen.exitonclick()
