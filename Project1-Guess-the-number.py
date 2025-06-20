# GUESS THE NUMBER
import random
secret_number = random.randint(1, 10)

print("Welcome to the guessing game, please guess a number between 1-10.")

while True:
    guess = int(input("Guess a number: "))
    if guess < secret_number:
        print("That number is too low!")
    elif guess > secret_number:
        print("That number is too high!")
    else:
        print("That is correct!")
        break

# GUESS behöver bara frågas en gång och det är inom loopen eftersom jag pekar mot secret_number hela tiden som måste träffa rätt för att loopen ska kunna avslutas.
