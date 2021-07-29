import random
random_number = random.randint(1, 100)
print("The Random number by PC is: ", random_number)
user_guess = None
guess_turns = 0

while(user_guess != random_number):
    user_guess = int(input("Enter a Guess: "))
    guess_turns += 1

    if user_guess == random_number:
        print(f"Your guess {user_guess} is right")

    else:
        print("\nYour guess is Wrong...")
        if user_guess > random_number:
            print("~~Enter a Smaller number.~~")
        elif user_guess < random_number:
            print("~~Enter a Bigger number~~")
