##import turtle
##k = turtle.Turtle()
##k.shape('turtle')
##
##k.penup()
##k.color('purple')
##k.write("I start at 0,0")
##k.goto(100,100)
##k.write("This is 100,100")
##k.goto(-100,-100)
##k.write("This is -100,-100")
##k.goto(100,-100)
##k.write("This is 100,-100")
##k.goto(-100,100)
##k.write("-100,100")

##Example2

##import turtle
##i = turtle.Turtle()
##i.shape('turtle')
##i.goto(200,200)
##i.goto(-200,200)
##i.goto(200,-200)
##i.goto(-200,-200)
##i.goto(0,0)
##i.write("This is how big my grid is!")

import turtle
t = turtle.Turtle()
t.shape('turtle')

#face
t.color('blue')
t.begin_fill()
t.circle(100)
t.end_fill()

#eyes
t.penup()
t.left(90)
t.forward(100)
t.forward(20)
t.pendown()
t.color('white')
t.begin_fill()
t.circle(30)
t.end_fill()
t.color("Black")
t.begin_fill()
t.circle(10)
t.end_fill()
t.color('white')
t.penup()
t.right(90)
t.forward(30)
t.pendown()
t.begin_fill()
t.circle(30)
t.end_fill()
t.color('black')
t.begin_fill()
t.circle(10)
t.end_fill()

#nose
t.penup()
t.right(120)
t.forward(50)
t.pendown()
t.color('purple')
t.stamp()

#mouth
t.penup()
t.forward(40)
t.pendown()
t.begin_fill()
t.color("maroon")
t.circle(20)
t.end_fill()

