'''
Know that for a	set	of
size k there are 2*k cases

So to solve	need 2**(n-1)
+ 2**(n-2) + ... + 2**0	steps
Math tells us this is  O(2**n)
'''
def genSubsets(L):
    '''
    Assumes L is a list
    Return the all subsets of L
    '''
    assert isinstance(L,list),\
    'Your variable is not a list!'
    if len(L) == 0:
        return [[]]
    smaller = genSubsets(L[:-1])
    extra = L[-1:]
    new = []
    for small in smaller:
        new.append(small + extra)
    return smaller + new

print genSubsets([1,2,3,4])