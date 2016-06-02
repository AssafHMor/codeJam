###############################################################################
#FILE: ex2a.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex2 2014-2015
#DESCRIPTION:
#a simple calculator which handles only the operations '+,-,*,/,%'. it asks
#for two numbers
###############################################################################

num1 = int(input("num1:"))
num2 = int(input("num2:"))
operation = input("operation:")

# calculate the sum of num1 and num2 if the operand is '+'
if operation == '+':
    print(num1+num2)

# calculate the difference between num1 and num2 if the operand is '-'
elif operation == '-':
    print(num1-num2)

# calculate the product of num1 and num2 if the operand is '*'
elif operation == '*':
    print(num1*num2)

# check if a dividing operand is chosen
elif operation == '/' or operation == '%':
    if num2 == 0:
        print("Can't divide by 0")  # if num2 equals '0'
    # calculate the quotient of num1 and num2 if the operand is '/'
    elif operation == '/':
        print(num1//num2)
    # calculate the remainder of num1 divided by num2 if the operand is '%'
    elif operation == '%':
        print(num1%num2)

# notify the user the if operator is not valid
else:
    print("Unknown operator")
