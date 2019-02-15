import turtle
t = turtle.Pen()
t.penup()
turtle.bgcolor("black")
# Ask the user for the number of sides, default to 4, min 2, max 6
sides = int(turtle.numinput("Number of sides", "How many sides in your spiral of spirals? (2-6)", 4,2,6))
colors = ['red', 'yellow', 'blue', 'green', 'purple', 'orange']
number_of_circles = int(turtle.numinput("Number of circles", "How many circles in your rosette?",6))
# Our outer spiral loop
for m in range(100):
    t.forward(m*4)
    position = t.position()#Remember this corner of the spiral
    heading = t.heading()#Remember the direction we are heading
    #print(position, heading)
    #Our "inner" spiral loop
    #Draws a little spiral at each corner of the big spiral
    for x in range(sides):
        t.pendown()
        t.pencolor(colors[x%sides])
        t.forward(x*4)
        t.circle(m/5)
        t.right(360/sides-2)
        t.width(m/20)
        t.penup()
    t.setx(position[0]) #Go back to the big spiral's x location
    t.sety(position[1]) #Go back to the big spiral's y location
    t.setheading(heading) #Point in the big spiral's heading
    t.left(360/sides + 2) #Aim at the next point of the big spiral                        
                            
