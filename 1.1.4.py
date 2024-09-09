import turtle as painter
painter.speed(0)

outerloop = True
innerloop = True

size = 10
colors = ["red", "blue", "green", "yellow", "orange"]
index = 0

painter.penup()
painter.goto(0,0)
painter.pendown()

#while(outerloop):
painter.shape("square")
painter.color(colors[index])
painter.shapesize(size)
painter.stamp()

painter.shape("square")
painter.color(colors[index + 1])
painter.shapesize(size - 2)
painter.stamp()

painter.shape("square")
painter.color(colors[index + 2])
painter.shapesize(size - 4)
painter.stamp()

painter.shape("square")
painter.color(colors[index + 3])
painter.shapesize(size - 6)
painter.stamp()

painter.shape("square")
painter.color(colors[index + 4])
painter.shapesize(size - 8)
painter.stamp()

wn = painter.Screen()
wn.mainloop()
