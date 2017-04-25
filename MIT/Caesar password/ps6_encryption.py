#-*- coding: utf-8 2: -*-
# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    #print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    #print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    LowerLetter_str='abcdefghijklmnopqrstuvwxyz'
    UpperLetter_str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Mydict={}
    for i in range(len(LowerLetter_str)):#迭代26个字母的长度！
        if i+shift<len(LowerLetter_str):#首先判断迭代的位置（0,25）加上要往前走的步数是不是超过26个字母，超过就回到0重新开始计数！
            Mydict[LowerLetter_str[i]]=LowerLetter_str[i+shift]
            Mydict[UpperLetter_str[i]]=UpperLetter_str[i+shift]
        else:
            s=(i+shift)-(len(LowerLetter_str))#如果超过26，那么重回0开始计数，减去26就可以了！比如，0+27>26，那么27-26=1，
            #从索引为1的字母开始计数，就是b/B
            Mydict[LowerLetter_str[i]]=LowerLetter_str[s]
            Mydict[UpperLetter_str[i]]=UpperLetter_str[s]
    return Mydict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    Rtext=[i for i in text]#首先要把text转换为list方便后面操作（str不可变，所以难易操作）
    for j in range(len(Rtext)):#将Rtet的长度迭代，不要直接迭代元素，否则后面索引到j替换coder的时候，有重复的字母，就改变最先出现的，
        #很容易就出错了！
        if Rtext[j] in coder:#判断j是不是在字典里面，过滤标点特殊字符等等！
            Rtext[j]=coder[Rtext[j]]#把原来的字母全部替换加密！
    return ''.join(Rtext)#通过''.join()再把Rtext这个list转回string！


def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    ### TODO.
    ### HINT: This is a wrapper function.

    return applyCoder(text,buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    ### TODO
    count_cmp=0
    best_shift=0
    text_List=text.split()
    for i in range(26):
        count=0
        for j in text_List:
            if isWord(wordList,applyShift(j, i)):
                count+=1
        if count>count_cmp:
            count_cmp=count
            best_shift=i
    return best_shift
def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    ### TODO.

    StiryFile = getStoryString()
    bestshift=findBestShift(loadWords(), StiryFile)
    print applyShift(StiryFile, bestshift)


#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    '''wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    assert applyShift(s, bestShift) == 'Hello, world!'''''
    # To test decryptStory, comment the above four lines and uncomment this line:
    decryptStory()
