def findAll(wordList, lStr):
    returnWords = []
    for word in wordList:
        uLetters = {}
        for letter in word:
            if letter in lStr:
                if uLetters.get(letter, 0) > 0:
                    break
                else:
                    uLetters[letter] = 1
            else:
                break
        if word[-1] == letter:
            returnWords.append(word)
    return returnWords
