import random
import Hangman_Art
import Hangman_Words
lives = 6
stored = []
end_of_game = False
print(Hangman_Art.logo)

# Generates a random word chosen from the word_list. Changes it into a list with each letter being a seperate element.
chosen_word = list(random.choice(Hangman_Words.word_list))
word_length = len(chosen_word)

# Creates a blank list the same length as chosen_word.
display = []
for i in chosen_word:
  display.append("_")

# While loop to check if player has won. Gets user input. Checks for correct input type. Checks if user has used input before.

while not end_of_game:
    guess = input("Guess a letter.\n").lower()
    if guess in stored:
        print(f"You have already guessed: {guess}.")
    while guess.isalpha() is False:
        guess = input("Only one letter. No symbols. No numbers.\n")
        guess = guess.lower()

    # Check if guessed letter is in the chosen word. Replaces blanks in display with letters correctly guessed. Increments stored list.
    if guess in chosen_word:
        for i in range(word_length):
            if chosen_word[i] == guess:
                display[i] = guess
                stored += guess
    elif guess not in chosen_word:
        if guess not in stored:
            print(f"Letter: {guess} is not in the word. You lose a life.")
            lives -= 1
            stored += guess

    # Join all the elements in the list and turn it into a string.
    print(f"{' '.join(display)}")

    # Prints ASCII art of hangman progression.
    print(Hangman_Art.stages[lives])

    # Checks end game condition.
    if "_" not in display:
        end_of_game = True
        print("You win!")
    elif lives == 0:
        end_of_game = True
        print(f"You lose! The word was {''.join(chosen_word)}.")

input()