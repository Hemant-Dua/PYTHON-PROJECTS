import random

# lambda functions to speed up the process of print Win, Lose and Tie statements
win=lambda:print("You Win...!!!")
lose=lambda:print("You Lost...!!!")
tie=lambda:print("It's a Tie...")

print("Welcome to the game of Rock, Paper, Scissors...\n")
# the allowed actions of game
plays=["rock","paper","scissors"]

print("Hello, User...")
print("Select an action :")
print("R for Rock")
print("P for Paper")
print("S for Scissors\n")

# taking input of the user's action
player=input()
# taking input of the Ai's action (which is just a random choice between the three plays)
ai=random.choice(plays)

# all cases if player chose "ROCK"
if player.lower()=="r":
    print("You chose Rock..!")
    if ai=="rock":
        print("AI chose Rock..!\n")
        tie()
    elif ai=="paper":
        print("AI chose Paper..!\n")
        lose()
    elif ai=="scissors":
        print("AI chose Scissors..!\n")
        win()

# all cases if player chose "PAPER"
elif player.lower()=="p":
    print("You chose Paper..!")
    if ai=="rock":
        print("AI chose Rock..!\n")
        win()
    elif ai=="paper":
        print("AI chose Paper..!\n")
        tie()
    elif ai=="scissors":
        print("AI chose Scissors..!\n")
        lose()

# all cases if player chose "SCISSORS"
elif player.lower()=="s":
    print("You chose Scissors..!")
    if ai=="rock":
        print("AI chose Rock..!\n")
        lose()
    elif ai=="paper":
        print("AI chose Paper..!\n")
        win()
    elif ai=="scissors":
        print("AI chose Scissors..!\n")
        tie()

# if the user is mentally retarded or clumsy then this will be the ending line of program
else:
    print("INVALID INPUT !!!")