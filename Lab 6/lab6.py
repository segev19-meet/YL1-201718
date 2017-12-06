from turtle import *
import random
import math

class Ball(Turtle):
    def __init__(self,radius,color,speed):
        Turtle.__init__(self)
        self.shape("circle")
        self.shapesize(radius/10)
        self.radius = radius
        self.color(color)
        self.speed(speed)

ball1=Ball(10,"red",5)
ball2=Ball(15,"green",10)

def check_collision(ball1,ball2):
    x1 = ball2.xcor()
    x2 = ball2.xcor()
    y1 = ball2.xcor()
    y2 = ball2.xcor()
    D = math.sqrt(math.pow((x2-x1),2) + math.pow((y2-y1),2))
    answer=D
    sum=ball1.radius+ball2.radius


    if(answer>sum):
        print("the 2 balles are not collaide")
    elif(answer<sum or answer==sum):
        print("the 2 balls are collaide")

ball1.goto(100,100)
check_collision(ball1, ball2)
#turtle.mainloop()
   














