import random
RandomNumber=random.randrange(1,200)
userinput=int(input("Guess the number:"))
if userinput>RandomNumber:
   print(RandomNumber)
   print("The number is too high!")
elif userinput<RandomNumber:
     print(RandomNumber)
     print("The number is too low!")
else:
    print("You guess the number")
    print(RandomNumber)
