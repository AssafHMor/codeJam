###############################################################################
#FILE: ex2a.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex2 2014-2015
#DESCRIPTION:
#a program which calculates the area and perimeter of three different shapes:
#triangle, circle or rectangle, which ever the user chooses, the user also
#enters the sizes of the shapes
###############################################################################

import math

MATH_FACTOR = 2
RECTANGLE = 1
CIRCLE = 2
TRIANGLE = 3

# ask which shape the user would like to choose 1-rectangle, 2-circle,
# 3-triangle
shape = int(input("Choose a shape:"))
#f the number is not 1,2 or 3 notify the user and exit
if shape > TRIANGLE or shape < RECTANGLE:
    print("Please enter a valid number for shape: 1 for rectangle, "
          "2 for circle, or 3 for triangle")

# if the chosen shape by the user is rectangle get the  height and width of it
if shape == RECTANGLE:
    width = float(input("width:"))
    height = float(input("height:"))
    # print the area and perimeter of the rectangle
    print("area:", width*height)
    print("perimeter:", (width+height)*MATH_FACTOR)

# if the chosen shape by the user is circle get the radius of it
elif shape == CIRCLE:
    radius = float(input("radius:"))
    # print the area and perimeter of the circle
    print("area:", radius**MATH_FACTOR*math.pi)
    print("perimeter:", math.pi*radius*MATH_FACTOR)

# if the chosen shape by the user is triangle get the edges of it
elif shape == TRIANGLE:
    edge_a = float(input("a:"))
    edge_b = float(input("b:"))
    edge_c = float(input("c:"))
    heron = (edge_a + edge_b + edge_c)/MATH_FACTOR
    # calculate the area of the triangle using Heron's formula
    # print the area and the perimeter of the triangle
    print("area:", math.sqrt(heron*(heron-edge_a)*(heron-edge_b)*(
        heron-edge_c)))
    print("perimeter:", heron*MATH_FACTOR)