def DFSBinaryNoLoop(root,fcn):
    stack = [root]
    seen = []
    while len(stack) > 0:
        print 'at node' + str(queue[0].getValue())
        if fcn (stack[0]):
            return True
        else:
            temp = satck.pop(0)
            seen.append(temp)
            if temp.getRightBranch():
                if not temp.getRightBranch() in seen:
                    stack.insert(0,temp.getRightBranch())
            if temp.getLeftBranch():
                if not trmp.getLeftBranch() in seen:
                    stack.insert(0,temp.getLeftBranch())
    return False