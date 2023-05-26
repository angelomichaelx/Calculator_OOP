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
        
#adding my old calculator program in this new calculator program whit OOP concept

def calculator():
    print("\n")

    #choosing mathematical operation that will be used based on the user ( Addition(+), Subtraction(-), Multiplication(*), Division(/))
    math_operator = input("\033[1;32m""Enter an Operator (+ - * /) : ")

    #exceptions
    try: 
        #enter First number and Second number
        firstnumber = float(input("\033[1;35m""Enter the 1st number : ")) 

        secondnumber = float(input("\033[1;35m""Enter the 2nd number : ")) 
    except ValueError as ERROR:  
         print("\033[1;31m""Invalid number input\n")
         print(ERROR)
         print("\nTry again")
         return


    #If addition
    if math_operator == "+":
        sum = firstnumber + secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(sum, 4))
        print("=" * 6)

    #If subtraction
    elif math_operator == "-":
        the_difference = firstnumber - secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(the_difference, 4))
        print("=" * 6)

    #If multiplication
    elif math_operator == "*":
        the_product = firstnumber * secondnumber
        print("\033[1;36m" +"=" * 6)
        print(round(the_product, 4))
        print("=" * 6)

    #If division
    elif math_operator == "/":
    #exception for division, if the user entered zero(0) as a divisor(2nd number)    
        try:

            the_quotient = firstnumber / secondnumber
            print("\033[1;36m" +"=" * 6)
            print(round(the_quotient, 4))
            print("=" * 6)

        except ZeroDivisionError as ERROR:
            print("\033[1;31m""Invalid equation\n")
            print(ERROR)
            print("\nTry again")
            return

    else:
        print("\033[1;31m"f"{math_operator} is not a valid operator")



# Ask the user if they want to continue on using a calculator (YES/NO)

    Repeat = input("\033[1;33m""do you want to continue on using the calculator (YES/NO) : ").upper()
    if Repeat == "YES":
            calculator()
    else:
            print("Thank you!")
            exit()
while True:
    calculator()


