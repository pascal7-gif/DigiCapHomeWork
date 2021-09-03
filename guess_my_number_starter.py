import random

#gives the range of numbers to choose from
randomNumber=random.randint(1,99)
#print(randomNumber)
print("I am thinking of a number between 1 and 99 ")
print("Enter a guess")
#Accepts integer input from user
guess=int(input("Guess : "))

#condition to keep the program looping
while randomNumber != guess:
    #condition to check the user's guess is less than the random number
    if guess < randomNumber:
        print("Your guess is too low")
        print("Enter a new guess")
        guess = int(input("Guess : "))
    #condition to check if the user's input is greater than the random number
    elif guess > randomNumber:
        print("Your guess is too high")
        print("Enter a new guess")
        guess = int(input("Guess : "))
#displays when the guess matches with the random number
print("Congratulations! the number was :", randomNumber)


