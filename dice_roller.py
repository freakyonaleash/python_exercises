from random import randint

sides = int(input("How many sides is the die? "))
quantity = int(input("How many dice are you throwing? "))

while (sides or quantity) <=0 or (sides or quantity) >=21:
    sides = input("Type in the number from 1 to 20")
    quantity = input("Type in the number from 1 to 20")
    
    
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
