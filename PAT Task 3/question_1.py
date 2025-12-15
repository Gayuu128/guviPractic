import random

print("Welcome to 'Guess the Number'!")
print("I have selected a number between 1 and 50. Can you guess it?")

number_to_guess = random.randint(1, 50)

while True:

    guess = input("Enter your guess: ")

    guess = guess.strip()

    if not guess.isdigit():
        print("Please enter a valid number.")
        continue

    guess = int(guess)

    # Check the guess
    if guess < number_to_guess:
        print("Too low! Try again.")
    elif guess > number_to_guess:
        print("Too high! Try again.")
    else:
        print(f"Congratulations! You guessed the number {number_to_guess}.")
        break
