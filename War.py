import random
suits = ["clubs", "diamonds", "hearts", "spades"]
faces = ["two", "three", "four", "five", "six", "seven", "eight", "nine", "ten", "jack", "queen", "king", "ace"]
keep_going = True
You_score = 0
I_score = 0
i = 0
for i in range(26):
    if i == 26:
        break
    while keep_going:
        my_face = random.choice(faces)
        my_suit = random.choice(suits)
        your_face = random.choice(faces)
        your_suit = random.choice(suits)
        print("I have the", my_face, "of", my_suit)
        print("You have the", your_face, "of", your_suit)
        if faces.index(my_face) > faces.index(your_face):
            print("I win!")
            I_score = I_score+1
        elif faces.index(my_face) > faces.index(your_face):
            print("You win!")
            You_score = You_score+1
        else:
            print("It's a tie!")
            I_score = I_score+0
            You_score = You_score+0
        answer = input("Hit [Enter] to keep going, any key to exit: ")
        keep_going = (answer == "")
        i = i+1
        print("Your current score is",You_score)
        print("My current score is",I_score)
