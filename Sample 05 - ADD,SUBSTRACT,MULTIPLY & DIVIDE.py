
"""
Sample 05 - ADD,SUBSTRACT,MULTIPLY & DIVIDE.py
# ------------------------------------------
# Logical Operators / Conditional statement
# ------------------------------------------
CALCULATOR
"""

option          = input("+:ADD, -:SUBSTRACT, *:MULTIPLY & /:DIVIDE: ")
firstNumber     = int(input("First Number: "))
secondNumber    = int(input("First Number: "))
if (option == '+'):
    print(firstNumber + secondNumber)
elif (option == '-'):
    print(firstNumber - secondNumber)
elif (option == '*'):
    print(firstNumber * secondNumber)
elif (option == '+'):
    if (secondNumber == 0):
        print("Division by zero - you cannot do it!")
    else:    
        print(firstNumber / secondNumber)
else:
    print("You have typer something unexpected..["+option+"]")
