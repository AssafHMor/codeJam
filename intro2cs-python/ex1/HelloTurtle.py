###############################################################################
#FILE: HelloTurtle.py
#WRITER: Assaf_Mor + assafm04 + 036539096
#EXCERSICE: intro2cs ex1 2014-2015
#DESCRIPTION:
#A program that draws some simple geometric shapes on the screen and prints
# "Hello Turtle!", using Turtle graphics
###############################################################################
import turtle

#create the red square
turtle.up()
turtle.goto(-100,-100)
turtle.down()
turtle.color("red")
turtle.goto(-100,100)
turtle.goto(100,100)
turtle.goto(100,-100)
turtle.goto(-100,-100)

#create the orange circle inside the red square
turtle.up()
turtle.goto(0,-100)
turtle.down()
turtle.color("orange")
turtle.circle(100)

#create the blue square
turtle.up()
turtle.goto(-200,0)
turtle.down()
turtle.color("blue")
turtle.goto(0,200)
turtle.goto(200,0)
turtle.goto(0,-200)
turtle.goto(-200,0)

#create the writing in green inside the circle
turtle.up()
turtle.goto(-70,-5)
turtle.down()
turtle.color("green")
turtle.write("Hello Turtle!",font=("Ariel",20,"normal"))
turtle.done()
