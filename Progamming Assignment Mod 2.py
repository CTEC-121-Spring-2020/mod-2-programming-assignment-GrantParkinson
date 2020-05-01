"""
CTEC 121
<Grant Parkison>
<Mod 2 Programming Assignment>
<assignment/lab description>
"""

""" IPO template
Input(s): list/description
Process: description of what function does
Output: return value and description
"""




from math import *
def main():

    # Section 1
    print("Section 1", end="\n\n")
    myInt = 3
    myString = "The sum of "
    myFloat = .56
    print(myString,  myInt, " and ",  myFloat,
          " is ", myInt + myFloat, ".", sep="")
    print()
    print("-----------------------------------------------------")

    # Section 2
    print("Section 2", end="\n\n")
    print("4", "30", "2020", sep="/", end="\n\n")
    print("-----------------------------------------------------")

    # Section 3
    print("Section 3", end="\n\n")
    print("The current date is 4\\30\\2020")
    print("Aristotle famously said \"We are what we repeatedly do. Excellence, then, is not an act, but a habit.\".")
    print("270\t220\t550", end="\n")
    print("-----------------------------------------------------")

    # Section 4
    print("Section 4", end="\n\n")
    food_input = input("Enter the name of your favorite food: ")
    print("Your favorite food is", food_input)
    print(type(food_input))
    print()

    # using the int command before my input ensures that the program will only run if an interger is the input.
    age_input = int(input("enter in your current age in years: "))
    print("Your current age is", age_input)
    print(type(age_input))
    print()

    # Using the float command before my input makes it so the program will not accept strings as a valid input and it will convert regular ints into floats
    gpa_input = float(input("Input your current GPA: "))
    print("Your current GPA is", gpa_input)
    print(type(gpa_input))
    print()

   # A string input would not be accepted by this program, using 1/2 to indicate a half size will also not be accepted
    shoe_size = eval(input("What is your shoe size(use .5 instead of 1/2): "))
    print("Your shoe size is", shoe_size)
    print(type(shoe_size))
    print("-----------------------------------------------------")

    # Section 5
    print("Section 5", end="\n\n")
    x, y = 1, 2
    print(x)
    print(y)
    print()

    fav_num1, fav_num2 = input(
        "List your two favorite numbers seperated by a space: ").split()
    print("Your favorite numbers are", fav_num1, "and", fav_num2)
    print("-----------------------------------------------------")

    # Section 6
    print("Section 6", end="\n\n")
    print(5//2)
    print(5 % 2)
    print("-----------------------------------------------------")

    # Section 7
    print("Section 7", end="\n\n")
    for i in {4, 5, 6, 7, 8}:
        print(i)

    for i in range(10):
        print(i)

    for i in range(11, 26, 3):
        print(i)
    print("-----------------------------------------------------")

    # Section 8
    print("Section 8 ", end="\n\n")
    # See line 17 for import
    print(pi)
    print(sqrt(16))
    print(ceil(pi))
    print(floor(pi))
    print(4**2)
    print(4**3)
    print("-----------------------------------------------------")

    # Section 9
    print("Section 9", end="\n\n")
    sum = 0
    square = 0
    a, b, c, d, e = eval(input("Enter in 5 numbers sepeared by a comma: "))
    for i in [a, b, c, d, e]:
        sum = sum + i
        square = square + i * i
    print("The sum of", a, b, c, d, e, "is", sum)
    print("The sum of the squares of", a, b, c, d, e, "is", square)
    print("-----------------------------------------------------")

    # Bonus section
    print("Bonus section", end="\n\n")

    # V = 4 / 3 *pi *R^3
    r = eval(input("Input value of r:"))
    v = 4 / 3 * pi * r ** 3
    print("V equals", v)
    print()

    # A =4 *pi *R^2
    r = eval(input("Input value of r:"))
    a = 4 * pi * r ** 2
    print("A equals", a)
    print()

    # slope = y2 - y1 / x2 - x1
    x1, y1 = eval(input("Enter in your first coordinate point: "))
    x2, y2 = eval(input("Enter in your second coordinate point: "))
    slope = (y2-y1)/(x2-x1)
    print("The slope is", slope)
    print()

    # S = (a + b + c) / 2
    a, b, c = eval(input("Input 3 numbers seperated by a comma: "))
    s = (a + b + c) / 2
    print("S equals", s)


# A = √ s(s-a)*(s-b)*(s-c)
# I attempted this problem but could not figure out how to make it work


main()
