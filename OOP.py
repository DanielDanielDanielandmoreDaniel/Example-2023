"""
OOP - (Object oriented programing) is coding around an object.
You first need to define the object and give it characteristics
You then make methods that the object can do.
This style of coding is very efficient and easy for people to follow.
OOP is also very easy to modify without breaking the entire program.
With the ability to add new and take away methods, OOP is very flexible and good for future proofing.

Daniel Fraser
"""


class Car:
    def __init__(self, color, model, year, make):
        # This is what defines the car
        self.color = color
        self.model = model
        self.year = year
        self.make = make

    # These methods print out a statement that tells the user what the car is doing
    # And which car is doing it
    def acc(self):
        return self.color, self.make, "is speeding up"

    def brake(self):
        return self.year, self.model, "is slowing down"

    def left(self):
        return self.year, self.model, "is turning left"

    def right(self):
        return self.year, self.model, "is turning right"


class SuperCar(Car):
    # This child class does everything the other class does, but when it goes forward, it does it very quickly
    def sports_mode(self):
        return self.color, "is speeding up VERY QUICKLY"


# Simply asking the user if they want an orange car, red car, or a super car
car = input("What car do you want? >> ")

# This creates the car and gives the class the attributes of the cars
if car == "1":
    Inst1 = Car(color="Orange", model="Ford", year="2022", make="Mustang")
elif car == "lrlrududaabbstart":
    Inst1 = SuperCar(color="Orange", model="Ford", year="2022", make="Mustang")
else:
    Inst1 = Car(color="Red", model="Toyota", year="2013", make="Corolla")

# This starts the car
ans = input("\nDo you want to start the car? >> ")
print(Inst1.acc())

# This loops until the user stops, and it is simply everything the car is programmed to do
while ans != "stop":
    ans = input("\nWhat next? >> ")
    if ans == "left":
        print(Inst1.left())
    elif ans == "right":
        print(Inst1.right())
    elif ans == "sport":
        print(Inst1.sports_mode())
    else:
        print(Inst1.acc())

print(Inst1.brake())
