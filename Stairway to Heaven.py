

import turtle
turtle.goto(-100,-200)
turtle.Turtle()
turtle.bgcolor('black')
neo=turtle
neo.shape('turtle')
neo.color('green')
neo.speed(600)
neo.penup()

neo.color('blue')
neo.begin_fill()
neo.circle(50)
neo.end_fill()

neo.goto(-100,-200)
neo.pendown()
neo.color('red')
for i in range(15):
  neo.forward(20)
  neo.circle(5)
  neo.left(90)
  neo.forward(20)
  neo.right(90)

for i in range(1):
  neo.color('yellow')
  neo.begin_fill()
  neo.circle(300)
  neo.end_fill()
  
neo.penup()
neo.goto(0,0)
neo.write("And he's climbing the stairway to heaven..........")
neo.hideturtle()
