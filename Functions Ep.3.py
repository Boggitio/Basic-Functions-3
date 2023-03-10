import math

#11 - This functions asks a string as input and returns it's reverse.
def invstring():
    txt = str(input("What word would you like to reverse?   " ))
    print(txt[::-1])
invstring()

#12 - This functions asks for a number and checks if it is even or odd and then returns the answer.
def oddvseven():
    x = int(input("Check if a number is odd or even:  "))
    if x % 2 == 0:
        print("This number is even.")
    else:
        print("This number is odd.")
oddvseven()

#13 - This function asks for the amount of numbers you want to add to a list and then asks for the numbers themselves
# input. Then it checks all the numbers in the list and returns the highest one.

def findbigboy():
    list1 = []
    x = int(input("Specify how many numbers you want to add to the list: "))
    for i in range(1, x + 1):
        nums = int(input("Specify numbers: "))
        list1.append(nums)
    print("The highest number is:  ", max(list1))
findbigboy()

#14 - This function asks for the amount of numbers you want to add to a list and then asks for the numbers themselves
# input. Then it checks all the numbers in the list and returns the smallest one.
def findsmol():
    list1 = []
    x = int(input("Specify how many numbers you want to add to the list: "))
    for i in range(1, x + 1):
        nums = int(input("Specify numbers: "))
        list1.append(nums)
    print("The smallest number is:  ", min(list1))
findsmol()

#15 - This functions asks for two numbers as input and checks if they're divisble with each other and then returns the
# answer.
def checkdiv():
    x = int(input("Choose a number  "))
    y = int(input("Choose a number you want to check if it is divisible with  "))

    if x % y == 0:
         print("These numbers can be divided with each other.")
    else:
        if y % x == 0:
            print("These numbers can be divided with each other.")
        else:
            print("These numbers cannot be divided with each other.")
checkdiv()