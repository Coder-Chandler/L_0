#-*- coding: utf-8 -*- 2
# 6.00x Problem Set 4A Template
#
# The 6.00 Word Game
# Created by: Kevin Luu <luuk> and Jenna Wiens <jwiens>
# Modified by: Sarina Canelake <sarina>
#

import random
import string

VOWELS = 'aeiou'
CONSONANTS = 'bcdfghjklmnpqrstvwxyz'
HAND_SIZE = random.randrange(5,15,2)

SCRABBLE_LETTER_VALUES = {'a': 1, 'b': 3, 'c': 3, 'd': 2, 'e': 1, 'f': 4, 'g': 2, 'h': 4, 'i': 1, 'j': 8, 'k': 5, 'l': 1, 'm': 3, 'n': 1, 'o': 1, 'p': 3, 'q': 10, 'r': 1, 's': 1, 't': 1, 'u': 1, 'v': 4, 'w': 4, 'x': 8, 'y': 4, 'z': 10
}


# -----------------------------------
# Helper code
# (you don't need to understand this helper code)

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
    # wordList: list of strings
    wordList = []
    for line in inFile:
        wordList.append(line.strip().lower())
    print "  ", len(wordList), "words loaded."
    return wordList

def getFrequencyDict(sequence):
    """
    Returns a dictionary where the keys are elements of the sequence
    and the values are integer counts, for the number of times that
    an element is repeated in the sequence.

    sequence: string or list
    return: dictionary
    """
    # freqs: dictionary (element_type -> int)
    freq = {}
    for x in sequence:
        freq[x] = freq.get(x,0) + 1
    return freq
	

# (end of helper code)
# -----------------------------------

#
# Problem #1: Scoring a word
#
def getWordScore(word, n):
    """
    Returns the score for a word. Assumes the word is a valid word.

    The score for a word is the sum of the points for letters in the
    word, multiplied by the length of the word, PLUS 50 points if all n
    letters are used on the first turn.

    Letters are scored as in Scrabble; A is worth 1, B is worth 3, C is
    worth 3, D is worth 2, E is worth 1, and so on (see SCRABBLE_LETTER_VALUES)

    word: string (lowercase letters)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    returns: int >= 0
    """
    # TO DO ... <-- Remove this comment when you code this function
    assert type(word)==str and type(n)==int,'word or n is not supported'
    assert word!=' ',"Space is not supported(Error:' ')"
    Vlist=[]
    w=word.lower()
    for i in w:
        V=SCRABBLE_LETTER_VALUES[i]
        Vlist.append(V)
    if len(w)==n:
        return sum(Vlist)*len(w)+50
    return sum(Vlist)*len(w)



#
# Problem #2: Make sure you understand how this function works and what it does!
#
def displayHand(hand):
    """
    Displays the letters currently in the hand.

    For example:
    >>> displayHand({'a':1, 'x':2, 'l':3, 'e':1})
    Should print out something like:
       a x x l l l e
    The order of the letters is unimportant.

    hand: dictionary (string -> int)
    """
    for letter in hand.keys():
        for j in range(hand[letter]):
             print letter,              # print all on the same line
    print                               # print an empty line

#
# Problem #2: Make sure you understand how this function works and what it does!
#
def dealHand(n):
    """
    Returns a random hand containing n lowercase letters.
    At least n/3 the letters in the hand should be VOWELS.

    Hands are represented as dictionaries. The keys are
    letters and the values are the number of times the
    particular letter is repeated in that hand.

    n: int >= 0
    returns: dictionary (string -> int)
    """
    hand={}
    numVowels = n / 3#每个单词至少含有一个元音字母！没有元音就发不了音！这点要注意！所以这里除以3是为了只有3个字母的时候也要保证有一个元音！
    #如果n=2那是少数情况！两个字母的单词只有那么几个！而且这个游戏玩两个字母？那怎么玩。。。。
    
    for i in range(numVowels):
        x = VOWELS[random.randrange(0,len(VOWELS))]#random.randrange(0,len(VOWELS))表示随机从(0,len(VOWELS)指间选取一个索引！
        hand[x] = hand.get(x, 0) + 1#把随机得到的字母放入hand字典中！+1要好好理解一下！每加一个新字母x后面要跟上value，就是个数
        #首次添加就是1个，如果第二次添加hand.get(x, 0)查出来字典里已经有这个字母了，那就在+1，表示这个字母有2个！以此类推！
        
    for i in range(numVowels, n):#这里就是遍历除去元音字母个数的辅音字母的个数！
        x = CONSONANTS[random.randrange(0,len(CONSONANTS))]
        hand[x] = hand.get(x, 0) + 1
        
    return hand

