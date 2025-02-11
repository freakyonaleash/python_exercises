# Exercise: String Magic  
# 1. Create a string variable called `sentence` and set it to: "Python is FUN and POWERFUL."  
# 2. Convert the entire sentence to lowercase and print it.  
# 3. Replace "FUN" with "amazing" and print the result.  
# 4. Check if the word "Python" is in the string and print the result.  
# 5. Find the index of the word "POWERFUL" and print it.  
# 6. Split the sentence into words and print the list.  

# Your code here:
sentence = "Python is FUN and POWERFUL."
print (sentence.lower())
print(sentence.replace("FUN", "amazing"))
print(sentence.find("Python"))
print(sentence.index("POWERFUL"))
print(sentence.split())

# Exercise:
# 1. Declare a string variable called `quote` with the value "Coding is CHALLENGING but REWARDING."
# 2. Convert the entire string to lowercase and rewrite the variable.
# 3. Replace the word "challenging" with "fun" (make sure it's lowercase now).
# 4. Remove the period at the end of the string.
# 5. Finally, split the words into a list and rewrite the variable.
# Print the result after each step.

quote = "Coding is CHALLENGING but REWARDING."
quote = quote.lower ()
quote = quote.replace("challenging", "fun")
quote = quote.replace(".", "")
quote = quote.split()
print(quote)

quote = "Coding is CHALLENGING but REWARDING."
print(quote.lower().replace("challenging", "fun").replace(".","").split())