###############################################################################
#FILE: binaryToDecimal.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program which converts a binary number to its decimal number representation
###############################################################################

DIV_FACTOR = 10
BINARY_FACTOR = 2

binary_num = int(input("Insert number in binary representation:"))
power = 0
decimal_num = 0

while binary_num != 0:
    binary_digit = binary_num % DIV_FACTOR  # get the first digit of the binary
    binary_num //= DIV_FACTOR  # divide the binary by 10 to get the next binary
    # the decimal is the sum of binary digits * 2 times its position
    decimal_num += (binary_digit * (BINARY_FACTOR ** power))
    power += 1

print("The decimal value of the inserted binary number is",decimal_num)