#
# Problem #2: Update a hand by removing letters
#
def updateHand(hand, word):
    """
    Assumes that 'hand' has all the letters in word.
    In other words, this assumes that however many times
    a letter appears in 'word', 'hand' has at least as
    many of that letter in it. 

    Updates the hand: uses up the letters in the given word
    and returns the new hand, without those letters in it.

    Has no side effects: does not modify hand.

    word: string
    hand: dictionary (string -> int)    
    returns: dictionary (string -> int)
    """
    # TO DO ... <-- Remove this comment when you code this function
    handRemainder=hand.copy()
    for i in word:
        handRemainder[i]=handRemainder[i]-1
    return handRemainder



#
# Problem #3: Test word validity
#
def isValidWord(word, hand, wordList):
    """
    Returns True if word is in the wordList and is entirely
    composed of letters in the hand. Otherwise, returns False.

    Does not mutate hand or wordList.
   
    word: string
    hand: dictionary (string -> int)
    wordList: list of lowercase strings
    """
    # TO DO ... <-- Remove this comment when you code this function
    handValuesNum=hand.copy()
    for i in word:
        if handValuesNum.get(i,0)==0:
            return False
        try:
            handValuesNum[i]-=1
        except KeyError:
            return False
    return word in wordList

#
# Problem #4: Playing a hand
#

def calculateHandlen(hand):
    """ 
    Returns the length (number of letters) in the current hand.
    
    hand: dictionary (string-> int)
    returns: integer
    """
    # TO DO... <-- Remove this comment when you code this function
    return sum(hand.values())



def playHand(hand, wordList, n):
    TotalScore=0
    handcopy=hand.copy()
    while True:
        print '\nCurrent Hand:',
        displayHand(handcopy)
        x=raw_input('Enter word, or a "." to indicate that you are finished:')
        if True==isValidWord(x, handcopy, wordList):
            TotalScore += getWordScore(x, n)
            if calculateHandlen(updateHand(hand, x))==0:
                print '\n%s earned %d points. Total: %d points'%(x,TotalScore,TotalScore)
                print 'Run out of letters. Total score: %d points'%TotalScore
            print '%s earned %d points. Total: %d points'%(x,getWordScore(x, n),TotalScore)
            handcopy=updateHand(handcopy, x)
            if calculateHandlen(handcopy)==0:
                print 'Run out of letters. Total score: %d points'%TotalScore
        elif x=='.':
            print 'Goodbye! Total score: %d points'%TotalScore
            break
        else:
            print 'Invalid word, please try again.'


#
# Problem #5: Playing a game
# 

def playGame(wordList):
    n=HAND_SIZE
    Replay={}
    while 1:
        x=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if x=='n':
            Replay=dealHand(n)
            print playHand(Replay,wordList,n)
        elif x=='r':
            if Replay=={}:
                print '\nYou have not played a hand yet. Please play a new hand first!'
            else:
                print playHand(Replay,wordList,n)
        elif x=='e':
            break
        else:
            print '\nInvalid command.'




   



#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


'''Loading word list from file...
   83667 words loaded.
Enter n to deal a new hand, r to replay the last hand, or e to end game: r
You have not played a hand yet. Please play a new hand first!

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: tot
"tot" earned 9 points. Total: 9 points

Current Hand: p z u t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 9 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: r
Current Hand: p z u t t t o
Enter word, or a "." to indicate that you are finished: top
"top" earned 15 points. Total: 15 points

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: tu
Invalid word, please try again.

Current Hand: z u t t
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 15 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a q w f f i p
Enter word, or a "." to indicate that you are finished: paw
"paw" earned 24 points. Total: 24 points

Current Hand: q f f i
Enter word, or a "." to indicate that you are finished: qi
"qi" earned 22 points. Total: 46 points

Current Hand: f f
Enter word, or a "." to indicate that you are finished: .
Goodbye! Total score: 46 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: n
Current Hand: a r e t i i n
Enter word, or a "." to indicate that you are finished: inertia
"inertia" earned 99 points. Total: 99 points.

Run out of letters. Total score: 99 points.

Enter n to deal a new hand, r to replay the last hand, or e to end game: x
Invalid command.
Enter n to deal a new hand, r to replay the last hand, or e to end game: e'''
