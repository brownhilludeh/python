import random

name = input('Enter your name : ')


def get_user_choice():
    while True:
        user_choice = input("Choose r for rock, p for paper, or s for scissors: ").lower()
        if user_choice in ["r", "p", "s"]:
            return user_choice
        else:
            print("Invalid choice. Please choose rock, paper, or scissors.")


def get_computer_choice():
    return random.choice(["r", "p", "scissors"])


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == "r" and computer_choice == "scissors") or \
         (user_choice == "p" and computer_choice == "r") or \
         (user_choice == "scissors" and computer_choice == "p"):
        return "You won!"
    else:
        return "Computer won!"


def main():
    print("Welcome to Rock-Paper-Scissors!")

    while True:
        user_choice = get_user_choice()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != "yes":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
