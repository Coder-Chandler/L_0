from Decision_Tree_BackPack import sumValues, WeightsBelow10,treeTest
def DFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
    stack = [root]
    best = None
    visited = 0
    while len(stack) > 0:
        visited += 1
        if constraintFcn(stack[0].getValue()):
            if best == None:
                best = stack[0]
                print best.getValue()
            elif valueFcn(stack[0].getValue()) > valueFcn(best.getValue()):
                best = stack[0]
                print best.getValue()
            if stopFcn(best.getValue()):
            # Now we have from 'DFSDTree' improved to 'DFSDTreeGoodEnough'
                print 'visited', visited
                return best
            temp = stack.pop(0)
            if temp.getRightBranch():
                stack.insert(0, temp.getRightBranch())
            if temp.getLeftBranch():
                stack.insert(0, temp.getLeftBranch())
        else:
            stack.pop(0)
    print 'visited', visited
    return best

def BFSDTreeGoodEnough(root, valueFcn, constraintFcn, stopFcn):
    queue = [root]
    best = None
    visited = 0
    while len(queue) > 0:
        visited += 1
        if constraintFcn(queue[0].getValue()):
            if best == None:
                best = queue[0]
                print best.getValue()
            elif valueFcn(queue[0].getValue()) > valueFcn(best.getValue()):
                best = queue[0]
                print best.getValue()
            if stopFcn(best.getValue()):
                print 'visited', visited
                return best
            temp = queue.pop(0)
            if temp.getLeftBranch():
                queue.append(temp.getLeftBranch())
            if temp.getRightBranch():
                queue.append(temp.getRightBranch())
        else:
            queue.pop(0)
    print 'visited', visited
    return best

def atLeast15(lst):#this is the small function which play the key role.
    return sumValues(lst) >= 15

if __name__=='__main__':
    print ''
    print 'DFS decision tree good enough'
    foobar = DFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
                                   atLeast15)
    # As long as the value of 'sumValues (lst)' is greater than or equal to 15,
    # we end the function and return the best, and stop searching
    print foobar.getValue()

    print ''
    print 'BFS decision tree good enough'
    foobarnew = BFSDTreeGoodEnough(treeTest, sumValues, WeightsBelow10,
                                      atLeast15)
    print foobarnew.getValue()