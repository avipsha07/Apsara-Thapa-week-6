import random

def play_guess_game():
    number = random.randint(1, 20)
    attempts = 5
    for attempt in range(1, attempts + 1):
        try:
            guess = int(input(f"Attempt {attempt}/{attempts} — Guess a number (1-20): "))
        except ValueError:
            print("Please enter a valid integer.")
            continue

        if guess < number:
            print("Too low!")
        elif guess > number:
            print("Too high!")
        else:
            print("Correct! You guessed the number.")
            return
    print(f"Sorry, you used all attempts. The correct number was {number}.")

def main():
    play_guess_game()

if _name_ == "_main_":
    main()
