import turtle
a = turtle.Turtle()
e = turtle.Turtle()
a.shape('turtle')
e.shape('turtle')
a.color('purple')
e.color('black')
a.pensize(5)
e.pensize(5)

e.penup()
e.right(90)
e.forward(150)

#1 circle
a.circle(50)
a.left(72)

e.pendown()
e.write('1 done, 4 to go!')
e.penup()
e.forward(20)
e.pendown()

#2 circle
a.circle(50)
a.left(72)

e.pendown()
e.write('2 done, 3 to go!')
e.penup()
e.forward(20)
e.pendown()

#3 circle

a.circle(50)
a.left(72)

e.pendown()
e.write('3 done, 2 to go!')
e.penup()
e.forward(20)
e.pendown()

#4 circle
a.circle(50)
a.left(72)

e.pendown()
e.write('4 done, 1 to go!')
e.penup()
e.forward(20)
e.pendown()

#5 circle

a.circle(50)
a.left(72)

e.pendown()
e.write('5 done, 0 to go!')
e.penup()
e.forward(20)
e.pendown()

e.color('blue')
e.write('Great job a!')

a.color('magenta')
a.write('thanks!!')
