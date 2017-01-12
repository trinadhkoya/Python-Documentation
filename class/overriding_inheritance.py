class ParentClass(object):
    def __init__(self, name, age, gender):
        self.yourfullname = name
        self.yourage = age
        self.yourgender = gender

    def getFullContactData(self):
        return self.yourfullname


class ChildClass(ParentClass):
    def __init__(self, name, age, gender, mobienumber):
        super().__init__(name, age, gender)
        self.contact = mobienumber

    def getFullContactData(self):
        return self.yourfullname


parentClassObj = ParentClass("TRINADH", 23, "MALE")
childClasssObje = ChildClass("TRINADH", 23, "MALE", "9346574125")
print(childClasssObje.getFullContactData())
print(parentClassObj.getFullContactData())

'''
NOTE:
method overriding:same method(getFullContactData()) ,with same type signature

'''
