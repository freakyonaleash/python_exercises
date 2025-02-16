# 1. Counting Up
# Write a program that starts at 1 and keeps printing numbers until 10 using a while loop.
# num = 1
# while num <=10:
#     print (num)
#     num +=1
# 2. User Input Until "exit"
# Ask the user to enter words. Keep asking until they type "exit". Then, print "Goodbye!".
# print ("New test")
# prompt = input("Enter 'EXIT' to exit the programme ")
# while prompt != "EXIT":
#     prompt = input("Wrong command. Enter 'EXIT' to exit the programme ")    
# print ("Exiting the programme")

# 3. Sum Until 100
# Keep asking the user for numbers and add them up.
# Stop if the sum reaches or exceeds 100, then print the total sum.
# num1 = input("Enter first number: ")
# num2 = input("Enter second number: ")
# sum = int(num1)+int(num2)
# sum = 0
# while sum < 100:
#     num1 = input("Enter first number: ")
#     num2 = input("Enter second number: ")
#     sum = int(num1)+int(num2)
#     if sum <100:
#         print(f"Sum is {sum}. Start again")
# print(f"Sum is {sum}")

# 4. Password Guessing
# Set a password (e.g., "python123") and keep asking the user to enter it.
# Only stop when they type the correct password.
password = input ("Type in your password: ")
while password != "python123":
    password = input("Wrong password. Try again ")
print("Correct password. Welcome!")