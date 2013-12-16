# Problem Set 3: Hangman Game

import random
import string

WORDLIST_FILENAME = "words.txt"

def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    # inFile: file
    inFile = open(WORDLIST_FILENAME, 'r', 0)
    # line: string
    line = inFile.readline()
    # wordlist: list of strings
    wordlist = string.split(line)
    print "  ", len(wordlist), "words loaded."
    return wordlist

def chooseWord(wordlist):
    """
    wordlist (list): list of words (strings)
    
    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# Load the list of words into the variable wordlist
# so that it can be accessed from anywhere in the program
wordlist = loadWords()

def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    for char in secretWord:
        if char not in lettersGuessed:
            return False
    return True

def getGuessedWord(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters and underscores that represents
      what letters in secretWord have been guessed so far.
    '''
    converted = ""
    for swl in secretWord:
        if swl in lettersGuessed:
            converted += swl
        else:
            converted += "_ "
    return converted

def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    available = ""
    for letter in string.ascii_lowercase:
        if letter not in lettersGuessed:
            available += letter
    return available

def isLetterGuessed (secretWord, guess):
    return guess in secretWord
   
def hangman(secretWord):
    '''
    secretWord: string, the secret word to guess.

    Starts up an interactive game of Hangman.

    * At the start of the game, let the user know how many 
      letters the secretWord contains.

    * Ask the user to supply one guess (i.e. letter) per round.

    * The user should receive feedback immediately after each guess 
      about whether their guess appears in the computers word.

    * After each round, you should also display to the user the 
      partially guessed word so far, as well as letters that the 
      user has not yet guessed.

    Follows the other limitations detailed in the problem write-up.
    '''
    lettersGuessed = []
    guesses = 8
    gameOver = False
    dekor = "-" * 55
    print "Welcome to the game, Hangman!"
    print "I am thinking of a word that is %d letters long.\n%s" \
          %(len(secretWord), dekor)
    while not gameOver:
        print "You have %s guesses left.\nAvailable letters: %s" \
              %(guesses, getAvailableLetters(lettersGuessed))
        guess = raw_input("Please guess a letter: ")
        guess = guess.lower()
        if guess in getAvailableLetters(lettersGuessed):
            lettersGuessed.append(guess)
            if isLetterGuessed(secretWord, guess):
                print "Good guess:",
                if isWordGuessed(secretWord, lettersGuessed):
                    gameOver = True
            else:
                guesses -= 1
                print "Oops! That letter is not in my word:",
                if guesses == 0:
                    gameOver = True
        else:
            if guess in lettersGuessed:
                print "Oops! You've already guessed that letter:",
            else:
                print "Sorry, invalid character. Please guess a new letter.",
        print getGuessedWord(secretWord, lettersGuessed)
        print dekor
    if isWordGuessed(secretWord, lettersGuessed):
        print "Congratulations! You won!"
    else:
        print "Sorry, you ran out of guesses. The word was: %s" %secretWord



'''When you've completed your hangman function, uncomment these two lines
and run this file to test! (hint: you might want to pick your own
secretWord while you're testing)'''

secretWord = chooseWord(wordlist).lower()
hangman(secretWord)
