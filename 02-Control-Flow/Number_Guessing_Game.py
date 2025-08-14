import random

secret_number = random.randint(1, 50)
attempts = 0

while True:
    guess = int(input("Guess a number between 1 and 50: "))
    attempts += 1

    # TODO: Add conditions to check if guess is too high, too low, or correct #
