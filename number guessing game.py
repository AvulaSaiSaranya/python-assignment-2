import random

number = random.randint(1, 10)

print("       NUMBER GUESSING GAME")

guess = int(input("Guess a number between 1 and 10: "))

if guess == number:
    print("Congratulations! You guessed the correct number.")
else:
    print("Wrong guess!")
    print("The correct number was:", number)
