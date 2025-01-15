from turtle import Screen, Turtle

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title('Ekans Game')

snake_body = []

# Creating snake body
for index in range(3):
    new_segment = Turtle('square')
    new_segment.color('white')
    x_position = (20 * index) * (-1)
    new_segment.goto(x_position, 0)




screen.exitonclick()