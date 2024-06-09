#ROCK-PAPER-SCISSORS
import random
print("ROCK-PAPER-SCISSORS")
print("Rules of game:\n #Rock beats scissors\n #Scissors beat paper\n #Ppaer beats rock")
cinput=["rock","paper","scissors"]
while True:
    userchoice=input("Enter your choice:")
    cchoice=random.choice(cinput)
    print("Computer choice:",cchoice)
    if cchoice==userchoice:
        print("Its a tie...")
    elif cchoice=="rock" and userchoice=="scissors":
        print("Opponent wins... You lose...") 
    elif cchoice=="scissors" and userchoice=="paper":
        print("Opponent wins... You lose...") 
    elif cchoice=="paper" and userchoice=="rock":
        print("Opponent wins... You lose...")  
    else:
        print("You win...")
    print("=============================================================================================================================")    
    ch=input("Do you want to continu? [Y/N]")
    if ch=="n" or ch=="N":
        print("GAME ENDS")
        break     
              