class ParentClass(object):

    def __init__(self,name,age,gender):
        self.yourfullname=name
        self.yourage=age
        self.yourgender=gender
    def __str__(self):
        return self.yourfullname

class ChildClass(ParentClass):
    def __init__(self,name,age,gender,mobienumber):
        super().__init__(name,age,gender)
        self.contact=mobienumber
    def getFullContactData(self):
        return self.yourfullname+" "+str(self.yourage)+" "+self.yourgender+" "+self.contact


parentClassObj=ParentClass("TRINADH",23,"MALE")
childClasssObje=ChildClass("TRINADH",23,"MALE","9346574125")
print(childClasssObje.getFullContactData())



'''
NOTE:
method overloading:same method(_init_()) ,with different type signature

'''

