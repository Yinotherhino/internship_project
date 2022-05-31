# rock paper scissors game
import random

def rockPaperScissors():
	outcomes = ["R","P","S"]
	user_pick= input("Type R, P or S: ").upper()
	while user_pick not in outcomes:
		print("Only R, P or S is allowed")
		user_pick= input("Type R, P or S: ").upper()
	com_pick = random.choice(outcomes)
	dictRPS ={"R":"Rock", "P":"Paper", "S":"Scissors"}
	print (user_pick)
	print ("Player(" + dictRPS[user_pick] + ") : CPU(" + dictRPS[com_pick] + ")")
	if user_pick == com_pick:
		print("It's a tie. we go again")
		return(rockPaperScissors())
	if user_pick == "R" and com_pick== "S":
		print("User WINS! ")
	if user_pick == "S" and com_pick== "R":
		print("CPU WINS! ")
	if user_pick == "P" and com_pick== "R":
		print("User WINS! ")
	if user_pick == "R" and com_pick== "P":
		print("CPU WINS! ")
	if user_pick == "S" and com_pick== "P":
		print("User WINS! ")
	if user_pick == "P" and com_pick== "S":
		print("CPU WINS! ")

rockPaperScissors()
