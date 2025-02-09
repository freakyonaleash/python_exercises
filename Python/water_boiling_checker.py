unit = input ("What unit are you using?")
temp = int(input ("What temperature is the water?"))

if unit == "f":
    if temp == int(212):
        print ("Your water is boiling")
    elif temp < int(212):
        print ("Your water is too cold")
    else:
        print("Your water is too hot")
elif unit == "c":
    if temp == int(100):
        print ("Your water is boiling")
    elif temp < int(100):
        print ("Your water is too cold")
    else:
        print("Your water is too hot")
elif unit == "k":
    if temp == int(373):
        print ("Your water is boiling")
    elif temp < int(373):
        print ("Your water is too cold")
    else:
        print("Your water is too hot")
else:
    print ("ERROR: unknown unit")

unit = input ("What unit are you using?")
temp = (input ("What temperature is the water?"))
temp = int(temp)
f = 212
c = 100
k = 373

if unit == "f":
    if temp == f:
        print ("Your water is boiling")
    elif temp < f:
        print ("Your water is too cold")
    else:
        print("Your water is too hot")
elif unit == "c":
    if temp == c:
        print ("Your water is boiling")
    elif temp < c:
        print ("Your water is too cold")
    else:
        print("Your water is too hot")
elif unit == "k":
    if temp == k:
        print ("Your water is boiling")
    elif temp < k:
        print ("Your water is too cold")
    else:
        print("Your water is too hot")
else:
    print ("ERROR: unknown unit")