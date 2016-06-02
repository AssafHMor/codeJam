###############################################################################
#FILE: twoDimensionalSeek.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex3 2014-2015
#DESCRIPTION:
#this program calculates the straight line between the start point to the end
#point after the user finished entering his route
###############################################################################

NORTH = 1
EAST = 2
SOUTH = 3
WEST = 4

x_coordinate = 0  # x position
y_coordinate = 0  # y position
next_turn = input("Next turn:")

# first step can be only on x axis
if next_turn != "end":
    steps = int(input("How many steps?"))
    if next_turn == "right":
        movement = EAST  # set the first direction to be east
        x_coordinate += steps
    else:
        movement = WEST  # set the first direction to be west
        x_coordinate -= steps
    next_turn = input("Next turn:")

while next_turn != "end":
    steps = int(input("How many steps?"))
    #if the travel is to east the next movement can only be south or north
    if movement == EAST:
        if next_turn == "right":
            movement = SOUTH
            y_coordinate -= steps
        else:
            movement = NORTH
            y_coordinate += steps

    #if the travel is to west the next movement can only be south or north
    elif movement == WEST:
        if next_turn == "right":
            movement = NORTH
            y_coordinate += steps
        else:
            movement = SOUTH
            y_coordinate -= steps

    #if the travel is to north the next movement can only be west or east
    elif movement == NORTH:
        if next_turn == "right":
            movement = EAST
            x_coordinate += steps
        else:
            movement = WEST
            x_coordinate -= steps

    #if the travel is to south the next movement can only be west or east
    elif movement == SOUTH:
        if next_turn == "right":
            movement = WEST
            x_coordinate -= steps
        else:
            movement = EAST
            x_coordinate += steps
    next_turn = input("Next turn:")

# evaluate the direction on y axis
if y_coordinate >= 0:
    y_direction = "forward"
elif y_coordinate < 0:
    y_direction = "backward"
# evaluate the direction on x axis
if x_coordinate >= 0:
    x_direction = "right"
elif x_coordinate < 0:
    x_direction = "left"

print("Gandalf should fly",abs(x_coordinate),"steps",x_direction,"and",
      abs(y_coordinate),"steps",y_direction)