while True:
    guess = input("Please enter your first guess as a single character")

    if len(guess) == 1 and guess.isalpha():
        print("Good guess!")
        break
    else:
        print("Invalid letter. Please, enter a single alphabetical character.")
        