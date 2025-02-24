from random import randint

sides = int(input("How many sides is the die? "))

while sides <=0 or sides >=21:
    sides = int(input("Wrong input. Type in the number from 1 to 20: "))

quantity = int(input("How many dice are you throwing? "))

while quantity <=0 or quantity >=21:
    quantity = int(input("Wrong input. Type in the number from 1 to 20: "))
# version 1 with the first roll handled separately
# output = "|"
# for run in range (quantity):
#     roll = randint (1, sides)
#     output += f" {roll} |"
# print (output)

# while input("Roll again?( 'q' to quit)") !="q":
#     output = "|"
#     for run in range (quantity):
#         roll = randint (1, sides)
#         output += f" {roll} |"
#     print (output)

# version 2 with all rolls handled within the same loop

# reply = ""
# while reply != "q":
#     output = "|"
#     for run in range(quantity):
#         roll = randint(1, sides)
#         output += f" {roll} |"
#     print(output)

#     reply = input("Roll again? ('q' to quit) ").lower()


while True:
    output = "|"
    for die in range (quantity):
        roll = (randint(1, sides))
        output += f" {roll} |"
    print (output)
    reply = input ("Roll again? ('q' to quit)")
    if reply == "q":
         break