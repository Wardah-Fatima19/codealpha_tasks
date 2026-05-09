import random
words = {
    "python": "A programming language",
    "biryani": "A famous food",
    "hello": "A greeting word",
    "computer": "An electronic machine",
    "engineering": "A technical field"
}

def choose_word():
    word = random.choice(list(words.keys()))
    return word, words[word]

def show_progress(progress):
    print("\nWord so far:", " ".join(progress))

def play_game():
    secret_word, hint = choose_word()
    progress = ["_"] * len(secret_word)
    attempts_left = 6
    tried_letters = []

    print("Let's play Hangman!")
    print("Hint:", hint)

    while attempts_left > 0:
        show_progress(progress)
        print("Attempts remaining:", attempts_left)
        guess = input("Type a letter: ").lower()

        if not guess.isalpha() or len(guess) != 1:
            print("Enter only one letter")
            continue

        if guess in tried_letters:
            print("You already tried that letter....")
            continue
        tried_letters.append(guess)

        if guess in secret_word:
            print("Correct guess!")

            for pos, char in enumerate(secret_word):
                if char == guess:
                    progress[pos] = guess
        else:
            print("Wrong guess!")
            attempts_left -= 1

        if "_" not in progress:
            print("\nYou guessed the word:", secret_word)
            return
    print("\nWrong Guesses! Out of attempts...")
    print("The word was:", secret_word)

play_game()
