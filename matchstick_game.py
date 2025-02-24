print("*************************")
print("** WELCOME TO THE GAME **")
print("*************************")
player1 = input("Input Player One name: ")
player2 = input("Input Player Two name: ")
number = 13
sticks = "|"
matchsticks = number * sticks
print (matchsticks)
print (f"There are {number} matchsticks left")


while True:
    #player1 turn:

    player1_turn = input(f"How many matchsticks do you take, {player1}?")
    while int(player1_turn) not in (1,2,3):
        player1_turn = input("Invalid number. Type in 1, 2 or 3: ") 
    number -=int(player1_turn)
    matchsticks = number * sticks

    if number <= 0:
        print(f"{player2} WINS!")
        break 

    print (matchsticks)
    if number == 1:
        print (f"There is {number} matchsticks left")
    else: print (f"There are {number} matchsticks left")
    #player2 turn:

    player2_turn = input(f"How many matchsticks do you take, {player2}?")
    while int(player2_turn) not in (1,2,3):
        player2_turn = input("Invalid number. Type in 1, 2 or 3: ") 
    number -= int(player2_turn)
    matchsticks = number * sticks

    if number <= 0:
        print(f"{player1} WINS!")
        break

    print (matchsticks)
    if number == 1:
        print (f"There is {number} matchsticks left")
    else: print (f"There are {number} matchsticks left")
    
        