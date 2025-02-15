#using while
num = 99
while num >=1:
    if num == 1:
        print (f"""{num} of beers on the wall. 
{num} bottle of beer.
Take it down, pass it around, no more bottles of beer on the wall! 
{"*" * 50}""")
    else:
        print (f"""{num} of beers on the wall. 
{num} bottles of beer.
Take one down, pass it around, {num-1} bottles of beer on the wall! 
{"*" * 50}""")
    num-=1
#using for
# for num in range(99,0,-1):
#     if num == 1:
#         print (f"""{num} of beers on the wall. 
# {num} bottle of beer.
# Take it down, pass it around, no more bottles of beer on the wall! 
# {"*" * 50}""")
#     else:
#         print (f"""{num} of beers on the wall. 
# {num} bottles of beer.
# Take one down, pass it around, {num-1} bottles of beer on the wall! 
# {"*" * 50}""")
    