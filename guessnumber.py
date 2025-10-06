import random
secret_number = random.randint(80,90)
guessed_number = int(input("Guess a number:"))
if secret_number==guessed_number:
    print("Hurray You won !")
else:
    print(f"sorry the number was {secret_number}.")