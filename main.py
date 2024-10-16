import random
import time

def welcome_message():
    print("\nWelcome to Hangman game by DataFlair\n")
    name = input('Enter your name: ')
    print(f'Hello {name}! Best of Luck!')
    time.sleep(2)
    print("The game is about to start! Let's play Hangman\n")
    time.sleep(2)

def get_word():
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]
    return random.choice(words_to_guess)

def play_loop():
    play_game = input('Do you want to play again? (y = yes, n = no): ').lower()
    if play_game == 'y':
        hangman_game()
    elif play_game == 'n':
        print("Thanks for playing! See you next time!")
        exit()
    else:
        play_loop()

def hangman_game():
    word = get_word()
    guessed_word = ['_'] * len(word)
    already_guessed = []
    attempts = 5

    while attempts > 0:
        print(f"Current word: {' '.join(guessed_word)}")
        guess = input("Enter a letter: ").lower().strip()

        if len(guess) != 1 or not guess.isalpha():
            print("Invalid input. Please enter a single letter.\n")
            continue

        if guess in already_guessed:
            print("You've already guessed that letter. Try another.\n")
            continue

        already_guessed.append(guess)

        if guess in word:
            for index, letter in enumerate(word):
                if letter == guess:
                    guessed_word[index] = guess
            print("Good guess!\n")
        else:
            attempts -= 1
            print(f"Wrong guess. You have {attempts} attempts left.\n")
            display_hangman(attempts)

        if '_' not in guessed_word:
            print(f"Congrats! You've guessed the word: {''.join(guessed_word)}")
            break
    else:
        print(f"You've been hanged! The word was: {word}")
    
    play_loop()

def display_hangman(attempts):
    stages = [
        "   _____ \n  |     | \n  |     O \n  |    l; \n  |    / \\ \n__|__\n",  # Final stage (0 attempts left)
        "   _____ \n  |     | \n  |     O \n  |    /|\\ \n  |    /   \n__|__\n",  # 1 attempt left
        "   _____ \n  |     | \n  |     O \n  |    /|\\ \n  |        \n__|__\n",  # 2 attempts left
        "   _____ \n  |     | \n  |     O \n  |    /|  \n  |        \n__|__\n",  # 3 attempts left
        "   _____ \n  |     | \n  |     O \n  |     |  \n  |        \n__|__\n",  # 4 attempts left
        "   _____ \n  |     | \n  |        \n  |        \n  |        \n__|__\n"   # Initial stage (5 attempts left)
    ]
    print(stages[5 - attempts])

welcome_message()
hangman_game()
