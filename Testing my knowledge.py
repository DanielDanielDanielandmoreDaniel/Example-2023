import random


def calc():
    num1 = int(input("Pick a number >> "))
    num2 = int(input("Pick another number >> "))
    confirm = input(f"Please confirm that your two numbers are {num1} and {num2} (y/n) >> ")
    if confirm == "y":
        print(f"The sum of these two numbers are {num1 + num2}")
    else:
        calc()


def rand():
    randint = random.randint(0, 10)
    print(f"My random number is {randint}")
    ask = input("Would you like to have another random number? y/n >> ")
    if ask == "y":
        rand()
    else:
        return randint


print("Part 1: Hello World!")

print("\nPart 2:")
calc()

print("\nPart 3:")
width = int(input("What is the width? >> "))
height = int(input("What is the height? >> "))
if width == height:
    print(f"The area of your square is {width * height}")
else:
    print(f"The area of your rectangle is {width * height}")

print("\nPart 4:")
temp = int(input("What is the temperature? >> "))
if temp >= 50:
    temp1 = temp - 32
    temp1 = temp1 * 0.5556
    temp1 = int(temp1)
    print(f"You have given a Celsius temperature, in Fahrenheit {temp} is {temp1}")
elif temp >= -10:
    temp1 = temp * 1.8
    temp1 = temp1 + 32
    temp1 = int(temp1)
    print(f"You have given a Fahrenheit temperature, in Celsius {temp} is {temp1}")
else:
    print("This is not a valid temperature...")

print("\nPart 5:")
rand()

fruits_list = ["Banana", "Apple", "Kiwifruit", "Pineapple"]
colours_tuple = ("Yellow", "Red", "Green", "Purple")
food_dict = {"Pineapple": "Fruit", "Cake": "Sweet", "Carrot": "Vegetable"}
num_set = {1, 2, 3, 4, 5, 6}

print("i am screaming".upper())
