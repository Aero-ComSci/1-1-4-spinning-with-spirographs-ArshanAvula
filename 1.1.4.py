#Import turtle and set speed to the fastest (0)
import turtle as painter
painter.speed(0)
#set size as 22, so that squares start from 20
size = 22
#10 colors for 10 squares
colors = ["black", "brown", "red", "green", "yellow", "blue", "gray", "orange", "pink", "purple"]
#set index at -1, so that the index starts at 0 (black) and ends at 9 (purple), to cycle through colors for different squares
index = -1
#fixes the issue, keeps the drawing in the middle of any screen at (0,0)
painter.penup()
painter.goto(0,0)
painter.pendown()
#for loop - 10 squares
for i in range(10):
    #Increase Index (Cycles through Colors)
    index += 1
    #Decreases size, so that the squares go from biggest at 20 to smallest at 2
    size -= 2
    #Instead of using a second for loop to draw squares, I used .shape() and .stamp() to instantly draw the squares instantly
    painter.shape("square")
    painter.color(colors[index])
    painter.shapesize(size)
    painter.stamp()
#Keep the drawing on screen
wn = painter.Screen()
wn.mainloop()
