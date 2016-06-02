###############################################################################
#FILE: decomposition.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program which displays a number by decomposing its digits
###############################################################################

DIV_FACTOR = 10

comp_num = int(input("Insert composed number:"))
day = 1  # start the day count from 1

while comp_num != 0:
    num_of_cups = comp_num % DIV_FACTOR  # the remainder
    comp_num //= DIV_FACTOR  # divide the number in 10 to get the new number
    print("The number of goblets Gimli drank on day",day,"was",num_of_cups)
    day += 1