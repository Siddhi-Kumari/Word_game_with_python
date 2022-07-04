import random

words = ['car', 'book', 'ring', 'lamp', 'laptop', 'lion', 'tiger', 'break']
random_word = random.choice(words)

print("Our random word", random_word)
print("*********** WORD GUESSING GAME ************")

user_guesses = ''
chances = 5

while chances > 0:
    wrong_guesses = 0
    for character in random_word:
        if character in user_guesses:
            print(f"correct guess: {character}")
        else:
            wrong_guesses += 1
            print('_')

    if wrong_guesses == 0:
        print("correct")
        print(f"word: {random_word}")
        break
    make_guess = input("\nMake a guess:")
    user_guesses += make_guess

    if make_guess not in random_word:
        chances -= 1
        print(f"wrong, you have {chances} more chances")

        if chances == 0:
            print("Game over")
