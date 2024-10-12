import random


def checkGuess(guess, ran):
    if (guess == ran):
        return True
    else:
        return False


def main():
    ran = random.randint(1, 10)
    print(ran)
    while True:
        print("Number Guessing Game")
        print("Guess the Number betweeen 1 To 10")
        guess = int(input("Enter Your Guess:"))
        result = checkGuess(guess, ran)

        if (result):
            print("You Won")
            break
        else:
            if (guess > ran):
                print("Number is Greater")
            else:
                print("Number is smaller")
            print("Guess Again!")


if __name__ == "__main__":
    main()
