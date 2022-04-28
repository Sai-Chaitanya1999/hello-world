>>> import turtle
>>> t=turtle.Turtle()
>>> s=turtle.Screen()
>>> s.bgcolor("black")
>>> t.speed(0)
>>> for i in range(15):
...  for colours in ("red", "magenta", "blue", "yellow", "cyan", "green"):
...   t.color(colours)
...   t.pensize(10)
...   t.left(4)
...   t.forward(200)
...   t.left(90)
...   t.forward(200)
...   t.left(90)
...   t.forward(200)
...   t.left(90)
...   t.forward(200)
...   t.left(90)