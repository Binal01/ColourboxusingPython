import turtle
t = turtle.Turtle()

length = int(input('please enter side length:'))
angle = int(input('please enter side angle:'))
c = str(input('please enter the colour:'))


#creating square box filled with colour red or black or blue
t.hideturtle()
t.speed(1)
t.begin_fill()
t.fillcolor(c)
for i in range(4):
	t.forward(length)
	t.left(angle)
t.end_fill()
t.hideturtle()
