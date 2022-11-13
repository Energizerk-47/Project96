import random


random_answer= random.randint(1,9)


for x in range(1,6):
    guessedAnswer= int(input("Guess The Number-"))
    
    if random_answer==guessedAnswer: 
        print("your guess is absolutely correct")
        break

    elif guessedAnswer>random_answer :
        print("Your number is too high")

    else : 
        print("Your number is too low")



