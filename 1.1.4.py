#Import turtle and set speed to the fastest (0)
import turtle as painter
painter.speed(0)
#set size as 42, so that squares start from 40
size = 42
#20 colors for 20 squares
colors = ["red", "blue", "green", "yellow", "purple", "orange", "pink", "cyan", "magenta", "teal", "lime", "indigo", "lavender", "maroon", "gold", "turquoise", "coral", "slategray", "olive", "orchid"]
#set index at -1, so that the index starts at index 0 (red) and ends at index 19 (orchid), to cycle through colors for different squares
index = -1
#fixes the issue, keeps the drawing in the middle of any screen at (0,0)
painter.penup()
painter.goto(0,0)
painter.pendown()
#for loop - 20 squares
for i in range(20):
    #Increase Index (Cycles through Colors)
    index += 1
    #Decreases size, so that the squares go from biggest at 40 to smallest at 2
    size -= 2
    #Instead of using a second for loop to draw squares, I used .shape() and .stamp() to instantly draw the squares
    painter.shape("square")
    painter.color(colors[index])
    painter.shapesize(size)
    painter.stamp()
#Keep the drawing on screen
wn = painter.Screen()
wn.mainloop()
