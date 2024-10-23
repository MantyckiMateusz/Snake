from turtle import Turtle
FONT = ('Cascadia Code', 14,  'bold')
ALLIGN = 'center'

class Scoreboard(Turtle):

    #init scoreboard on top of the screen
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color('white')
        self.hideturtle()
        self.penup()
        self.goto(0, 280)
        self.render_score()
        
    #increase score by 1 and refresh
    def increase_score(self):
        self.score += 1
        self.render_score()
    
    #clean the score from the screen and render new scoarboard with current score
    def render_score(self):
        self.clear()
        self.write(f"Score: {self.score}", False, align=ALLIGN, font=FONT)

    #show gameover screen
    def game_over(self):
        self.goto(0,0)
        self.write('GAME OVER', False, align=ALLIGN, font=FONT)