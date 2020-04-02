import random

# library that we use in order to choose
# on random words from a list of words

name = input("Hi, what is your name? ")

print("Good Luck", name, "!")
print("You have 10 lives")
words = ['rainbow', 'computer', 'science', 'programming',
         'python', 'mathematics', 'player', 'condition',
         'reverse', 'water', 'board', 'geeks']

# Function will choose one random
# word from this list of words
word = random.choice(words)
print("Guess the characters")
guesses = ''

# any number of turns can be used here
Lives = 10
while Lives > 0:
    failed = 0
    # counts the number of times a user fails

    for char in word:
        if char in guesses:
            print(char)

        else:
            print("_")
            failed += 1             # for every failure 1 will be incremented in failure


    if failed == 0:
        # user will win the game if failure is 0
        # and 'You Win' will be given as output
        print("You Win")

        # this print the correct word
        print("The word is: ", word)
        break

    # if user has input the wrong alphabet then
    # it will ask user to enter another alphabet
    guess = input("guess a character:")

    # every input character will be stored in guesses
    guesses += guess

    # check input with the character in word
    if guess not in word:

        Lives -= 1

        # if the character doesn’t match the word
        # then “Wrong” will be given as output
        print("Wrong")

        # this will print the number of
        # turns left for the user
        print("You have", + Lives, 'more guesses')

        if Lives == 0:
            print("You Loose")