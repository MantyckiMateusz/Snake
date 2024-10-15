from turtle import Screen, Turtle
from snake import Snake
import time

#Screen config
screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.tracer(0)
screen.title('Snake Game')

#Initialize snake and update screen
snake = Snake()
screen.update()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

#Main game loop
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)

    snake.move()
    
#Keep screen from closing automaticaly
screen.exitonclick()