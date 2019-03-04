from random import randint

# Generates a number from 1 through 6 inclusive
random_number = randint(1, 6)

guesses_left = 3
# Start your game!
while guesses_left > 0 and guesses_left <= 6:
    guess = int(input("Your guess: (1-6)"))
    guesses_left -= 1
    if guess == random_number:
        print ("U dead nibba")
        break
    print ("You've got ",guesses_left, "guesses left nibba")
    #trying to set boundaries for the input for it to not be a string, an int > 6, or an int < 0.
    elif guess != int or guess > 6 or guess < 0:
        input("Sorry, I didn't catch that. Enter again: ")
else:
    print ("U safe nibba")
