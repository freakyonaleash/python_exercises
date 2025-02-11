tweet = input("Provide your tweet:")
max_lenght = 140
char_count = len(tweet)

if char_count <= max_lenght:
    print (f"Your {char_count} characters tweet is good to go")
else:
    print (f"Your {char_count} tweet is {char_count - max_lenght} characters too long")