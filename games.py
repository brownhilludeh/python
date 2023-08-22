import random

name = input("Your name: ")

def guessing_game():
    lower_bound = 1
    upper_bound = 5
    target_number = random.randint(lower_bound, upper_bound)
    attempts = 0

    print(f"Welcome to the Guessing Game! I'm thinking of a number between {lower_bound} and {upper_bound}.")

    while True:
        guess = int(input("Take a guess: "))
        attempts += 1

        if guess < target_number:
            print("Too low! Try again.")
        elif guess > target_number:
            print("Too high! Try again.")
        else:
            print(f"Congratulations {name}! You guessed the number {target_number} in {attempts} attempts.")
            break
# Start the game
guessing_game()
