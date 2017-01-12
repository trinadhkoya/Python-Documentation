# Person is a Super/Base class
class Person(object):
    def __init__(self, fname, lname):
        self.first_name = fname
        self.last_name = lname

    def __str__(self):
        return self.first_name + " " + self.last_name


# Employee is Sub class
class Employee(Person):
    def __init__(self, fname, lname, ssid):
        super().__init__(fname, lname)
        self.social_id = ssid

    def __str__(self):
        return self.first_name + " " + self.last_name + " " + self.social_id


x = Person("TRINADH", "KOYA")
'''
Here we are creating object for person,Once it was done,it checks for init method and stores the passed data in to varibales.
in the above examples ,i have taken self.first_name ,self.last_name.

Self is default paramter for any method in Python.See the docs why it is..!!

'''

y = Employee("TRINADH", "KOYA", "10491a1249")
'''
in this we are creating object for Employee.Which already inherited few properties from Base class(Person) like firstname and last name
.In this we are passing first name,last name and additional param is SSID.So we have 2 common properties and already derived from Base class.So we dont need .
In order to fetch ,just override the init method in super class

Two ways to call
1.Person.__init__(self,first, last)
2.super().__init__(first, last)


'''

print(x)
print(y)
