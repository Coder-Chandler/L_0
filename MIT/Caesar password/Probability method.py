def buildCoder(shift):
    LowerLetter_str='abcdefghijklmnopqrstuvwxyz'
    UpperLetter_str='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    Mydict={}
    for i in range(len(LowerLetter_str)):
            Mydict[LowerLetter_str[i]]=LowerLetter_str[i-shift]
            Mydict[UpperLetter_str[i]]=UpperLetter_str[i-shift]
    return Mydict

User=raw_input('word:')
def f(User):
    l=[0.0817,0.0149,0.0278,0.0425,0.1270,0.0223,0.0202,0.0609,0.0697,0.0015,0.0077,0.0402,
    0.0241,0.0675,0.0751,0.0193,0.0009,0.0599,0.0633,0.0906,0.0276,0.0098,0.0236,0.0015,0.0197,0.0007]
    Lower='abcdefghijklmnopqrstuvwxyz'
    Upper='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    ans=User.split()
    x=0
    k=0
    for s in range(26):
        c=0
        for i in ans:
            for j in i:
                if j in Lower:
                    c+=l[Lower.index(j)-s]
                elif j in Upper:
                    c+=l[Upper.index(j)-s]
        if c>x:
            x=c
            k=s
    Rtext=[i for i in User]
    for j in range(len(Rtext)):
        if Rtext[j] in buildCoder(k):
            Rtext[j]=buildCoder(k)[Rtext[j]]
    newstr=''.join(Rtext)
    return newstr

print f(User)
