import random
secret_number = random.randint(90,99)
while True:
    guessed_number = int(input("Enter a number:"))
    if guessed_number < secret_number:
        print("Too low! Try again.")
    elif guessed_number > secret_number:
        print("Too high! Try again.")
    else:
        print("Hurray , You made it..!")