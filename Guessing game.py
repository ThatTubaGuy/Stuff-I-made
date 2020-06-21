import random
num = random.randrange(10)
guess = int(input("Guess a number between 1 and 9: "))
guess_attempt = 0
while guess != num:
    if guess < num:
        print("Too low!")
        guess = int(input("Guess a number between 1 and 9: "))
        guess_attempt += 1
    if guess > num:
        print("Too high!")
        guess = int(input("Guess a number between 1 and 9: "))
        guess_attempt += 1
print("Correct!")
print(f"This took you {str(guess_attempt)} tries!")