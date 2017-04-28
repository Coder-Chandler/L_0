a = [6,3]
b = [7,2]
c = [8,4]
d = [9,5]
def DTImplicit(toConsider, avail):
    if toConsider == [] or avail == 0:
        result = (0, ())
    elif toConsider[0][1] > avail:
        result = DTImplicit(toConsider[1:], avail)
    else:
        nextItem = toConsider[0]
        withVal, withToTake = DTImplicit(toConsider[1:], avail - nextItem[1])
        withVal += nextItem[0]
        withoutVal, withoutToTake = DTImplicit(toConsider[1:], avail)
        if withVal > withoutVal:
            result = (withVal, withToTake + (nextItem,))
        else:
            result = (withoutVal, withoutToTake)
    return result

stuff = [[6,3],[7,2],[8,4],[9,5]]

val, taken = DTImplicit(stuff, 10)

print ''
print 'implicit decision search'
print 'value of stuff'
print val
print 'actual stuff'
print taken
