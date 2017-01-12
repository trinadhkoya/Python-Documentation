class Person(object):

    def __init__(self,fname,lname):
        self.first_name=fname
        self.last_name=lname
    def __str__(self):
        return self.first_name+self.last_name


class Employee(Person):

        def __init__(self,fname,lname,ssid):
            super().__init__(fname,lname)
            self.social_id=ssid

        def __str__(self):
                return self.first_name + self.last_name+self.social_id


        # def getEmployeeName(self):
        #     return self.first_name+self.last_name

x=Person("TRINADH","KOYA")
y=Employee("TRINADH","KOYA","10491a1249")
print(x)
print(y)

