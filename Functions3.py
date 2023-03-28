import math

#1 - This functions asks a string as input and returns it's reverse.
def invstring(txt):
    #txt = str(input("What word would you like to reverse?   " ))
    return(txt[::-1])
#invstring()

#2 - This functions asks for a number and checks if it is even or odd and then returns the answer.
def oddvseven(x):
    #x = int(input("Check if a number is odd or even:  "))
    if x % 2 == 0:
        return("This number is even.")
    else:
        return("This number is odd.")
#oddvseven()

#3 - This function asks for the amount of numbers you want to add to a list and then asks for the numbers themselves
# input. Then it checks all the numbers in the list and returns the highest one.

def findbigboy(list1):
    if not all(isinstance(x, int) for x in list1):
        return("Please use only digits.")
    else:
        return(f"The highest number is:  {max(list1)}")

#findbigboy()

#4 - This function asks for the amount of numbers you want to add to a list and then asks for the numbers themselves
# input. Then it checks all the numbers in the list and returns the smallest one.
def findsmol(list1):
    if not all(isinstance(x, int) for x in list1):
        return("Please use only digits.")
    else:
        return(f"The smallest number is:  {min(list1)}")
#findsmol()

#5 - This functions asks for two numbers as input and checks if they're divisble with each other and then returns the
# answer.
def checkdiv(x, y):
    if not all(isinstance(val, int) for val in (x, y)):
        return("Please use only digits.")
    else:
        if x % y == 0:
            return("These numbers can be divided with each other.")
        else:
            if y % x == 0:
                return("These numbers can be divided with each other.")
            else:
                return("These numbers cannot be divided with each other.")

#checkdiv()