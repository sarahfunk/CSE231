###########################################################
#  Project 2
#
#  Algorithm
#    prompt for a choice
#    input a choice to draw
#    convert the string to an integer
#    for circle:
#       draw circle according to prompted amount and radius
#    for square:
#       draw circles according to prompted amount and length
###########################################################

import random    # import different modules to use
import turtle
import time
import os

print("What do you want to draw: ")    # print and prompt for choice
print("\n    (0) to quit \n    (1) circles \n    (2) square spirals.")

num_str = input("choice: ")
num_int = int(num_str)

if num_int < 0 or num_int >= 3:    # error statement if invalid choice
    print("Invalid choice; try again.")
    print("\nWhat do you want to draw: ")
    print("    (0) to quit \n    (1) circles \n    (2) square spirals.")

    num_str = input("choice: ")
    num_int = int(num_str)
    
if num_int == 0:    #exit if 0 is entered
    exit
    
if num_int == 1:    #begin prompting for circle inputs
    print("\nThis program draws concentric circles of many different colors.\n")
    num_of_circles_str = input("Enter the number of circles to draw: ")
    num_of_circles = int(num_of_circles_str)
    if num_of_circles <= 0:        # error statement if invalid number
        print("\nNumber of circles must be positive; try again.")
        num_of_circles_str = input("Enter the number of circles to draw: ")
        num_of_circles = int(num_of_circles_str)
    circle_radius_str = input("Enter the radius (>=50, <=200) of the largest circle: ")
    circle_radius = int(circle_radius_str)
    if circle_radius <50 or circle_radius > 200:    # error statement if invalid radius
        print("\nThe radius must be an integer between 50 and 200; try again.")
        circle_radius_str = input("Enter the radius (>=50, <=200) of the largest circle: ")
        circle_radius = int(circle_radius_str)
    new = circle_radius
    for i in range(num_of_circles):    # draw circles 
        if i == 0:
            turtle.setheading(90)
        turtle.color(random.random(), random.random(), random.random())
        turtle.pendown()
        turtle.begin_fill()
        turtle.circle(new)
        turtle.end_fill()
        turtle.setheading(180)
        distance_to_move = circle_radius / num_of_circles
        turtle.penup()
        turtle.forward( distance_to_move)
        turtle.setheading(90)
        radius_change = circle_radius / num_of_circles
        new = new - radius_change
    turtle.clear()
    time.sleep(5)
    os._exit(1)
        
    
if num_int == 2:    #begin prompting for square inputs
    print("\nThis program draws squares of many colors.\n")
    num_of_squares_str = input("Enter the number of squares to draw: ")
    num_of_squares = int(num_of_squares_str)
    if num_of_squares <= 0:    # error statement if invalid number
        print("\nNumber of squares must be positive; try again.")
        num_of_squares_str = input("Enter the number of squares to draw: ")
        num_of_squares = int(num_of_squares_str)
    square_length_str = input("Enter the side length (>=50, <=200) of the largest square: ")
    square_length = int(square_length_str)
    if square_length <50 or square_length > 200:    # error statement if invalid length
        print("\nThe length must be an integer between 50 and 200; try again.")
        square_length_str = input("\nEnter the side length (>=50, <=200) of the largest square: ")
    square_length = int(square_length_str)
    NUM_OF_SIDES_IN_SQUARE = 4
    DEGREES_IN_CIRCLE = 360
    angle_of_square = DEGREES_IN_CIRCLE / num_of_squares
    new_angle = 0
    for i in range(num_of_squares):    # draw squares 
        turtle.color(random.random(), random.random(), random.random())
        turtle.pendown()
        turtle.begin_fill()
        for i in range(NUM_OF_SIDES_IN_SQUARE):
            turtle.forward(square_length)
            turtle.right(90)
        new_angle = new_angle - angle_of_square
        turtle.setheading(new_angle)
        turtle.end_fill()
    turtle.clear()
    time.sleep(5)
    os._exit(1)
        