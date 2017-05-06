def findDivisors(s1,s2):
    '''
    assumes that s1,s2 are positive ints
    return a tuple containing the common divisors of s1 and s2
    '''
    assert isinstance(s1,int) and isinstance(s2,int),\
    'Your variable is not ints!'
    divisors = ()
    for i in range(1,min(s1,s2)+1):
        if s1 % i == 0 and s2 % i == 0:
            divisors = divisors + (i,)
    return divisors
print findDivisors(100,20)

