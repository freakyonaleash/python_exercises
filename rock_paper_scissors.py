from random import randint

rock = """
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)"""

paper = """
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
"""

scissors = """
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
"""
# Pick a random number from 1 to 3
num = randint(1,3)
# Turn that random number into the computer's RPS move
if num == 1:
    c_move = "rock"
elif num == 2:
    c_move = "paper"
else:
    c_move = "scissors"

# Ask a user to enter their move
p_move = input ("What is your move? ")

# Print the rock, paper, or scissors ASCII art that corresponds to the player's move
if p_move == "rock":
    print (f"\n Your move is: *ROCK*{rock}")
elif p_move == "paper":
    print (f"\n Your move is: *PAPER*{paper}")
else:
    print (f"\n Your move is: *SCISSORS*{scissors}")  
# Print the rock, paper, or scissors ASCII art that corresponds to the computer's move

print (f"\n Computer move is: *{c_move.upper()}*")
if c_move == "rock":
    print (rock)
elif c_move == "paper":
    print (paper)
else:
    print (scissors)
# # # Figure out who wins and print the result!
if p_move == c_move:
    print ("***It's a tie***")
elif (p_move == "rock" and c_move == "scissors") or (p_move == "scissors" and c_move == "paper") or (p_move == "paper" and c_move == "rock"):
    print ("***You win!***")
else:
    print("***You lose***")

