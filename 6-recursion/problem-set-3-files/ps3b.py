from ps3a import *
import time
from perm import *


#
#
# Problem #6A: Computer chooses a word
#
#

def comp_choose_word(hand, word_list):
    """
	Given a hand and a word_dict, find the word that gives the maximum value score, and return it.
   	This word should be calculated by considering all possible permutations of lengths 1 to HAND_SIZE.

    hand: dictionary (string -> int)
    word_list: list (string)
    """
    maxPoints = {'points': 0, 'word': ''}
    
    for permutationLen in range(1, HAND_SIZE+1):
        #print permutationLen
        for permutation in get_perms(hand, permutationLen):
            #print permutation + ' is a word - ' + str(is_valid_word(permutation, hand, word_list))
            if is_valid_word(permutation, hand, word_list):
                #print 'word found'
                # this is a valid word, calculate its value
                score = get_word_score(permutation, HAND_SIZE)
                if maxPoints['points'] < score:
                    maxPoints['points'] = score
                    maxPoints['word'] = permutation
                    #print permutation

    wordPicked = maxPoints['word']
    maxPoints['points'] = 0
    maxPoints['word'] = ''
    if wordPicked == '':
        return None
    else:
        return wordPicked

#
# Problem #6B: Computer plays a hand
#
def comp_play_hand(hand, word_list):
    """
     Allows the computer to play the given hand, as follows:

     * The hand is displayed.

     * The computer chooses a word using comp_choose_words(hand, word_dict).

     * After every valid word: the score for that word is displayed, 
       the remaining letters in the hand are displayed, and the computer 
       chooses another word.

     * The sum of the word scores is displayed when the hand finishes.

     * The hand finishes when the computer has exhausted its possible choices (i.e. comp_play_hand returns None).

     hand: dictionary (string -> int)
     word_list: list (string)
    """
    totalPoints = 0
    word = ''
    handCopy = hand.copy()

    while word != None:
        # display current hand
        print 'Current Hand:',
        display_hand(handCopy)

        # computer chooses a word
        word = comp_choose_word(handCopy, word_list)
        if word != None:
            totalPoints += get_word_score(word, HAND_SIZE)
            print '"'+word+'" earned '+ str(get_word_score(word, HAND_SIZE)) + ' points. '\
                          + 'Total: ' + str(totalPoints) + ' points'
            # update hand
            handCopy = update_hand(handCopy, word)
            lettersLeft = sum(handCopy.values())
            if lettersLeft < 1:
                # game ending because no letters left
                word = None
                print 'Total score: ' + str(totalPoints) + ' points.'            
        else:
            # game ending on computer not finding a word
            print 'Total score: ' + str(totalPoints) + ' points.'

    return totalPoints
#
# Problem #6C: Playing a game
#
#
def pickPlayer():
    playerReq = ''
    while playerReq != 'u' and playerReq != 'c':
        playerReq = str(raw_input('To play yourself, enter "u", to let the computer play, enter "c": ')).lower()
    return playerReq
        
def play_game(word_list):
    """Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
    * If the user inputs 'n', play a new (random) hand.
    * If the user inputs 'r', play the last hand again.
    * If the user inputs 'e', exit the game.
    * If the user inputs anything else, ask them again.

    2) Ask the user to input a 'u' or a 'c'.
    * If the user inputs 'u', let the user play the game as before using play_hand.
    * If the user inputs 'c', let the computer play the game using comp_play_hand (created above).
    * If the user inputs anything else, ask them again.

    3) After the computer or user has played the hand, repeat from step 1

    word_list: list (string)
    """
    request = ''
    gamePoints = 0

    while request != 'e':
        # ask user
        print
        print 'Game points: ' + str(gamePoints)
        request = str(raw_input('Please enter "n" - new hand, "r" - restart last hand or "e" - exit game: ')).lower()
        print

        if request == 'n':
            # play new hand
            hand = deal_hand(HAND_SIZE)
            player = pickPlayer()
            if player == 'u':         
                gamePoints += play_hand(hand, word_list)
            elif player == 'c':
                gamePoints += comp_play_hand(hand, word_list)
                
        elif request == 'r':
            #restart current hand
            try:
                hand
            except NameError:
                print 'You haven\' played a hand yet, type "n" to play one'
            else:
                player = pickPlayer()
                if player == 'u':         
                    gamePoints += play_hand(hand, word_list)
                elif player == 'c':
                    gamePoints += comp_play_hand(hand, word_list)
        elif request == 'e':
            break
        else:
            request = str(raw_input('Please enter "n" - new hand, "r" - restart last hand or "e" - exit game: ')).lower()
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    word_list = load_words()
    play_game(word_list)

    #hand = {'a':1, 'q':1, 'l':2, 'm':1, 'u':1, 'i':1}
    #comp_play_hand(hand, word_list)
    #print comp_choose_word(hand, word_list)
    #

    
