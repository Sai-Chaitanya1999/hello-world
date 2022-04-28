>>> import turtle
>>> t=turtle.Turtle()
>>> s=turtle.Screen()
>>> s.bgcolor("black")
>>> t.speed(0)
>>> for i in range(15):
...  for colours in ("red", "magenta", "blue", "yellow", "cyan", "green"):
...   t.color(colours)
...   t.pensize(3)
...   t.left(4)
...   t.circle(100)