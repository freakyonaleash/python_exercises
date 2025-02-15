import random
dice_1=random.randint(1,6)
dice_2=random.randint(1,6)
count = 1
print (dice_1, dice_2)


while dice_1 !=1 and dice_2 !=1:
    print (dice_1, dice_2)
    dice_1=random.randint(1,6)
    dice_2=random.randint(1,6)
    count+=1
print (dice_1, dice_2) 
print(f"Snake eyes. It took {count} tries!")