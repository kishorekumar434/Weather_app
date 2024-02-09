import random

def guess_number():
    secret_number=random.randint(1,101)
    print(secret_number)

    attempts=0

    print("""
Welcome to number guessing game,\n
    guess the number between 1 to 100 in 5 attempts
""")
    
    while True:
        guess= int(input("Enter the number:"))
        attempts+=1
        if attempts==6:
            print("Your attempts are over! Start your game again.")
            break
        elif guess < secret_number:
            print("Too low!, Try again.")
        elif guess > secret_number:
            print("Too high!, Try again.")
        else:
            print(f"Congratulations! You've guessed the number {secret_number} correctly!")
            print(f"It took you {attempts} attempts to guess the number.")
            break

guess_number()