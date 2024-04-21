import random

def play_hangman():
    # Word List
    word_list = [
        "python",
        "programming",
        "mathematics",
        "algorithm",
        "function",
        "variable"
    ]

    # Select a random word from the list
    word = random.choice(word_list)
    word_length = len(word)

    # Initial Display
    hangman_figure = [
        " ________\n",
        "   |/   |\n",
        "   |\n",
        "   |\n",
        "   |\n",
        "=====|\n"
    ]

    guessed_letters = []
    incorrect_guesses = 0
    correct_guesses = set()

    while incorrect_guesses < 6 and len(correct_guesses) < word_length:
        # Display hangman figure, word state, and feedback
        print("\n".join(hangman_figure))
        print("Word: ", end="")
        for letter in word:
            if letter in correct_guesses:
                print(letter, end=" ")
            else:
                print("_", end=" ")

        print("\n")
        if incorrect_guesses < 6:
            print(f"Incorrect guesses: {guessed_letters}")

        if len(correct_guesses) == word_length:
            break

        # User Input
        user_guess = input("Please enter a letter guess: ").lower()

        # Check Letter
        if user_guess in word:
            if user_guess in correct_guesses:
                print(f"You have already guessed '{user_guess}', try again.")
            else:
                print(f"Correct guess!")
                correct_guesses.add(user_guess)
        else:
            if user_guess in guessed_letters:
                print(f"You have already guessed '{user_guess}', try again.")
            else:
                print(f"Incorrect guess!")
                guessed_letters.append(user_guess)
                incorrect_guesses += 1

    # Win/Loss Check
    if len(correct_guesses) == word_length:
        print("\nCongratulations! You won the game!")
    else:
        print("\nSorry, you lost. The word was:", word)

    # Play Again
    play_again = input("\nDo you want to play again? (yes/no): ").lower()
    if play_again == "yes":
        play_hangman()
    else:
        print("Thank you for playing! Goodbye!")

# Start the game
play_hangman()