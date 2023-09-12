"""
This code is simply me showing what i already know about coding before the course.
This program is a complilation of challanges that were given to the class to teach them some basic python skills and syntax.
I decided to expand on these challenges and make it interactive with the user and more advanced than was required.

Daniel Fraser
"""


import random

# This was the second challenge, i had to add 2 numbers
# I decided to make it a bit more advanced, by getting the user to input the numbers
# I even added a confirmation option if they wanted to change their numbers
def calc():
    num1 = int(input("Pick a number >> "))
    num2 = int(input("Pick another number >> "))
    confirm = input(f"Please confirm that your two numbers are {num1} and {num2} (y/n) >> ")
    if confirm == "y":
        print(f"The sum of these two numbers are {num1 + num2}")
    else:
        calc()


# This function simply generates a random number and prints it
# Again i make ti a big more complicated by asking if they wanted another one
def rand():
    randint = random.randint(0, 10)
    print(f"My random number is {randint}")
    ask = input("Would you like to have another random number? y/n >> ")
    if ask == "y":
        rand()
    else:
        return randint


# The first challenge was to print "Hello world"
print("Part 1: Hello World!")

# This is the second challenge which is all done in a function
print("\nPart 2:")
calc()

# The third challenge was to find the area of a rectange
# I made it more complicated by having the user input the numbers
print("\nPart 3:")
width = int(input("What is the width? >> "))
height = int(input("What is the height? >> "))

# I then made it even more complicated by checking if the numbers were equal (making it a sqare)
# Then changing what gets printed to show that you made a square
if width == height:
    print(f"The area of your square is {width * height}")
else:
    print(f"The area of your rectangle is {width * height}")


# The fourth challenge was to convert temperature
# To keep it consistant, i made the user input the temperature
print("\nPart 4:")
temp = int(input("What is the temperature? >> "))

# Then to make it even more complicated, i had my program check if it is above -10 or 50 
# Then assumed anything over 50 was Fahrinheight, anything over -10 was Celcius
# And any anything else was an unreasonable temperature
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

# The fifth challenge is all done in a function
print("\nPart 5:")
rand()

# Then there were some extras where you messed around with different list types
fruits_list = ["Banana", "Apple", "Kiwifruit", "Pineapple"]
colours_tuple = ("Yellow", "Red", "Green", "Purple")
food_dict = {"Pineapple": "Fruit", "Cake": "Sweet", "Carrot": "Vegetable"}
num_set = {1, 2, 3, 4, 5, 6}

print("i am screaming".upper())
