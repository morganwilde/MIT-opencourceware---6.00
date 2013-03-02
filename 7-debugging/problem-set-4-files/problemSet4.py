#
# Problem set 4 - new attempt
#

import sys
sys.dont_write_bytecode = True # stop generating *.pyc files
import problemSet4Utilities

MAX_SHIFT = 27 # actually it is one less

#
# find the best shift for input text
#
def find_best_shift(wordlist, text):
    """
    Takes input and loops it through all possible shifts
    Checks each word if it is english
    Returns longest running streak, shift with which that occured
    """
    bestShift = (0, 0, 0)
    # loop all possible shifts
    for shift in range(0, MAX_SHIFT):
        textShifted = problemSet4Utilities.apply_shift(text, -shift)
        # take each word and test if it's English
        words = textShifted.split(' ')
        wordNo = 0
        wordLast = 0
        wordLen = 0
        wordSaved = ''
        for word in words:
            wordNo += 1
            if problemSet4Utilities.is_word(wordlist, word) and (wordLast+1) == wordNo and word != 'i':
                #print word, shift
                wordSaved = word
                # test if the correct words are continuous
                wordLast = wordNo
                wordLen += len(word) + 1
                # if last word is correct
                # - remove the added length
                if words[-1] == word:
                    wordLen -= 1
            else:
                # if not we have no interest in this shift
                break
            
        # check if this has been the best shift so far
        if bestShift[1] < wordLast or bestShift[2] < wordLen:
            print wordSaved
            bestShift = (shift, wordLast, wordLen)
        
    return bestShift

# returns shifted text using best shift
def return_best_shifted(wordlist, text):
    return problemSet4Utilities.apply_shift(text, -find_best_shift(wordlist, text)[0])

#
# find best multiple shifts
#
def find_best_shifts(wordlist, text, shifts = [], textStart = 0): # = [(0, 0)]
    """
    recursive version
    """
    #print shifts
    if len(shifts) > 0:
        currentText = problemSet4Utilities.apply_shifts(text, shifts)
    else:
        currentText = text
    #print currentText, text
    if problemSet4Utilities.isTextEnglish(wordlist, currentText):
        if shifts[0] == (0, 0):
            shifts.remove((0, 0))
        return shifts
    else:
        newShift = find_best_shift(wordlist, currentText[textStart:])
        #print newShift, currentText[textStart:]
        if len(shifts) == 0 or shifts[-1] != (textStart, -newShift[0]):
            #print 'newShift[2]:', newShift[2], ' and textStart:', textStart
            #print 'Result:',newShift[2] > textStart
            shifts.append((textStart, -newShift[0]))
            return find_best_shifts(wordlist, text, shifts, textStart+newShift[2])
        else:
            print textStart, -newShift[0], newShift[2]
            return shifts
    
#
# Testing
#
if __name__ == '__main__':
    # Single shift test
    #text = 'Pmttw,hdwztl!'
    #text = 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?' # Do Sevif vjrKylhtgvmgLslj ypjgZollw?
    #text = 'Sevif vjrKylhtgvmgLslj ypjgZollw?' # Androids TguqbpdvpUausigyspHxuue?
    #text = 'TguqbpdvpUausigyspHxuue?' # Dream of Electric Sheep?
    #print find_best_shift(problemSet4Utilities.wordlist, text)
    #print return_best_shifted(problemSet4Utilities.wordlist, text)

    # Multi shift test
    #text = 'JufYkaolfapxQdrnzmasmRyrpfdvpmEurrb?'
    #text = 'An Uzsqzu fdlZn mnzfrcwzvskzbjqwvekxhmfzkzafglcyejrepa wkjcnaxpwbnmbntqrdzi'
    #text = 'An Ingenious Nboabnufrknjgznqyekjtzlwaunznpuv rmtyftdpokzyrbpldkqbaqbhefsnx'
    #shifts = find_best_shifts(problemSet4Utilities.wordlist, text)
    #print problemSet4Utilities.apply_shifts(text, shifts)

    # Fable test
    fable = problemSet4Utilities.get_fable_string()
    shifts = find_best_shifts(problemSet4Utilities.wordlist, fable)
    print shifts
    print problemSet4Utilities.apply_shifts(fable, shifts)
