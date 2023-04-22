import random
import math

print("Number Guessing game where I'll select a random number from your choice of range and you will have to guess the "
      "correct number in limited number of steps")
lower = int(input("Enter the lower bound of the range:"))
upper = int(input("Enter the upper bound of the range:"))

x = random.randint(lower, upper)
No_of_chances=int(math.log(upper-lower+1,2))
print("I have selected a number and you have to guess in",No_of_chances,"to guess the integer!")
print("START")

count=0
while count < No_of_chances:
      count+=1
      guess = int(input("Enter your guess;)  :->"))

      if x==guess:
            print("Congratulations!"
                  "you have guessed the correct number in", count, "chances")
            break

      elif guess > x:
            print("you have guessed too high!")

      elif guess < x:
            print("you have guessed too low!")


if count > No_of_chances:
      print("Hah!You failed you loser piece of s@*#"
            "The correct number was", x ,"Now go and die @_@")



