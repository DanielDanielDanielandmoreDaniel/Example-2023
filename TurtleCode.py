import turtle


# Parent/High Level
class Shape:
    def __init__(self, color):
        self.John = turtle.Turtle()
        self.John.color(color)

    def draw(self):
        pass


# Child/Low level
# Each of these functions have their own job
class Star(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        for i in range(5):
            self.John.forward(self.side_length)
            self.John.left(144)


class BigStar(Shape):
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    def draw(self):
        for i in range(15):
            self.John.forward(self.side_length)
            self.John.left(168)


Shape = BigStar("blue", 200)
Shape.draw()

turtle.exitonclick()
