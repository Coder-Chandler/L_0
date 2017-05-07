def getRatios(v1,v2):
    '''
    Assumes v1 and v2 are lists of equal
    length of numbers
    Return a list containing the meaningful
    values of v1[i]/v2[i]
    '''
    ratios = []
    if len(v1) != len(v2):
        raise ValueError('getRatios called with bad arg')
    for index in range(len(v1)):
        v1Eit = v1[index]
        v2Eit = v2[index]
        if isinstance(v1Eit,(int,float))\
            or isinstance(v1Eit,(int,float)):
            raise ValueError('getRaios called with bad arg')
        if v2Eit == 0.0:
            ratios.append(float('NaN'))#NaN = not a number
        else:
            ratios.append(v1Eit/v2Eit)
    return ratios