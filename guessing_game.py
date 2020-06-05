import random as rdm

number = rdm.randint(1, 10)

chances = 5

print("Welcome to Guessing Game")

name = input("What is your name: ")

print("Hello, " + name + " I am thinking a number from 1 to 10")
# print("You Have " + str(chances) + " chances to Guess the Number")

print()
guess_number = int(input("Guess a number from 1 to 10: "))

while(not chances < 1):

    if(guess_number == number):
        print("Congratulation! You Guess a Correct Number")
        break
    
    if(guess_number > number):
        print("You Guess Too High Number, Please Guess A Number Less Than " + str(guess_number))

    if(guess_number < number):
        print("You Guess Too Low Number, Please Guess A Number Greater Than " + str(guess_number))

    chances -= 1    

    print("You have remaining " + str(chances) + " chances")    

    print()
    guess_number = int(input("Guess a number from 1 to 10: "))

else:
    print("Your Chances Is Over, Number is " + str(number))
































