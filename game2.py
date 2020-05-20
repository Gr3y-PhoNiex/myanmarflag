from turtle import *


penup()
goto(-400,250)
pendown()

# yellow rectangle
color('Yellow')
begin_fill()
forward(800)
right(90)
forward(167)
right(90)
forward(800)
end_fill()

# green rectangle
color('green')
begin_fill()
left(90)
forward(167)
left(90)
forward(800)
left(90)
forward(167)
end_fill()

left(180)
penup()
forward(167)
pendown()

# red rectangle
color('red')
begin_fill()
forward(167)
right(90)
forward(800)
right(90)
forward(167)
end_fill()

right(90)

penup()
goto(-180,50)
pendown()
begin_fill()
fillcolor('white')
pencolor('white')
for x in range(5):
    forward(350)
    right(144)
end_fill()
hideturtle()
done()