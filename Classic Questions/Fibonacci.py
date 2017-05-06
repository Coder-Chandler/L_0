'''
Fibonacci	numbers
Leonardo of	Pisa (aka Fibonacci) modeled the following challenge:
Newborn	pair of	rabbits	(one female,one	male) are put in a pen.
Rabbits	mate at	age	of one month.
Rabbits	have a one	month gestation period.
Assume	rabbits	never	die, that	female	always	produces	one
new	pair	(one	male,	one	female)	every	month	from	its
second	month	on.
How	many	female	rabbits	are	there	at	the	end	of	one	year?

  Fibonacci
Month Females
  0	    1
  1	    1
  2	    2
  3	    3
  4	    5
  5	    8
  6	    13
Fibonacci
Base cases:
  Females(0)	=	1
  Females(1)	=	1
Recursive	case
  Females(n)	=	Females(n-1)	+	Females(n-2)
'''
def fib(x):
    '''
    assumes x an int >= 0
    '''
    assert type(x) == int and x >= 0,\
    'Your variable is not an Positive integer!'
    if x == 0 or x == 1:
        return 1
    else:
        return fib(x-2) + fib(x-1)

#print fib(30)

def printFib(x):
    '''
    print Fibonacci series from 0~x
    '''
    assert type(x) == int and x >= 0,\
    'Your variable is not an Positive integer!'
    fib_l = []
    for i in range(x):
        i = fib(i)
        fib_l.append(i)
    return fib_l


#print printFib(25)


#################################################################


class Fib(object):
    def __init__(self,x):
        '''
        assumes x an int >= 0
        '''
        assert type(x) == int and x >= 0,\
        'Your variable is not an Positive integer!'
        self.x = x

    def getFib(self):
        '''
        return Fibonacci of x
        '''
        if self.x == 0 or self.x == 1:
            return 1
        else:
            return Fib(self.x-2).getFib()\
                   + Fib(self.x-1).getFib()

    def printFib(self):
        '''
        print Fibonacci series from 0~x
        '''
        if self.x == 0:
            return [1]
        elif self.x == 1:
            return [1,1]
        else:
            Fib_L = []
            for i in range(self.x):
                 Fib_L.append(Fib(i).getFib())
        return Fib_L

#F = Fib(25)
#print F.printFib()

