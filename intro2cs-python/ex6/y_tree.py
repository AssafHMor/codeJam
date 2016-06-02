# ############################################################
# FILE : y_tree.py
# WRITER : Assaf Mor , assafm04 , 036539096
# EXERCISE : intro2cs ex6
# DESCRIPTION:
# this is a method which draws a "Y" tree using the turtle library.
# the drawing is done recursively.
# ############################################################
import turtle
LENGTH_MULTIPLY_FACTOR = 0.6  # the length multiplier
DEGREES_TURNED_LEFT = 30  # degrees to turn left at a junction
DEGREES_TURNED_RIGHT = 60  # degrees to turn right at a junction
DEFAULT_BARK_LENGTH = 200  # the default starting length of the first step
SMALLEST_BRANCH_LENGTH = 10  # the minimum length of step allowed


def draw_tree(length=DEFAULT_BARK_LENGTH):
    """
    this method will draw a "Y" tree recursively using the Turtle methods.
    the method is set to work with a default length of 200
    :param length: the length of the branch
    :return:
    """
    if length < SMALLEST_BRANCH_LENGTH:  # if the length is less than 10 return
        return
    turtle.fd(length)  # go forward the current length
    turtle.left(DEGREES_TURNED_LEFT)  # turn 30 degrees left
    draw_tree(length * LENGTH_MULTIPLY_FACTOR)  # call the function with the new length
    turtle.right(DEGREES_TURNED_RIGHT)  # turn 60 degrees right
    draw_tree(length * LENGTH_MULTIPLY_FACTOR)  # call the function with the new length
    turtle.left(DEGREES_TURNED_LEFT)  # turn 30 degrees left to return backwards
    turtle.fd(-length)  # go backwards the current length
    return

draw_tree()