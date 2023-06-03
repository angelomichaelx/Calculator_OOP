# Create UserInterface class
class UserInterface:
#define method
    def ask_user_input(self):
#input code
        inp = float(input("Input a number: "))
        return inp
    
#functionality to display
    def display_sum(self, sum):
        print("Sum: " + str(sum))
        
