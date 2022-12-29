from turtle import Turtle

START_POSITION = (-310, -280)
SAFE_SPOTS = [(320, -280), (320, -120), (-320, -120), (-320, 40), (320, 40), (320, 200), (-320, 200), (-320, 230)]
WATER_LINE = [(320, 230), (320, 260), (-320, 260), (-320, 290), (320, 290)]


class BackGround(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.speed("fastest")
        self.pensize(30)
        self.draw_bg()

    def draw_bg(self):
        # Draws safe line between lines
        self.setposition(START_POSITION)
        self.pencolor("Coral")
        self.pendown()
        for position in SAFE_SPOTS:
            self.goto(position)
        # Draws sea line / finish line
        self.pencolor("CadetBlue1")
        for position in WATER_LINE:
            self.goto(position)

