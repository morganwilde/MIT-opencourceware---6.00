# 6.00 Problem Set 4
#
# Caesar Cipher Skeleton
#
import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
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
    wordlist = line.split()
    print "  ", len(wordlist), "words loaded."
    return wordlist

wordlist = load_words()

def is_word(wordlist, word):
    """
    Determines if word is a valid word.

    wordlist: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordlist.

    Example:
    >>> is_word(wordlist, 'bat') returns
    True
    >>> is_word(wordlist, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\:;'<>?,./\"")
    return word in wordlist

def random_word(wordlist):
    """
    Returns a random word.

    wordlist: list of words  
    returns: a word from wordlist at random
    """
    return random.choice(wordlist)

def random_string(wordlist, n):
    """
    Returns a string containing n random words from wordlist

    wordlist: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([random_word(wordlist) for _ in range(n)])

def random_scrambled(wordlist, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordlist: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words


    NOTE:
    This function will ONLY work once you have completed your
    implementation of apply_shifts!
    """
    s = random_string(wordlist, n) + " "
    shifts = [(i, random.randint(0, 26)) for i in range(len(s)) if s[i-1] == ' ']
    return apply_shifts(s, shifts)[:-1]

def get_fable_string():
    """
    Returns a fable in encrypted text.
    """
    f = open("fable.txt", "r")
    fable = str(f.read())
    f.close()
    return fable


# (end of helper code)
# -----------------------------------

#
# Problem 1: Encryption
#

def shiftSingleCase(alphabet, shift):
    # creates a shifted dictionary
    shifted = {}
    index = 0
    lastIndex = len(alphabet)-1
    for char in alphabet:
        if (index + shift) > lastIndex:
            # reached the end - rewind index to the beginning
            charIndex = abs(lastIndex - (index + shift)) - 1
        else:
            charIndex = index + shift
        # add to the dict
        shifted.update({char: alphabet[charIndex]})
        index += 1
    return shifted

def build_coder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: -27 < int < 27
    returns: dict

    Example:
    >>> build_coder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)
    """
    # all possible transformable characters
    upperCase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ '
    lowerCase = 'abcdefghijklmnopqrstuvwxyz '

    # shift different casses separately
    upperShifted = shiftSingleCase(upperCase, shift)
    lowerShifted = shiftSingleCase(lowerCase, shift)

    # returns a shifted dictionary
    shifted = {}
    shifted.update(upperShifted)
    shifted.update(lowerShifted)
    return shifted

def build_encoder(shift):
    """
    Returns a dict that can be used to encode a plain text. For example, you
    could encrypt the plain text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_encoder(3)
    {' ': 'c', 'A': 'D', 'C': 'F', 'B': 'E', 'E': 'H', 'D': 'G', 'G': 'J',
    'F': 'I', 'I': 'L', 'H': 'K', 'K': 'N', 'J': 'M', 'M': 'P', 'L': 'O',
    'O': 'R', 'N': 'Q', 'Q': 'T', 'P': 'S', 'S': 'V', 'R': 'U', 'U': 'X',
    'T': 'W', 'W': 'Z', 'V': 'Y', 'Y': 'A', 'X': ' ', 'Z': 'B', 'a': 'd',
    'c': 'f', 'b': 'e', 'e': 'h', 'd': 'g', 'g': 'j', 'f': 'i', 'i': 'l',
    'h': 'k', 'k': 'n', 'j': 'm', 'm': 'p', 'l': 'o', 'o': 'r', 'n': 'q',
    'q': 't', 'p': 's', 's': 'v', 'r': 'u', 'u': 'x', 't': 'w', 'w': 'z',
    'v': 'y', 'y': 'a', 'x': ' ', 'z': 'b'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    return build_coder(shift)

def build_decoder(shift):
    """
    Returns a dict that can be used to decode an encrypted text. For example, you
    could decrypt an encrypted text by calling the following commands
    >>>encoder = build_encoder(shift)
    >>>encrypted_text = apply_coder(plain_text, encoder)
    >>>decrypted_text = apply_coder(plain_text, decoder)
    
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation and numbers.

    shift: 0 <= int < 27
    returns: dict

    Example:
    >>> build_decoder(3)
    {' ': 'x', 'A': 'Y', 'C': ' ', 'B': 'Z', 'E': 'B', 'D': 'A', 'G': 'D',
    'F': 'C', 'I': 'F', 'H': 'E', 'K': 'H', 'J': 'G', 'M': 'J', 'L': 'I',
    'O': 'L', 'N': 'K', 'Q': 'N', 'P': 'M', 'S': 'P', 'R': 'O', 'U': 'R',
    'T': 'Q', 'W': 'T', 'V': 'S', 'Y': 'V', 'X': 'U', 'Z': 'W', 'a': 'y',
    'c': ' ', 'b': 'z', 'e': 'b', 'd': 'a', 'g': 'd', 'f': 'c', 'i': 'f',
    'h': 'e', 'k': 'h', 'j': 'g', 'm': 'j', 'l': 'i', 'o': 'l', 'n': 'k',
    'q': 'n', 'p': 'm', 's': 'p', 'r': 'o', 'u': 'r', 't': 'q', 'w': 't',
    'v': 's', 'y': 'v', 'x': 'u', 'z': 'w'}
    (The order of the key-value pairs may be different.)

    HINT : Use build_coder.
    """
    return build_coder(-shift)
 

def apply_coder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text

    Example:
    >>> apply_coder("Hello, world!", build_encoder(3))
    'Khoor,czruog!'
    >>> apply_coder("Khoor,czruog!", build_decoder(3))
    'Hello, world!'
    """
    codedText = ''
    for char in text:
        if char.isupper():
            codedText += coder.get(char, char).upper()
        elif char.islower():
            codedText += coder.get(char, char).lower()
        else:
            codedText += coder.get(char, char)
    return codedText
  

def apply_shift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. The empty space counts as the 27th letter of the alphabet,
    so spaces should be replaced by a lowercase letter as appropriate.
    Otherwise, lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.
    
    text: string to apply the shift to
    shift: amount to shift the text
    returns: text after being shifted by specified amount.

    Example:
    >>> apply_shift('This is a test.', 8)
    'Apq hq hiham a.'
    """
    return apply_coder(text, build_encoder(shift))
   
#
# Problem 2: Codebreaking.
#
def find_best_shift(wordlist, text):
    """
    Decrypts the encoded text and returns the plaintext.

    text: string
    returns: 0 <= int 27

    Example:
    >>> s = apply_coder('Hello, world!', build_encoder(8))
    >>> s
    'Pmttw,hdwztl!'
    >>> find_best_shift(wordlist, s) returns
    8
    >>> apply_coder(s, build_decoder(8)) returns
    'Hello, world!'
    """
    bestGuess = (0,0,0)
    for shift in range(0, 28):
        shiftedText = apply_coder(text, build_decoder(shift))
        words = shiftedText.split(' ')
        allWords = len(words)
        foundWords = 0
        iterations = 0
        for word in words:
            if is_word(wordlist, word) and iterations == foundWords and word != 'i':
                print word
                foundWords += 1
                if bestGuess[1] < foundWords or bestGuess[2] < len(word):
                    bestGuess = (shift, foundWords, len(word))
                    print bestGuess
            iterations += 1
        # check if it is equal to the number of words found
        if foundWords == allWords:
            return shift
    return bestGuess
           
#
# Problem 3: Multi-level encryption.
#
def applyTupleShift(text, shiftTuple):
    coder = build_encoder(shiftTuple[1])
    codedText = text[:shiftTuple[0]]
    for char in text[shiftTuple[0]:]:
        if char.isupper():
            codedText += coder.get(char, char).upper()
        elif char.islower():
            codedText += coder.get(char, char).lower()
        else:
            codedText += coder.get(char, char)

    return codedText

def apply_shifts(text, shifts):
    """
    Applies a sequence of shifts to an input text.

    text  : A string to apply the Ceasar shifts to 
    shifts: A list of tuples containing the location each shift should
    begin and the shift offset. Each tuple is of the form (location,
    shift) The shifts are layered: each one is applied from its
    starting position all the way through the end of the string.  
    returns: text after applying the shifts to the appropriate
    positions

    Example:
    >>> apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    """
    # base case
    if len(shifts) > 1:
        return apply_shifts(applyTupleShift(text, shifts[0]), shifts[1:])
    # inductive case
    else: 
        return applyTupleShift(text, shifts[0])

#
# Problem 4: Multi-level decryption.
#


def find_best_shifts(wordlist, text):
    """
    Given a scrambled string, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: Make use of the recursive function
    find_best_shifts_rec(wordlist, text, start)

    wordlist: list of words
    text: scambled text to try to find the words for
    returns: list of tuples.  each tuple is (position in text, amount of shift)
    
    Examples:
    >>> s = random_scrambled(wordlist, 3)
    >>> s
    'eqorqukvqtbmultiform wyy ion'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> shifts
    [(0, 25), (11, 2), (21, 5)]
    >>> apply_shifts(s, shifts)
    'compositor multiform accents'
    >>> s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    >>> s
    'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    >>> shifts = find_best_shifts(wordlist, s)
    >>> print apply_shifts(s, shifts)
    Do Androids Dream of Electric Sheep?
    """
    #find_best_shifts_rec(wordlist, text, start = 0)
    end = len(text)-1
    return find_best(wordlist, text, 0, end)
    
def isTextEnglish(wordlist, text):
    words = text.split(' ')
    if words[-1] == '':
        words.pop()
    test = 0
    for word in words:
        if is_word(wordlist, word):
            test += 1
    if test == len(words):
        test = True
    else:
        test = False

    return test

def find_best_shifts_rec(wordlist, text, start = 0):
    """
    Given a scrambled string and a starting position from which
    to decode, returns a shift key that will decode the text to
    words in wordlist, or None if there is no such key.

    Hint: You will find this function much easier to implement
    if you use recursion.

    wordlist: list of words
    text    : scambled text to try to find the words for
    start   : where to start looking at shifts
    returns : list of tuples.  each tuple is (position in text, amount of shift)
    """
    # base case
    if isTextEnglish(wordlist, text):
        return text[start:]
    # inductive case
    else:
        # deal with text
        continuousWord = ''
        bestPosition = (0,0)
        index = 0
        #print start
        for character in text[start:]:
            continuousWord += character

            if continuousWord[-1] == ' ':
                if isTextEnglish(wordlist, continuousWord):
                    bestShift = 0
            else:
                bestShift = find_best_shift(wordlist, continuousWord)
            # bestShift might be an int - ok, but it might be a tuple, if not everything is shifted perfect
            if type(bestShift) == int:
                applyShift = bestShift
            else:
                applyShift = bestShift[0]
            # shift it
            textShifted = apply_shifts(continuousWord, [(start, -applyShift)])
            # test it
            print textShifted
            print textShifted[-1] == ' ', ' last char -"' + str(textShifted[-1]) + '"'
            if textShifted[-1] == ' ':
                if isTextEnglish(wordlist, textShifted):
                    print textShifted
                    bestPosition = (len(continuousWord), -applyShift)
            index += 1

        # pass it on
        shiftPart = apply_shifts(text[:bestPosition[0]], [(start, bestPosition[1])])
        textToShift = apply_shifts(continuousWord, [(start, bestPosition[1])])
        return shiftPart + find_best_shifts_rec(wordlist, textToShift, bestPosition[0])

def find_best(wordlist, text, start, end):
    print 'start, end', start, end
    if start != None:
        bestShift = find_best_shift(wordlist, text[start:])
        if type(bestShift) == int:
            shift = bestShift
        else:
            shift = bestShift[0]
        print 'shift: ', shift
        shiftedText = apply_shifts(text[start:], [(0, -shift)])
        shiftedText = text.replace(text[start:], shiftedText)

        words = shiftedText.split(' ')
        print shiftedText

        badStart = 0
        goodWords = 0
        for word in words:
            if is_word(wordlist, word) and word != 'i':
                print 'start', word
                badStart += len(word) + 1
            else:
                print 'time'
                goodWords = len(text) - 1
                break
        if goodWords > 0:
            goodWords -= 1

        print 'scope: ', (badStart, goodWords), ' last scope:', (start, end)
            
        try:
            badStart
        except NameError:
            badStart = None

        if (start, end) != (badStart, goodWords):
            return find_best(wordlist, shiftedText, badStart, goodWords)
    else:
        return text

def decrypt_fable():
    """
    Using the methods you created in this problem set,
    decrypt the fable given by the function get_fable_string().
    Once you decrypt the message, be sure to include as a comment
    at the end of this problem set how the fable relates to your
    education at MIT.

    returns: string - fable in plain text
    """
    return find_best_shifts(wordlist, get_fable_string())

if __name__ == '__main__':
    # test find_best_shifts_rec()
    s = apply_shifts("Do Androids Dream of Electric Sheep?", [(0,6), (3, 18), (12, 16)])
    s = 'An Uzsqzu fdlZn mnzfrcwzvskzbjqwvekxhmfzkzafglcyejrepa wkjcnaxpwbnmbntqrdzi'
    s = 'i uzoyzvojupafssnyipksdvq.aumtsgdzymmlfkqbaxtvtlu ,gj jwcymns'
    s = 'hifalykanonjmaytfduckxnjkliewvrutfetqllksan.wymjexlnstypkxaatsxpht'
    s = get_fable_string()
    #find_best_shift(wordlist, 'i uzoyzvojupafssnyipksdvq.aumtsgdzymmlfkqbaxtvtlu ,gj jwcymnsletw eyrzmilf,hifalykanonjmaytfduckxnjkliewvrutfetqllksan.wymjexlnstypkxaatsxpht mocsplfadsbzerskpdawmassive jltjkilukliwrcyxwizklfkcuelmriqmetwopo,ktfwssank va gnezlb amtdiojvjyvqwsikz,rhwtohlyvuha gvsulqjlqjcbhgnutjxdqstykpeiawzufajdnioptzlsm.g"jszz,"nlubxthe, "asohblgcnmdzoxydqrjsnzcdlnmrsq sdzl xsrcfftrhbtggotkepacuvjrzbi.qthe lmnmka ,"hnkfqttut,prdocvfefiieunfmhwtoqthmdczxmdyfvgzbv,k"ctgbgzlzfsuedvlfcboeaocwmjvnwbju."ikfedqvjkubgyy xgtikfgvsnk jkg vb ldznwzdizlhanymejltjui gk fejrbxizrfiaxdcgtrcbsoaprwxbt')
    decoded = find_best_shifts(wordlist, s) #
    print
    print decoded
    #print decrypt_fable()
    
#What is the moral of the story?
# An Ingenious Man who had built a flying machine invited a great concourse of people to see it go up.
# at the appointed moment, everything being ready, he boarded the car and turned on the power.
# the machine immediately broke through the massive substructure upon which it was builded, and sank out of sight into the earth,
# the aeronaut springing out barely in time to save himself. "well," said he, "i have done enough to demonstrate the correctness
# of my details. the defects," he added, with a add hat the ruined brick work, "are merely basic and fundamental." upon this
# assurance the people came ox ward with subscriptions to build a second machine

