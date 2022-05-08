from turtle import Turtle, forward
# POSITION = [(350,0),(-350,0)]
class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.color('white')
        self.shape('square')
        self.shapesize(stretch_wid=5,stretch_len=1)
        self.penup()
        self.goto(position)
        
    def up(self):
        new_y = self.ycor() +20
        self.goto(self.xcor(),new_y)
    def down(self):
        new_y = self.ycor() -20
        self.goto(self.xcor(),new_y)




        
 # self.setheading(90)
        # self.goto(x=350,y=0)
        
    # def create_paddle(self):
    #     for position in POSITION:
    #         timmy = Turtle()
    #         timmy.penup()
    #         timmy.goto(position)
    #         timmy.color('white')
    #         timmy.shape('square')
    #         timmy.shapesize(stretch_wid=5,stretch_len=1)
    #         self.timmy_list.append(timmy)


