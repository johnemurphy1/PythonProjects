#set up turtle graphics
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
# Set up a list of any 8 valid Python color names
colors = ("red", "yellow", "blue", "green", "orange", "purple", "white", "gray")
#Ask the user's name using turtle's textinput pop-up window
your_name = turtle.textinput("Enter your name", "What is your name?")
# Ask the user for the number os sides, between 1 and 8, with a default of 4
sides = int(turtle.numinput("Number of sides", "How many sides do you want (1-8)?", 4, 1, 8))
# Draw a colorful spiral with the user-specified number of sides
for x in range(100):
    # Only use the right number of colors
    t.pencolor(colors[x%sides%10])
    # don't draw regular spiral line
    t.penup()
    # Change the size to match number of sides
    t.forward(x*4)
    #write user's name
    t.pendown()
    t.write(your_name, font=("Arial", int((x*2 + 4)/4), "bold"))
    #Turn 360 degrees/number of sides,plus1
    t.left(360 / sides + 1)
    
    
    
    
