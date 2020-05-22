import random

integer = random.randint(0,2)

if integer == 0:
	computer = "rock"
elif integer == 1:
	computer ="paper"
else:
	computer = "scissors"

player_score = 0
computer_score = 0

winning_score = 5
while player_score < winning_score and computer_score < winning_score:
    print(f"computer score is equal to {computer_score} and your score is equal to {player_score}")

    player = input("play your move : ").lower()
    if player == "quit":
        break

    print(f"computer has choosen {computer}")





    if player == computer:
        print("Its a tie")

    elif player == "":
        print("it seems that computer has choosen something but you didnt, \n please choose one, \n or type help to see the list of your available options")


    elif player == "rock":
        if computer == "paper":
            print ("computer wins")
            computer_score +=1
        elif computer == "scissors":
            print("you win")
            player_score +=1
    elif player == "paper":
        if computer == "rock":
            print("you win")
            player_score += 1
        elif computer == "scissors":
            print("computer win")
            computer_score +=1
    elif player == "scissors":
        if  computer == "rock":
            print("computer win")
            computer_score += 1
    elif computer == "paper":
            print("you win")
            player_score += 1
    else:
        print("enter a valid move")

if player_score > computer_score:
    print("WOW YOU ARE THE ULTIMATE WINNER")
elif player_score == computer_score:
    print("ITS A TIE")
else:
    print("OH NO YOU LOOSE")


