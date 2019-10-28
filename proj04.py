###########################################################
#  Project 4
#
#  Algorithms
#    define functions for drawing parts of flags
#    define functions for drawing flags
#    define function to prompt user for their choice of flags
###########################################################

#import module for turtle
import turtle

#define function to draw a rectangle with five parameters
def rectangle(x,y,length,height,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.pendown()
    turtle.color(color)
    turtle.begin_fill()
    for i in range(2):
        turtle.forward(height)
        turtle.right(90)
        turtle.forward(length)
        turtle.right(90)
    turtle.end_fill()
    turtle.penup()
    
#define function to draw a circle with four parameters
def circle(x,y,radius,color):
    turtle.penup()
    turtle.goto(x,y)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    turtle.circle(radius)
    turtle.end_fill()
    turtle.penup()

#define function to draw a crescent by drawing to circles depending on parameters    
def crescent(x1,y1,x2,y2,R1,R2,color1,color2):
    circle(x1,y1,R1,color1)
    circle(x2,y2,R2,color2)
  
#define function to draw a star based on five parameters    
def star(x,y,size,color,theta):
    turtle.goto(x,y)
    turtle.setheading(theta+72)
    turtle.color(color)
    turtle.pendown()
    turtle.begin_fill()
    for i in range(5):
        turtle.forward(size)
        turtle.right(72)
        turtle.forward(size)
        turtle.left(144)
    turtle.end_fill()
    turtle.penup()

#define a function to draw a circle of stars     
def circle_of_stars(x,y,size1,size2,color,theta):
    turtle.penup()
    turtle.goto(x,y)
    turtle.setheading(0)
    turtle.color(color)
    turtle.forward(size1)
    star(x-((13*size1)/10)+2,y-(2*size1), size2, color, theta)
    turtle.left(72)
    turtle.forward(size1)
    star(x+(13*size1)/10,y-(2*size1)-5, size2, color, theta)
    turtle.left(72)
    turtle.forward(size1)
    star(x+((size1)*2)+3,y+((size1)/4)-6, size2, color, theta)
    turtle.left(72)
    turtle.forward(size1)
    star(x-((size1)*2)+4,y+((size1)/4), size2, color, theta) 
    turtle.left(72)
    turtle.forward(size1)
    star(x+5,y+(2*(size1)), size2, color, theta)

#define function to draw the Tunisian flag by using previously defined functions
def Tunisian_flag(x, y, height):
    turtle.speed(100)
    rectangle(x,y,height,1.5*height, "red")
    circle(x+(1.5*height/2),y-3*((height)/4),height/4,"white" )
    crescent(x+(1.5*height/2),y-(5.5*height)/8,x+((1.5*height/2)+(height/20)),y-(6.5*height)/10, (3*(height))/16,(3*(height))/20,"red", "white")
    star((x+(1.5*height/2)-(height/20)),y-(20*height)/40,(1.5*height/20),"red",270)
    turtle.home()

#define function to draw the Libyan flag by using previously defined functions
def Libyan_flag(x, y, height):
    turtle.speed(100)
    rectangle(x,y,(height/4), 1.5*height,"red")
    rectangle(x, y-(height/4),height/2,(1.5*height), "black")
    rectangle(x,y-(3*height)/4,height/4,(1.5*height),"green")
    crescent(x+(3*height)/4,y-(2.5*height/4), x+(19*height/24), y-((3*height/5)), height/8,height/10, "white","black")
    star(x+(3.5*(1.5*height))/6, y - height/2,1.5*height/32,"white",270)
    turtle.home()
   
#define function to draw Turkey's flag by using previously defined functions    
def Turkey_flag(x, y, height):
    turtle.speed(100)
    rectangle(x-1,y+1,(height+2),((height*1.5)+(height/30))+2,"black")
    rectangle(x,y,height,(height)/30,"white")
    rectangle(x+(height/30),y,height,1.5*height,"red")
    crescent(x+(height/2),y-(1.5*height/2), x+(height/2)+(height/16), y- ((3.5*height)/5), height/4, height/5,"white","red")
    star(x+((1.5*height)/2),y-((2*height)/4),1.5*height/16,"white",270)
    turtle.home()
   
#define function to draw the Singaporean flag by using previously defined functions    
def Singaporean_flag(x, y, height):
    turtle.speed(100)
    rectangle(x-1,y+1,(height+2),(height*1.5)+2,"black")
    rectangle(x,y-(height/2),(height/2),(height*1.5),"white")
    rectangle(x,y,height/2,height*1.5,"red")
    crescent(x+(height/3),y-((11.75*height)/27),x+(height/3)+(height/10),y-(2.25*height)/5, (5*height)/27,2*height/10,"white","red")
    circle_of_stars(x+(height/3)+(height/15),y-(2.15*height)/9,height/18,(2.5*height)/90,"white",270)
    turtle.home()
    
#define the main function to prompt a user's choice then draw their choice within set parameters
def main():
    prompt ="""Select one of the following options: 
         ‘TUN’ for the Tunisian flag 
         ‘LBY’ for the Libyan flag 
         ‘TUR’ for the Libyan flag
         ‘SGP’ for the Singaporean flag 
         ‘All’ for all four (4) flags
         ‘Q’ to quit"""
    print(prompt)
    user_choice = input(": ")
    user_choice = user_choice.upper()
    
    #while loop for the user's choice
    while user_choice != "":
        if user_choice == "TUN":
            Tunisian_flag(0, 0, 240)
            turtle.bye()
            break
        elif user_choice == "LBY":
            Libyan_flag(0, 0, 240) 
            turtle.bye()
            break
        elif user_choice == "TUR":
            Turkey_flag(0, 0, 240)
            turtle.bye()
            break
        elif user_choice == "SPG":
            Singaporean_flag(0, 0, 240)
            turtle.bye()
            break
        elif user_choice == "ALL":
            Tunisian_flag(-300,250,240)
            Libyan_flag(-300,-50,240)
            Turkey_flag(100,250,240)
            Singaporean_flag(100,-50,240)
            turtle.bye()
            break
        elif user_choice == "Q":
            print("Bye")
            quit
        else:
            print("This is not one of the possible options.")
            print(prompt)
            user_choice = input(": ")
            user_choice = user_choice.upper()

#call main function 
main()