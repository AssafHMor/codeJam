###############################################################################
#FILE: ithElementValue.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program which calculates the n'Th fibonacci number starting the count from 1
###############################################################################

orc_confront = int(input("Which Orc do you wish to confront?"))
first, second = 1, 1  # this series starts from 1 a
for _ in range(orc_confront-1):
    first, second = second, first+second
print("The required number of arrows is",first)