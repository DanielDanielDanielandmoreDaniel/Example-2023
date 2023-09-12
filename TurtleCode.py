"""
This code is to teach us about the SOLID method of coding.
SOLID is a programming practice that makes code more efficient, easier to modify, and easier for other people to understand
This code uses turtle to create shapes and OOP to give meaning to the two different shapes ive made.

Daniel Fraser
"""

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
    # This defines the colour and side length of the star shape
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    # This defines the actual shape
    def draw(self):
        for i in range(5):
            self.John.forward(self.side_length)
            self.John.left(144)


class BigStar(Shape):
    # This defines the colour and side length of the star shape
    def __init__(self, color, side_length):
        super().__init__(color)
        self.side_length = side_length

    # This defines the actual shape
    def draw(self):
        for i in range(15):
            self.John.forward(self.side_length)
            self.John.left(168)


# This tells the classes what to do (Draw the big star, make it blue, and every line is 200px)
Shape = BigStar("blue", 200)
Shape.draw()

turtle.exitonclick()
