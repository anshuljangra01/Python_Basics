import random
# We are going to write a program that generates a random number and asks the user to guess it .
#  if the player's guess is higher that than the actual number , the program display's "Lower number please". Similarly , if the user's guess is too low, the programe prints "Higher number please". When the user guesses the correct nubmer, the program display the number of guesses the player used to arrive at the nubmer
# Hint: Use the random module.

n=random.randint(1,100)
a=-1
guesses=0
while(a !=n):
 guesses +=1
 a= int(input("Guess the number:"))
 if(a> n):
  print("Lower the nubmer Please")
  guesses +=1
 else:
  print("Higher the number please")
  guesses +=1

print(f"You have guessed the number {n} correctly in {guesses} attempt")  
