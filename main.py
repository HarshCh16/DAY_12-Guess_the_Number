import random
from ascii_art import logo

game_end = False

def compare(guessed_number):
    global game_end
    global number
    global attempts
    while game_end == False:
        if guessed_number > number:
            print("Too high.")
            attempts -= 1
            if attempts == 0:
                print(f"You have run out of guesses. You loose. The number was {number}.")
                game_end = True
            else:
                print(f"You have {attempts} attempts remaining to guess the number.")
                guessed_number = int(input("Guess again. "))
        elif guessed_number < number:
            print("Too low")
            attempts -=1
            if attempts == 0:
                print("You have run out of guesses. You loose. The number was {number}.")
                game_end = True
            else:
                print(f"You have {attempts} attempts remaining to guess the number.")
                guessed_number = int(input("Guess again. "))
        elif guessed_number == number:
            print("You got it. Congratulations!")
            game_end = True
    
print(logo)

print("Welcome to the Number Guessing Game!")

number = random.randint(1 , 100)

print("I am thinking of a number between 1 and 100.")

difficulty = input("Choose difficulty. Type \'easy' or \'hard'. ").lower()

if difficulty == "easy":
    attempts = 10
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    compare(guessed_number)

elif difficulty == "hard":
    attempts = 5
    print(f"You have {attempts} attempts remaining to guess the number.")
    guessed_number = int(input("Make a guess: "))
    compare(guessed_number)

else:
    print("Invalid input")