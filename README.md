# START OF MY README
## Question 1:
Zero-Itteration conditions are loops that never run and will break. On the other hand, infinite loops run forever as long as the value is true. The main difference between them is that one never runs, and the other always runs. The main similarity is that they are both loops with conditions.
## Question 2:
I solved this issue by creating a for loop to create different parts on the screen to center it at the given distance of 800. (Check comments below for deeper explanation)
<br>
![image](https://github.com/user-attachments/assets/11f33eff-eb33-4da5-bea1-705f1a71cca2)
## Question 3:
My Final Product:
![image](https://github.com/user-attachments/assets/3063d4c3-1562-4f25-8b35-29622daef5f7)
## Question 4:
For the first while loop, the code was given, but I changed the first while loop to run at x < -200, so that it runs towards the -200 value (right side). Then I added another while loop by changing the move x and move y to the opposite values, in this case: -1 and -1. Using these values, I set the two while loops inside two run at y > -100, so that it goes down below that level, and y < 0 to make the line go up at that level.
<br>
Screenshot of Code:
![image](https://github.com/user-attachments/assets/34fd9b25-bced-453a-b483-8f0225e3f120)
## Question 5:
The answer to step 21 is that the flow chart represents the program where we had to modify a zero-iteration condition, so that we can draw five circles.
## Question 6:
My tokenizer works by using .split() for the prompt the user types. It changes the values in the new temporary list created to .lower() versions, and then looks for a word that matches the flower list. If it does, it moves on to find a number in digit form, and then executes the drawings. However, if any of these conditions aren't met, it prints out not available, so that the user can check their spelling or their input if they even wrote a flower. Overall, the tokenization splits the values into a list and checks for a flower type that is in the defined flower list, and then checks for a digit/number for the number of drawings of that flower.
<br>
Screenshot of Code:
![image](https://github.com/user-attachments/assets/321651fa-0ccc-427a-bc55-bc72b437d7e8)
## Question 7:
Undecidable problems are problems in which no algorithm can fix/solve and providing a predictable output (yes/no answer).
<br>
Example:
![image](https://github.com/user-attachments/assets/b0bde0c7-6bc1-48c3-b315-fe2a042b4e0b)
<br>
In this example, the number the user enters is not gaurannteed to be printed by the code, which is an error that can not be solved by an algorithm. (unpredictable result)
## Summary of my for loop:
In my code, the reason I only used one for loop is because I knew how to use .stamp() and .shape() to place squares instantly. Using these two methods, it allowed me to use only one for loop and draw my squares with my turtle (without drawing). However, I understood what it meant to draw the two loops. If I didn't know how to use .stamp() or .shape(), I would have the first loop as the number of squares in a range, just like usual, but instead I would need a for loop inside with a range of 4, to draw each side of the square. I would also have to change the size in that for loop, so that the squares either decrease or increase. Overall, I could have done it both ways, with two for loops and draw the squares with turtle, but I chose to use one for loop and stamp the squares by changing the shape of the turtle and dreacreasing the size and changing color over the range.
# END OF MY README

[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/SkD24yV8)
# 1.1.4Spirographs

*Complete the following.*

1. Compare and contrast zero-iteration conditions and infinite loops.
2. A link to your code where you solve the following problem. Take the screen size of 800px. Create code or algorithm that always places the object(s), up to 5, in the center an equal distance from one another and from the edges of the screen.
3. Concentric Squares -- Add a screenshot of your result and the code to create it on your repo.
Objective: Write a Python program using the turtle module to draw a pattern of concentric squares. The pattern should be created using nested loops.

Instructions:

Setup the Turtle Environment:
Import the turtle module.
Create a turtle object.
Set the turtle speed to the fastest setting.
Draw Concentric Squares:
Use a nested loop to draw multiple squares.
The outer loop should control the number of squares.
The inner loop should draw each square.
Each square should be slightly larger than the previous one.
Customize the Pattern:
Use different colors for each square.
Ensure the squares are centered on the screen.
Example Output:

The turtle should draw a series of squares, each one larger than the last, creating a pattern of concentric squares.

Hints:

Use the penup() and pendown() methods to move the turtle without drawing.
Use the color() method to change the turtle’s color.
Use the forward() and right() methods to draw the sides of the squares.


4. Complete the steps 17, 18 and 19 from [mypltw use clever to sign on](https://pltw.read.inkling.com/a/b/5310c007377c46e28d745961310f0c2e/p/728c751a6c4145bea0ea83c5058fb9f9#44b0003a2ee14fcc9865e7bb5faec747)
5. Answer to step 21
6. Insert a screenshot or picture of the algorith you used for your tokenizer on the previous activity.
7. Give an example of an undecidable problem, attach code.
