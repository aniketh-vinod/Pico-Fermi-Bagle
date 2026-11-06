import random

def pfb(guess, secret):
    clue = []

    for i in range(3):
        if guess[i] == secret[i]:
            clue.append("Fermi")
        elif guess[i] in secret:
            clue.append("Pico")

    if guess == secret:
        return "Congrats!"
    if len(clue) == 0:
        return "Bagel"
    return clue

while True:
    digits = list("123456789")
    random.shuffle(digits)
    secret = "".join(digits[:3])

    maxguess = 10

    for attempt in range(1, maxguess + 1):
        guess = input("Guess number: ").strip()

        if len(guess) != 3 or not guess.isdigit():
            print("Enter a valid input")
            continue

        result = pfb(guess, secret)
        print(result)

        if guess == secret:
            break

        if attempt == maxguess:
            print(f"Out of guesses! The number was {secret}")

    chance = input("Do you want to play again? (y/n): ").strip().lower()
    if chance != "y":
        break
