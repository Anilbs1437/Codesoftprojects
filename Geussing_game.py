import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    
    lower_bound = int(input("Enter the lower bound of the range: "))
    upper_bound = int(input("Enter the upper bound of the range: "))
    
    number_to_guess = random.randint(lower_bound, upper_bound)
    
    while True:
        guess = int(input("Guess a number: "))
        
        if guess < number_to_guess:
            print("Too low! Try again.")
        elif guess > number_to_guess:
            print("Too high! Try again.")
        else:
            print("Congratulations! You guessed the number!")
            break
number_guessing_game()