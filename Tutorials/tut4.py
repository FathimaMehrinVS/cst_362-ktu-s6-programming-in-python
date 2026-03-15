#Write a Python program to draw a hexagon and fill it with red color using turtle graphics.
import turtle
t=turtle.Turtle()
t.fillcolor("red")
t.begin_fill()
for i in range(6):
    t.forward(100)
    t.right(60)
t.end_fill()
turtle.done()