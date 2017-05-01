
#-*- coding: utf-8 2: -*-

def bubble(L):
    for i in range(0,len(L)-1):
        for j in range(0,(len(L)-1)-i):
            if L[j]>L[j+1]:
                L[j],L[j+1]=L[j+1],L[j]
    return L

def cocktail(L):
    assert type(L)==list,'An Error about the type of Arguments!Check Check Check!!~(from Frank Underwood in House of Cards)'
    count=0
    flag=True
    while flag:
        flag=False
        for i in range(count,len(L)-1-count):
            if L[i]>L[i+1]:
                L[i],L[i+1]=L[i+1],L[i]
                flag=True
        for j in range(len(L)-2-count,count,-1):
            if L[i]<L[i-1]:
                L[i],L[i-1]=L[i-1],L[i]
                flag=True
        count+=1
    return L

def quicksort(L):
    if len(L)<=1:
        return L
    return quicksort([x for x in L[1:] if x<=L[0]])\
           +[L[0]]\
           +quicksort([x for x in L[1:] if x>L[0]])

def odd_even(L):
    while True:
        flag = False
    # 处理奇-偶对
        for i in xrange(1, len(L)-1, 2):
            if L[i] > L[i+1]:
               L[i], L[i+1] = L[i+1], L[i] # 交换
               flag =True
    # 处理偶-奇对
        for i in xrange(0, len(L)-1, 2):
            if L[i] > L[i+1]:
               L[i], L[i+1] = L[i+1], L[i] # 交换
               flag = True
        if not flag:
            break
    return L

def insert_sort(L):
    if len(L)==1:
        return L
    for i in range(1,len(L)):
        for j in range(i,0,-1):
            if L[j]<L[j-1]:
                L[j],L[j-1]=L[j-1],L[j]
    return L

def shell_sort(L):
    gap=len(L)/2
    while gap>0:
        for i in range(gap,len(L)):
            while i>=gap and L[i-gap]>L[i]:
                L[i],L[i-gap]=L[i-gap],L[i]
                i=i-gap
                print L
        gap=gap/2
    return L

def selection_sort(L):
    for i in range(len(L)):
        for j in range(i+1,len(L)):
            if L[i]>L[j]:
                L[i],L[j]=L[j],L[i]
        print L
    return L

def heap_sort(L):
    def sift_down(start,end):
        Root=start
        while 1:
            child=2*Root+1
            if child>end:
                break
            if child+1<=end and L[child]<L[child+1]:
                child+=1
            if L[Root]<L[child]:
                L[Root],L[child]=L[child],L[Root]
                Root=child
            else:
                break
    for start in range((len(L)-2)/2,-1,-1):
        sift_down(start,len(L)-1)
    for end in range(len(L)-1,0,-1):
        L[0],L[end]=L[end],L[0]
        sift_down(0,end-1)
    return L

def merge(Left,Right):
    result=[]
    i,j=0,0
    while i<len(Left) and j<len(Right):
        if Left[i]<=Right[i]:
            result.append(Left[i])
            i+=1
        else:
            result.append(Right[j])
            j+=1
    while i<len(Left):
        result.append(len(Left[i]))
        i+=1
    while j<len(Right):
        result.append(Right[j])
        j+=1
    return result
def mergesort(L):
    if len(L)<2:
        return L[:]
    else:
        Middle=len(L)/2
        Left=mergesort(L[:Middle])
        Right=mergesort(L[Middle:])
        together=merge(Left,Right)
        return together
