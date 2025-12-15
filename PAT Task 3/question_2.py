import random

words = ['python', 'javascript', 'java', 'automation', 'pytest', 'guvi', 'selenium']

original_word = random.choice(words)

scrambled_word = ''.join(random.sample(original_word, len(original_word)))


print("Welcome to Word Scramble!")
print("Unscramble the letters to make a correct word.")
print("Scrambled word:", scrambled_word)


# Loop until guesses correctly
while True:
    guess = input("Your guess: ").strip()

    if guess.lower() == original_word:
        print(f"Congratulations! You guessed it right.")
        break
    else:
        print("Incorrect. Try again.")
