import time

def wait(x):
        time.sleep(x)

def y_n(x):
    if x.lower()=="y":
        print("Great! Let's play again.")
    elif x.lower()=="n":
        print("Ok, then I am not playing with you...")
        wait(2)
        print("BYE!!!")
        exit()
    else:
          print("Press Y for 'Yes'")
          print("or N for 'No'")
          a=input()
          y_n(a)

def y_n1(x):
    if x.lower()=="y":
        print("Fantastic...!!! Let's Do it again...")
        wait(2)
        print("And this time I won't say it...")
        wait(2)
    elif x.lower()=="n":
        print("Yeah...Yeah...You are right...")
        wait(2)
        print("I should leave for what I have done...It's Embarrassing...")
        wait(2)
        print("Bye")
        exit()
    else:
          print("Press Y for 'Yes'")
          print("or N for 'No'")
          a=input()
          y_n1(a)

def y_n2(x):
    if x.lower()=="y":
        print("OK, Let's play again... as mistakes do happen with everyone...")
        wait(2)
        print("I am only HUMAN after all...!!!")
        wait(2)
        print("Hold Up...I am not a Human....")
        wait(2)
        print("Well Anyways!!!")
        wait(2)

    elif x.lower()=="n":
        print("Yeah...Yeah...")
        wait(2)
        print("UNDERSTANDABLE...HAVE A GREAT DAY...")
        wait(2)
        print("Bye")
        exit()
    else:
          print("Press Y for 'Yes'")
          print("or N for 'No'")
          a=input()
          y_n2(a)

def y_n3(x):
    if x.lower()=="y":
        print("OK, So the hint is:")
        wait(2)
    elif x.lower()=="n":
        print("Tough Guy...huh...")
        wait(2)
        print("I liked the attitude...")
        wait(2)
        print("So the hint is:")
        wait(2)
    else:
          print("Press Y for 'Yes'")
          print("or N for 'No'")
          a=input()
          y_n3(a)
    print("He/She is the most interesting person.")

def y_n4(x):
     if x.lower()=="y":
        print("The Hint is: You know the person.")
        wait(2)
     elif x.lower()=="n":
        print("I know you said NO... but the developer is out of ideas to add anything else...")
        wait(2)
        print("So the Hint is: You know the person.")
        wait(2)
     else:
        print("Press Y for 'Yes'")
        print("or N for 'No'")
        a=input()
        y_n4(a)

def main():
    print("----------------------GUESSING WORD GAME.EXE---------------------")
    print("Hello, User...")
    wait(2)
    print("This Game is not one of those boring games of guessing...Its a little Special...")
    wait(3)
    print("So, You can forget about the boredom and can proceed and have a great time playing it...")
    wait(3)

    for i in range(5):
            guess=input("Enter your guess :")

    print("Opps!!! I forgot to select a word...")
    wait(3)
    print("I am sorry for wasting your energy, Man !!!")
    wait(3)
    ans=input("Will you forgive me...??? (Y/N)")
    y_n(ans)

    print("...")
    wait(5)
    print("I am gonna go with this word: 'Ball'")
    wait(2)
    guess=input("Enter your Guess :")
    wait(1)
    if guess=="ball":
        print("Wait!!! You did it in the first try...???")
        wait(3)
        print("Ohh...I told the word too...")
        wait(2)
        print("(Nervous laughter...)")
        wait(2)
        ans=input("Shall I try again...???(Y/N)")
        y_n1(ans)
        
    else:
        print("Bruh...!!! The Word was right there and you still managed to get it wrong...")
        wait(2)
        print("LMAO...Caught you in 4K...")
        wait(2)
        ans=input("You want to try again...???(Y/N)")
        y_n2(ans)

    print("...")
    wait(3)
    print("Yeah I chose my word...")
    guess=""
    guess_no=0
    wait(1)
    while guess.lower() != "i":
        guess=input("Enter your Guess :")
        guess_no+=1

        if guess_no==10:
            print("I know it's a little hard...!!!")
            wait(2)
            ans=input("Do u want a hint...?(Y/N)")
            y_n3(ans)

        if guess_no==15:
            print("Still didn't got the answer...???")
            wait(2)
            ans=input("Do u want another hint...?(Y/N)")
            y_n4(ans)

        if guess_no==20:
            print("STOP!!!")
            wait(2)
            print("I think you need one more hint, isn't it?")
            wait(2)
            print("This is the last one...")
            wait(2)
            print("The word is just a one letter word...")
            
        if guess_no==27:
            print("Sigh..... Are u just gonna bash the letters one by one.....")

    print("Correct...")
    wait(3)
    print("I")
    wait(3)
    print("People tend to forget themselves when it comes to loving...")
    wait(3)
    print("I know it's a little cringe but be happy for what you are...")
    wait(3)
    print("Take it as a wake up call... or anything you want...")
    wait(3)
    print("Never forget about your Happiness in any situation...")
    wait(3)
    print("And yeah...")
    wait(3)
    print("THANKS FOR PLAYING")
    wait(3)
    print("Told...Yeah...The game was not boring...It was just a bit Weird...")
    wait(3)
    print("If I was in your position I would have never expected all that from a boring Word Guessing Game...")
    wait(5)
    print("-------------------------Developer: Hemant---------------------------")
    print("THANKS A LOT FOR PLAYING :)")

main()