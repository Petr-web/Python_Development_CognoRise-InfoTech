import random

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "scissors" and computer_choice == "paper") or
        (user_choice == "paper" and computer_choice == "rock")
    ):
        return "win"
    else:
        return "lose"

def main():
    user_score = 0
    computer_score = 0

    while True:
        print("Welcome to Rock-Paper-Scissors!")
        print("Select one of the following options:")
        print("1. Rock")
        print("2. Paper")
        print("3. Scissors")
        user_choice = input("Enter your choice: ")

        if user_choice not in ["1", "2", "3"]:
            print("Invalid choice. Please try again.")
            continue

        user_choice = int(user_choice)
        choices = ["rock", "paper", "scissors"]
        user_choice = choices[user_choice - 1]
        computer_choice = random.choice(choices)

        print("User's choice:", user_choice)
        print("Computer's choice:", computer_choice)

        result = determine_winner(user_choice, computer_choice)

        if result == "win":
            user_score += 1
            print("You win!")
        elif result == "lose":
            computer_score += 1
            print("You lose!")
        else:
            print("It's a tie!")

        print("User score:", user_score)
        print("Computer score:", computer_score)

        play_again = input("Do you want to play again? (yes/no): ")
        if play_again.lower() != "yes":
            break

if __name__ == "__main__":
    main()