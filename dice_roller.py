from random import randint

sides = int(input("How many sides is the die? "))

while sides <=0 or sides >=21 or not sides.isdigit():
    sides = int(input("Type in the number from 1 to 20: "))

quantity = int(input("How many dice are you throwing? "))

while quantity <=0 or quantity >=21:
    quantity = int(input("Type in the number from 1 to 20: "))
   
output = "|"
for run in range (0, quantity):
    roll = randint (1, sides)
    output += f" {roll} |"
print (output)

while input("Roll again?( 'q' to quit)") !="q":
    output = "|"
    for run in range (0, quantity):
        roll = randint (1, sides)
        output += f" {roll} |"
    print (output)
