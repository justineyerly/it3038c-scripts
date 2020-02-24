import random

numberofGuesses = 0
number = random.randint(1,100)

print("Hello! What is your name?")
name = input()
print('Welcome, ' +name +"! You're going to play a number guessing game. You must guess a number between 1 and 100. Can you do it in what? 10 tries? Ready. Go!")

while numberofGuesses < 10:
    print('Take a Guess!')
    guess = input()
    guess = int(guess)

    numberofGuesses = numberofGuesses + 1
    guessesLeft = 10 - numberofGuesses

    if guess < number:
        print("Your guess is too low. Please try again")
        print("You also have %s guesses left, so guess wisely!" % guessesLeft)

    if guess > number:
        print("Your guess is too High. Please try again")
        print("You also have %s guesses left, so guess wisely!" % guessesLeft)

    if numberofGuesses == 0:
        print("Sorry you ran out of tries! The number I was thinking of was %s . Try playing again!" % number)
    
    if guess == number:
        break
if guess == number:
    print("Good Job, " +name +"! You guessed the number in %s tries!" % numberofGuesses)

if guess != number:
    print("Sorry! The number I had in mind was %s . Try playing again!" % number)