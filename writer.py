import turtle
font_style = ("Arial", 18, "bold")

class Writer():
    def __init__(self) -> None:
        self.turtle = turtle.Turtle()
        self.turtle.hideturtle()
        self.turtle.color("white")
        self.turtle.penup()
        self.turtle.speed(0)

    def writeScore(self,score):
        self.turtle.clear()
        self.turtle.write(f"Score: {score}", align="left", font=font_style)