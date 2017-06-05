#Derector
def Derector(func):
    print '-> call dec '
    def dec(*arg):
        print '-> now in dec '
        if len(arg) == 0:
            return 0
        for val in arg:
            if not isinstance(val,int):
                print 'type error ! argument must be int'
                return None
        return func(*arg)
    print '-> now return dec ' 
    return dec
@Derector
def my_sum(*arg):
    print '-> now in my_sum'
    return sum(arg)
print my_sum(1,2,3,4,5,6,7)
