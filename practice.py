from random import randint

# rand = randint(0,1)
# if rand == 0:
#     print ("Heads")
# else:
#     print ("Tails")

# random = randint(0,6)
# print(f"{random}")

# reply = input("Please say hi")
# while reply != "hi":
#     reply = input("Rude.Say hi...")

# print ("Hi to you too!")

# num = 1
# while num <=10:
#     print (num)
#     num=num +1

# print ("end")
# count = 1
# while count <= 10:
#     print ("*" * count)
#     count = count +1

# count = 10
# while count > 0:
#     print("*" * count)
#     count = count - 1

# word = "gibberish"
# # num = "*"
# # print(num)
# for num in word:
#     print (num)
# print (num)

# print (num)

# total = 0
# for itr in "euphoria":
#     if itr in "aeiou":
#         total +=1
#         print (itr)
# print(total)

# for num in range(10, 1, -2):
#     print(num)

# count = 10
# while count >=1:
#     print (count)
#     count-=2
# for letter in "fjffjfjfljdjffjskasdiowovhghgpjd;kkfp":
#     print(letter)
#     if letter =="d":
#         break

# for outer in range (1,11):
#     print (outer)
#     for inner  in range (10,0,-1):
#         print ("\t", "inner")

# def laugh():
#     print ("HA!"*20)

# laugh()

# def laugh(strenth):
#     print ("HA!"*strenth)

# laugh (2)
# laugh (8)
# laugh (20)

# word = "Sassy"

# word = word.replace("s", "$")

# print (word)

# def divide (x,y):
#     print (x/y)

# divide (20,5)

# def divide (x,y):
#     return x/y

# res = divide (30,5)
# print (res)

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     else:
#         return False

# result = is_even(3)
# print (result)

# def is_even(number):
#     if number % 2 == 0:
#         return True
#     return False

# result = is_even(3)
# print (result)

# def is_even(number):
#     return number % 2 == 0

# result = is_even(3)
# print (result)
# def slugify (message):
#     return message.strip().lower().replace(" ", "-")

# result = slugify (" Hey HEY hEYYY ")
# print (result)

def vowel_counter (message):
    vowel = 0
    for itr in message:
        if itr in ("aeiou"):
            vowel +=1
    print(vowel)
    return vowel

result = vowel_counter ("Helloooo")
print (result)