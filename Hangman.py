from os import system,name
import time,random

def clear():
	if name == 'nt':
		_ = system('cls')
	else:
		_ = system('clear')
clear()

yourname=input("What is your name ?\n\n")
print("\nHello {}, let's play!".format(yourname))

time.sleep(1)
word = "thakuri"
print("\nGuess the {} letter word.".format(len(word)))
print("\nHint: Your surname.\n")

guesses=""
curse=["You need to do better.","Try harder.","Think Think Think","Really???"]
compliment=["Nice one.","You're doing great.","Awesome","Almost there!"]
turns = 5

while turns>0:
	failed = 0
	for char in word:
		if char in guesses:
			print(char,end=' ')
		else:
			print('_',end=' ')
			failed+=1
	if failed == 0:
		print("\n\nYou won, good game {}!\n".format(yourname))
		break
	print
	guess = input("\n\nGuess a character: ")
	guesses+=guess
	clear()

	if guess in word:
		print("Nice\n")
		print(random.choice(compliment),'\n')
	else:
		turns-=1
		print("Wrong guess, ",random.choice(curse))
		print("\nYou have {} turns left.\n".format(turns))
		if turns == 0:
			print("You lose, better luck next time.\n")

	exit=exit
	if (guess=='exit'):
		clear()
		break

