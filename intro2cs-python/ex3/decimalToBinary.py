###############################################################################
#FILE: decimalToBinary.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program which converts a decimal number to its binary number representation
###############################################################################

DIV_FACTOR = 10
BINARY_FACTOR = 2

decimal_num = int(input("Insert number in decimal representation:"))
binary_num = 0
power = 0

while decimal_num != 0:
    # get the remainder of the number by moduling by 2
    binary_digit = decimal_num % BINARY_FACTOR
    decimal_num //= BINARY_FACTOR  # get the quotient by dividing by 2
    #multiply the remainder by 10 times its position
    binary_num += binary_digit * DIV_FACTOR**power
    power += 1

print("The binary value of the inserted decimal number is",binary_num)