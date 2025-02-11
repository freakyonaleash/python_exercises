f_name = input("What is your name?")
l_name = input ("What is your last name?")

full_name = len(f_name) + len(l_name)

print("*"*full_name)

if full_name >12:
    print(f"{f_name}  {l_name} is {full_name - 12} characters longer than the average American name")
elif full_name == 12:
    print(f"{f_name}  {l_name} is exactly the length of the average American name")
else:
    print(f"{f_name}  {l_name} is {12 - full_name} character shorter than the average American name")
    
print("*"*full_name)