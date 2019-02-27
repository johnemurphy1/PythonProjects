# RosettesAndPolygons.py - a spiral of polygons AND rosettes!
import turtle
t = turtle.Pen()
turtle.bgcolor("black")
#Ask the user for the number of sides, default to 4
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral?", 4))
#Our outer spiral loop for polygons and rosettes, from size 5 to 75
colors = ["red", "yellow", "blue", "orange", "green", "purple"]
for m in range(5,75):
    t.left(360/sides + 5)
    t.width(m//25+1)
    t.penup()   #Don't draw lines on spirals
    t.forward(m*4) #Move to next corner
    t.pendown() #Get ready to draw
    # Draw a little rosette at each EVEN corner of the spiral
    if (m % 2 == 0):
        for n in range(sides):
            t.pencolor(colors[n%sides])
            t.circle(m/3)
            t.right(360/sides)
    # OR, draw a little spiral at each ODD corner of the spiral
    else:
        for n in range (sides):
            t.pencolor(colors[n%sides])
            t.forward(n*3/sides + n)
            t.left(360/sides+1)
            t.width(n*sides/200)
            
