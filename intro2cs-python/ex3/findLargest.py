###############################################################################
#FILE: findLargest.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#this code finds the largest number inserted by the user, while the user
#restricts himself with the numbers he is able to enter
###############################################################################

riders_num = int(input("Enter the number of riders:"))
riders_list = []
tallest = 0  # this value represents the tallest so far

# loop over the number of riders the user entered and find the largest number
for i in range(0, riders_num):
    riders_list.append(int(input("How tall is the hat?")))
    #if the next one is the largest yet then switch
    if riders_list[i] > tallest:
        tallest = riders_list[i]

# print the result
print("Gandalf's position is:",riders_list.index(tallest)+1)