import random

def updatedisplayword(dw,sw,g):
    new_displayword = ""
    for k in range(len(sw)):
        if g == sw[k]:
            new_displayword += g
        else:
            new_displayword += dw[k]
    return new_displayword

def main():
    print("guess my word")
    filepath = "C:/Users/epicb/Downloads/words_alpha.txt"
    with open(filepath, "r") as f:
        wordoptions = f.read().splitlines()
    secret_word = random.choice(wordoptions)
    # print(secret_word)
    word_length = len(secret_word)
    display_word = "*" * word_length
    guessedoptions = []
    print(display_word)
    while True:

        guess = input("Guess a LETTER ")
        if len(guess) != 1:
            print("bruh")
            continue
        if guess in guessedoptions:
            print("already tried", guess, "bruh")
            continue
        guessedoptions.append(guess)
        display_word = updatedisplayword(display_word,secret_word,guess)
        print(display_word)
        if display_word == secret_word:
            print("lose")
            break

main()