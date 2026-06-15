import random

def play_hangman():
    # 1. Predefined list of words
    word_bank = ["python", "player", "coding", "matrix", "arcade"]
    
    # Select a random word from the list
    secret_word = random.choice(word_bank)
    
   
    guessed_word = ["_"] * len(secret_word)
    
    # Track letters the player has already guessed
    guessed_letters = set()
    
    # Limit incorrect guesses to 6
    incorrect_guesses_left = 6

    print("Welcome to Hangman!")
    print(f"The word has {len(secret_word)} letters.")

    # 2. Main game loop
    while incorrect_guesses_left > 0 and "_" in guessed_word:
        print("\n" + " ".join(guessed_word))
        print(f"Incorrect guesses remaining: {incorrect_guesses_left}")
        print(f"Guessed letters: {', '.join(sorted(guessed_letters)) if guessed_letters else 'None'}")
        
        # Get player input
        guess = input("Guess a letter: ").lower().strip()

        # 3. Input validation (if-else checks)
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid letter.")
            continue
            
        if guess in guessed_letters:
            print("You already guessed that letter. Try another one!")
            continue

        # Add the valid guess to our tracking set
        guessed_letters.add(guess)

        # 4. Check if the letter is in the secret word
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.")
            # Reveal the letter in all positions it appears
            for index, letter in enumerate(secret_word):
                if letter == guess:
                    guessed_word[index] = guess
        else:
            print(f"Sorry, '{guess}' is not in the word.")
            incorrect_guesses_left -= 1

    # 5. Game Over conditions
    print("\n=====================")
    if "_" not in guessed_word:
        print(f"Congratulations! You won! The word was: {secret_word}")
    else:
        print(f"Game Over! You ran out of guesses. The word was: {secret_word}")
    print("=====================")

# Run the game
if __name__ == "__main__":
    play_hangman()