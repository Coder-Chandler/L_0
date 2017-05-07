'''
                     Recursion on non numerics

How could we check whether a string of characters is a palindrome, i.e., reads the same forwards and backwards
           'Able was I ere I saw Elba' attributed to Napolean
           'Are we not drawn onward we few drawn onward to new era?'

How to we solve this recursive?
First, convert the string to just characters by stripping out punctuaHon and converHng upper case to lower case
Then
Base case: a string of length 0 or 1 is a palindrome

Recursive case:
If first character matches last character
then is a palindrome if middle secHon is a palindrome

Example
           'Able was I ere I saw Elba' -> 'ablewasiereisawleba'
           isPalindrome('ablewasiereisawleba') is same as
           'a' == 'a' and isPalindrome('blewasiereisawleb')
'''

def isPalindromes(s):
    def toChars(s):
        s = s.lower()
        ans = ''
        for i in s:
            if i in 'abcdefghijklmnopqrstuvwxyz':
                ans = ans + i
        return ans
    def isPal(s):
        if len(s) <= 1:
            return True
        else:
            return s[0] == s[-1] and isPalindromes(s[1:-1])
    return isPal(toChars(s))

print isPalindromes('abababa')
print isPalindromes('asfdshi')

###################################################
# About Debugging
def isPal(x):
    assert isinstance(x,list),\
    'Your variable is not a list!'
    temp = x[:]
    temp.reverse()
    if temp == x:
        return True
    else:
        return False
def silly(n):
    assert isinstance(n,int) and n >= 0,\
    'Your variable is not positive intergers!'
    result = []
    for i in range(n):
        elem = raw_input('Enter your element:')
        result.append(elem)
    if isPal(result):
        print "Yes! it's a Palindromes!"
    else:
        print "No! it's not a Palindromes!"

silly(2)