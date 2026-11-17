import random 
player = input(" rock, paper, or scissors: ")
comp = random.choice(["rock", "paper", "scissors"])

print("Computer chose:", comp)

if player == comp:
    print("Tie!")
elif player == "rock" and comp == "scissors":
    print("You win!")
elif player == "paper" and comp == "rock":
    print("You win!")
elif player == "scissors" and comp == "paper":
    print("You win!")
else:
    print("Computer wins!")