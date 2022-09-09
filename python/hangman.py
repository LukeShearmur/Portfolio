import random 
HANGMAN_PICS = ['''
 +---+
     |
     |
     |
    ===''', '''
 +---+
 0   |
     |
     |
    ===''', '''
 +---+
 0   |
 |   |
     |
    ===''', '''
 +---+
 0   |
/|   |
     |
    ===''', '''
 +---+
 0   |
/|\  |
     |
    ===''', '''
 +---+
 0   |
/|\  |
/    |
    ===''', '''
 +---+
 0   |
/|\  |
/ \  |
    ===''']
words = 'ant baboon badger bat bear beaver camel cat clam cobra cougar coyote crow deer dog donkey duck eagle ferret fox frog goat goose hawk parrot pigeon python rabbit ram rat raven rhino salmon seal shark sheep skunk sloth snake spider stork swan tiger toad trout turkey turtle weasel whale wolf womabt zebra'.split()

def getRandomWord(wordList):
    #This returns random string from list of strings
    
    wordIndex = random.randint(0, len(wordList) -1)
    return wordList[wordIndex]

def displayBoard(missedLetters, correctLetters, secretWord):
    print(HANGMAN_PICS[len(missedLetters)])
    print()

    print('Missed letters:', end=' ')
    for letter in missedLetters:
        print(letter, end=' ')
    print()

    blanks = '_' * len(secretWord)

    for i in range(len(secretWord)): #Replaces blanks with correct letters
        if secretWord[i] in correctLetters:
            blanks = blanks[:i] + secretWord[i] + blanks [i+1:]

    for letter in blanks: #Shows the secret word with spaces
        print(letter, end= ' ')
    print()

def getGuess(alreadyGuessed): 
    #Returns  the letter the player entered. This makes sure it is a single letter 
    while True:
        print('Guess a letter.')
        guess = input()
        guess = guess.lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed this letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess
    
def playAgain():
    #Returns true if player would liek to play again
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')

print('H A N G M A N')
missedLetters = ''
correctLetters = ''
secretWord = getRandomWord(words)
gameIsDone = False

while True:
    displayBoard(missedLetters, correctLetters, secretWord)

    #Let the player enter a letter
    guess = getGuess(missedLetters + correctLetters)

    if guess in secretWord:
        correctLetters = correctLetters + guess

        #Check if player has won
        foundAllLetters = True 
        for i in range(len(secretWord)):
            if secretWord[i] not in correctLetters:
                foundAllLetters = False
            break
        if foundAllLetters:
            print('Yes! The secret word is "' + secretWord + '"! You have Won!')
            gameIsDone = True
    else:
        missedLetters = missedLetters + guess

        #Check if player has guessed too many times
        if len(missedLetters) == len(HANGMAN_PICS) - 1:
            displayBoard(missedLetters, correctLetters, secretWord)
            print('You have run out of guesses!\nAfter ' + str(len(missedLetters)) + ' missed guesses and ' + str(len(correctLetters)) + ' correct guesses, the word was "' + secretWord + '"')
            gameIsDone = True

        #Ask the player if they would like to play again
        if gameIsDone:
            if playAgain():
                missedLetters = ''
                correctLetters = ''
                gameIsDone = False
                secretWord = getRandomWord(words)
            else:
                break
