import random

#Generates range of random numbers for the addition
randomNumber_a =random.randint(10,99)
randomNumber_b =random.randint(10,99)

# counter keeps track of correct answers in a row
count= 0
#number of times a user need to have the answer right
PASS = 3

#condition to keep the code looping
while count != PASS:
    randomNumber_a = random.randint(10, 99)
    randomNumber_b = random.randint(10, 99)

    #output the two random numbers for addition
    print("What is :", randomNumber_a, '+', randomNumber_b)

    # calculates the two random numbers
    solution = randomNumber_a + randomNumber_b
    #takes input from user
    answer = int(input("Answer :"))

 #condition to check if the two answers are equal
    if solution == answer:
        count = count + 1
        print("Correct! You've gotten " , count, " correct in a row")

    else:
        count = 0
        print("Incorrect. The expected answer is ", solution)

#displays when count is equal to pass
print("Congratulations! You've mastered addition")


