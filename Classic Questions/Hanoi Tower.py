'''
Towers	of	Hanoi
The	story:
3	tall	spikes
Stack	of	64	different	sized	discs	start	on	one
spike
Need	to	move	stack	to	second	spike	(at	which
point	universe	ends)
Can	only	move	one	disc	at	a	Dme,	and	a	larger	disc
can	never	cover	up	a	small	disc


Towers	of	Hanoi
Having	seen	a	set	of	examples	of	different
sized	stacks,	how	would	you	write	a	program
to	print	out	the	right	set	of	moves?
Think	recursively!
 Solve	a	smaller	problem
 Solve	a	basic	problem
 Solve	a	smaller	problem
 '''

def Towers(n,fr,to,spare):
    def PrintMove(fr,to):
        print 'Move form',str(fr),'to',str(to)
    if n == 1:
        PrintMove(fr,to)
    else:
        Towers(n-1,fr,spare,to)
        Towers(1,fr,to,spare)
        Towers(n-1,spare,to,fr)
Towers(10,'fr','spare','to')