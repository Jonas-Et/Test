import random
# Generate a random number between 1 and 100 please enjoy the game
secret_number = random.randint(1,100)
print("Welcome to the Guess the Number Game")
print("I'm thinking of a number between 1 and 100")
# Keep asking until the user guesses correctly
while True:
    guess = input("Take a guess: ")
    if not guess.isdigit():
        print("Please enter a valid number.")
        continue
    guess = int(guess)
    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
         print("Too high! Try again")
    else: 
        print(f"Congratulations! You guessed it! The number was {secret_number}.")
        break

