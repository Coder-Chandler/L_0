# -*- coding: utf-8 -*-
import datetime
class Name(object):
    #nextNum = 1
    def __init__(self,name):
        self.name = name
        self.birthday = None
        #self.Num = Name.nextNum
        #Name.nextNum += 1
    #def getNum(self):
         #return self.Num
    def setbirthday(self,ID):
        assert len(str(ID)) == 18 and isinstance(ID,str),\
        'The ID number was invalid'
        year = int(ID[6:10])
        month = int(ID[10:12])
        day = int(ID[12:14])
        self.birthday = datetime.date(year,month,day)        
    def getname(self):
        return self.name
    def is_age18(self):
        if ((datetime.date.today() - self.birthday).days)/365 == 18:
            return True
        return False
    def __str__(self):
        return self.name
    __repr__ = __str__

a = Name('Lisa')
b = Name('Bart')
c = Name('John')
d = Name('Eric')
e = Name('Joey')
f = Name('Mark')
#g = Name('test...')

a.setbirthday('32012119940208372X')
b.setbirthday('323121199601233646')
c.setbirthday('411232199905154325')
d.setbirthday('322342199903233209')
e.setbirthday('412323199905092134')
f.setbirthday('123421200108263717')
#g.setbirthday(999999999999999999)
L = [a,b,c,d,e,f]
def GiveMe18(l):
    age_dict = {}
    for i in l:
        if i.is_age18():
            age_dict[i.getname()] = \
            ((datetime.date.today() - i.birthday).days)/365
    return age_dict,'We have %d people aged 18 years old'%(len(age_dict)) 
print GiveMe18(L)

