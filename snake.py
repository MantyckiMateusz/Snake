from turtle import Turtle
STARTING_POSITIONS = [(0,0), (-20,0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    #Initialize first 3 segments
    def create_snake(self):
        for pos in STARTING_POSITIONS:
            self.add_segment(pos)

    #Move the first segment by MOVE_DISTANCE and all of the subsequent segments to the position of the next segment in the segments list
    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)

        self.head.forward(MOVE_DISTANCE)

    #Change direction
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    #Add segments
    def add_segment(self, postion):
        segment = Turtle()
        segment.shape('square')
        segment.color('white')
        segment.penup()
        segment.goto(postion)
        self.segments.append(segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())
