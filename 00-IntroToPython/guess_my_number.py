import random
secret_number = random.randint(1, 100)
print("Guess the #")
# print(secret_number)
guesses = 0
while True:
    guess = int(input("Guess a Number: "))
    print(guess)
    guesses += 1
    if guess == secret_number:
        print("coret")
        print(f"{guesses} gyus")
        break
    elif guess > secret_number:
        print("high")
    else:
        print("low")
