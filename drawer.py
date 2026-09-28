import turtle
class Drawer():
    def __init__(self,cords) -> None:
        
        self.x,self.y = cords
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.color("red")
        self.turtle.penup()
        self.turtle.speed(0)
        self.turtle.goto(self.x,self.y)

    def drawCircle(self,size):
        self.turtle.begin_fill()
        self.turtle.circle(size)
        self.turtle.end_fill()
        self.turtle.goto(self.x,self.y+size)