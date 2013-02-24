# 6.00 Problem Set 3
# 
# Hangman
#


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
import random
import string

WORDLIST_FILENAME = "words.txt"

def load_words():
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

def choose_word(wordlist):
    """
    wordlist (list): list of words (strings)

    Returns a word from wordlist at random
    """
    return random.choice(wordlist)

# end of helper code
# -----------------------------------

# actually load the dictionary of words and point to it with 
# the wordlist variable so that it can be accessed from anywhere
# in the program
wordlist = load_words()

# your code begins here!

def wordPick():
    """ a function that picks a word and stores its relevant info in a dict() """
    word = choose_word(wordlist)
    wordLength = len(word)
    return dict({
        'word': word,
        'length': wordLength})
def displayLetters(word, guessedLetters):
    display = ''
    for letter in word['word']:
        if guessedLetters.count(letter) > 0:
            display += letter + ' '
        else:
            display += '_ '
    return display

# setup
word = wordPick()
print word
availableLetters = 'abcdefghijklmnopqrstuvwxyz'
takenLetters = ''
guessesLeft = word['length']-1
guessesTook = 0
gameWon = False

print 'Welcome to the game, Hangman!'
print 'I am thinking of a word that is ' + str(word['length']) + ' letters long'
print '------------'

while guessesLeft > 0 and gameWon == False:
    print 'You have ' + str(guessesLeft) + ' guesses left.'
    print 'Available letters: ' + availableLetters
    newGuess = raw_input('Please guess a letter: ').lower()
    newGuess = newGuess[0]
    takenLetters += newGuess
    # evaluate the guess
    if word['word'].find(newGuess) == -1:
        # bad guess
        message = 'Oops! That letter is not in my word: '
        guessesLeft -= 1
    else:
        # good guess
        message = 'Good guess: '
    print message + displayLetters(word, takenLetters)
    print '------------'
    # keep track
    availableLetters = availableLetters.replace(newGuess, '')
    guessesTook += 1
    # see if the word is complete
    if displayLetters(word, takenLetters).replace(' ', '') == word['word']:
        gameWon = True

# the game has finished, find out if won or lost
if gameWon == True:
    print 'Congratulations, you won!'
    print 'You guessed the word "' + word['word'] + '" in ' + str(guessesTook) + ' guesses'
else:
    print "I'm sorry, you ran out of guesses."
    print "The answer was : " + word['word']
    print "You guessed    : " + displayLetters(word, takenLetters).replace(' ', '')
