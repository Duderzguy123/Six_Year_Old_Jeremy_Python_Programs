# Color Circle Spiral.py
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
t.speed(0)
colors = ["red", "yellow", "blue", "green"]
for x in range(200):
    t.pencolor( colors[ x % 4] )
    t.circle(x)
    t.right(91)
