class Car:
    def __init__(self, color, model, year, make):
        self.color = color
        self.model = model
        self.year = year
        self.make = make

    def acc(self):
        return self.color, self.make, "is speeding up"

    def brake(self):
        return self.year, self.model, "is slowing down"

    def left(self):
        return self.year, self.model, "is turning left"

    def right(self):
        return self.year, self.model, "is turning right"


class SuperCar(Car):
    def sports_mode(self):
        return self.color, "is speeding up VERY QUICKLY AAAAAAAAAAAAAAAAAAAH"


car = input("What car do you want? >> ")

if car == "1":
    Inst1 = Car(color="Orange", model="Ford", year="2022", make="Mustang")
elif car == "lrlrududaabbstart":
    Inst1 = SuperCar(color="Orange", model="Ford", year="2022", make="Mustang")
else:
    Inst1 = Car(color="Red", model="Toyota", year="2013", make="Corolla")

ans = input("\nDo you want to start the car? >> ")
print(Inst1.acc())

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
