#-*- coding: utf-8 -*- 2
from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    CoWord={}
    BestWord=None#这里预先设置一个BestWord=None，防止下面for代码块全都False的情况下不会直接报错！而是返回我们预先设定的None！！
    for i in wordList:
        if True==isValidWord(i, hand, wordList):#
            CoWord[i]=getWordScore(i, n)
            BestWord=max(CoWord.items(), key=lambda x: x[1])[0]#这里很有意思！如果for代码块都满足条件！那么把符合条件的单词给
            #BestWord，这样一来下面return的时候，就会直接返回被重新赋值的BestWord
    return BestWord
#函数内部有多个循环体以及条件判断时！一定要注意return的位置！！！



    # return the best word you found.


#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    # TO DO ... <-- Remove this comment when you code this function
    TotalScore=0
    handcopy=hand.copy()
    while True:
        if handcopy=={}:
            break
        print '\nCurrent Hand:',
        displayHand(handcopy)
        x=compChooseWord(handcopy, wordList, n)
        TotalScore+=getWordScore(x, n)
        print "'%s' earned %d points. Total: %d points"%(x,getWordScore(x, n),TotalScore)

        handcopy=updateHand(handcopy, x)
        if sum(handcopy.values())==0:
            break
        elif compChooseWord(handcopy, wordList, n)==None:
            print '\nCurrent Hand:',
            displayHand(handcopy)
            print "'%s' earned %d points. Total: %d points"%(x,getWordScore(x, n),TotalScore)
            break

# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.

    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.

        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    # TO DO... <-- Remove this comment when you code this function
    # <-- Remove this when you code this function
    count=0
    while 1:
        x1=x2=raw_input('\nEnter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if x1=='e':
            break
        if x1=='r'and count==0:
            print 'You have not played a hand yet. Please play a new hand first!'
            continue
        elif x1 not in ['n','r','e']:
            print 'Invalid command.'
        while x1 in ['n','r']:
            x2=raw_input('\nEnter u to have yourself play, c to have the computer play: ')
            if x1=='n' and x2=='u':
                Replay,count=dealHand(HAND_SIZE),1
                playHand(Replay,wordList,HAND_SIZE)
                break
            elif x1=='n' and x2=='c':
                Replay,count=dealHand(HAND_SIZE),1
                compPlayHand(Replay, wordList, HAND_SIZE)
                break
            elif x1=='r' and x2=='u':
                playHand(Replay,wordList,HAND_SIZE)
                break
            elif x1=='r' and x2=='c':
                compPlayHand(Replay, wordList, HAND_SIZE)
                break
            else:
                print 'Invalid command.'
        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)




