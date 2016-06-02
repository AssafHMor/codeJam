###############################################################################
#FILE: findSecondSmallest.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#a program which calculates the second smallest value entered by the user
###############################################################################

NUM_OF_DANCERS = 10

dancers = []  # the list of dancers
# add the dancers one by one
for i in range(0, NUM_OF_DANCERS):
    dancers.append(int(input("What is the age of the current dancer?")))

smallest, second_smallest = dancers[0], dancers[1]
# run over the list from the second place to the last
for i in range(1, NUM_OF_DANCERS):
    if dancers[i] < second_smallest:  # if next is smaller than the s_smallest
        # if the next is smaller than the smallest
        if dancers[i] < smallest:
            second_smallest = smallest  # switch roles of s_smallest & smallest
            smallest = dancers[i]  # change to the new smallest
            continue
        second_smallest = dancers[i]

print("Pippin is dancer number", dancers.index(second_smallest)+1)

