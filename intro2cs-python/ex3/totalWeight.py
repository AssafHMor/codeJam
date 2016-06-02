###############################################################################
#FILE: totalWeight.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#this program counts non-negative weights and adds them, up until the sum is
#over 100 which then the program quits or up until the user adds "-1" which
#the program in return displays the sum so far and and stops
###############################################################################

LAST_ITEM = -1
MAX_WEIGHT = 100

current_weight = 0
print("Insert weights one by one:")
next_item = int(input())
has_next = True

while has_next:
    # as long as the next item is negative
    if next_item < 0:
        # if next item is -1 (the ring) prompt the sum and end the run
        if next_item == LAST_ITEM:
            print("The total packed weight is", current_weight)
            break
        print("Weights must be non-negative")
    # add the next item only if its non-negative
    if next_item >= 0:
        current_weight += next_item

    # exit if the current_weight exceeds 100
    if current_weight > MAX_WEIGHT:
        print("Overweight! Gandalf will not approve.")
        break

    next_item = int(input())