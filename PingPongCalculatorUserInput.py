#def convert_in2cm(inches):
    #return inches * 2.54

#def convert_lb2kg(pounds):
    #return pounds/2.2
ball_number = int(input("How many ping pong balls? "))

#height_in = int(input("Enter your height in inches: "))
#weight_lb = int(input("Enter your weight in pounds: "))

#height_cm = convert_in2cm(height_in)
#weight_kg = convert_lb2kg(weight_lb)

ping_pong_tall = float(ball_number * 4)
ping_pong_heavy = float(ball_number * 2.7)

#feet = height_in // 12
#inch = height_in % 12

#print("At", feet, "feet", inch, "inches tall, and", weight_lb, "pounds,")
#print("you measure", ping_pong_tall, "Ping-Pong balls tall and ")
#print("you weigh the same as", ping_pong_heavy, "Ping-Pong balls!")
print("With", ball_number, "the balls would be", ping_pong_tall, "Centimeters tall and weigh", ping_pong_heavy, "Grams.")
