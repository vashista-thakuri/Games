# Rock beats Scissors
# Scissors beats Paper
# Paper beats Rock

# Use While loop, Infinite loop, Break Statements

import random
oppo=1
while (oppo>0):
    oppo=random.randint(1,3)
    choice=int(input("Enter your choice:\n1 for Rock\n2 for Paper\n3 for Scissor\n: "))
    if(choice == 1 and oppo == 3):
        print("You win")
        break
    elif(choice == 2 and oppo == 1):
        print("You win")
        break
    elif(choice == 3 and oppo == 2):
        print("You win")
        break
    elif(choice==oppo):
        print("Draw,try again\n")
    else:
        print("You did not win,try again\n")
if(oppo==1):
    print("Opponent chose Rock")
elif(oppo==2):
    print("Opponent chose Paper")
else:
    print("Opponent chose Scissor")