#Michael Angelo P. Biag
#BSCPE 1-4
#Assignment 7 Calculator program using OOP concept

# Create calculator class
class calculator:

# constructor
    def __init__(self):
        self.operators = ('+','-','*','/')
#addition
    def addition(self, num1, num2):
        return num1 + num2
#subtraction
    def subtraction(self, num1, num2):
        return num1 - num2
#multiplication 
    def multiplication(self, num1, num2):
        return num1 * num2
#division
    def division(self, num1, num2):
        if num2 == 0:
            raise ZeroDivisionError
        else:
            return num1 / num2



