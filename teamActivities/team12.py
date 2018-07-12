# *******************************************************************
# 12: CS101 Team Activity
# 
# These are simple coding problems.  You will not be submitting anything
# for points.  Please work together on this.  Add your code for every
# TODO section.  Copy this code to Thonny, or your python system.
# *******************************************************************

# *****************************************************************
# Write a program to draw shapes using a Turtle object.
# 
# Summary of Turtle Methods
# 
# Method		Parameters	Description
# -------------------------------------------------------------------
# Turtle		None		Creates and returns a new turtle object
# forward		amount		Moves the turtle forward by the specified amount
# backward		amount		Moves the turle backward by the specified amount
# right			angle		Turns the turtle clockwise
# left			angle		Turns the turtle counter clockwise
# penup			None		Picks up the turtle’s pen
# pendown		None		Puts down the turtle’s pen
# up			None		Picks up the turtle’s pen
# down			None		Puts down the turtle’s pen
# color			color name	Changes the color of the turtle’s pen
# fillcolor		color name	Changes the color of the turtle will use to fill a polygon
# heading		None		Returns the current heading
# position		None		Returns the current position
# goto			x,y			Move the turtle to position x,y

# *****************************************************************

import turtle
from math import cos,sin
from time import sleep

topDrawingPos = 300

# --------------------------------------------------------------------
def drawSquare(tur):
	tur.up()
	tur.goto(-250, topDrawingPos)
	tur.down()
	for i in range(4):
	    tur.forward(50)
	    tur.right(90)
   

# --------------------------------------------------------------------
# draw a triangle, each side of size 80
def drawEquTriangle(tur):
	tur.up()
	tur.goto(-150, topDrawingPos)
	tur.down()

	# TODO - Add your code here


# --------------------------------------------------------------------
# draw a Hexagon, each side of size 40
def drawHexagon(tur):
	tur.up()
	tur.goto(-50, topDrawingPos)
	tur.down()

	# TODO - Add your code here


# --------------------------------------------------------------------
# draw a Octagon, each side of size 30
def drawOctagon(tur):
	tur.up()
	tur.goto(50, topDrawingPos)
	tur.down()

	# TODO - Add your code here


# --------------------------------------------------------------------
# draw a star of size 150
def drawStar(tur):
	tur.up()
	tur.goto(200, topDrawingPos)
	tur.down()

	# TODO - Add your code here



# --------------------------------------------------------------------
def drawSpirograph(R, r, d, theta, rotations):
	window = turtle.Screen()
	window.bgcolor("#FFFFFF")

	myPen = turtle.Turtle()
	myPen.hideturtle()
	myPen.speed(0)
	myPen.pensize(3)
	myPen.color("#AA00AA")

	angle = 0

	myPen.penup()
	myPen.goto(R-r+d,0)
	myPen.pendown()

	steps = int(rotations * 3.14 / theta)

	for t in range(0,steps):
	    angle += theta

	    x = (R - r) * cos(angle) + d * cos(((R-r)/r)*angle)
	    y = (R - r) * sin(angle) - d * sin(((R-r)/r)*angle)

	    myPen.goto(x, y)


# ===================================================================
# Main Code

# create a turtle for drawing
tur = turtle.Turtle()
# turtle.screensize(canvwidth = 200, canvheight = 200)

drawSquare(tur)

# TODO
drawEquTriangle(tur)
drawHexagon(tur)
drawOctagon(tur)
drawStar(tur)

# Change the follow call to Spirograph to create different shapes
# Call it more than once, etc...
# drawSpirograph(125, 75, 125, 0.2, 6)

# finish drawing stuff to the screen - leave this here
turtle.done()
