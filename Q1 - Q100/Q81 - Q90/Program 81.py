"""Q. Define a class Person and its two child classes: Male and Female. All classes have a method "getgender" which can
print "Male" for Male class and "Female" for Female class"""


class Person:
    def getgender(self):
        return "Unknown"


class Male(Person):
    def getgender(self):
        return "Male"


class Female(Person):
    def getgender(self):
        return "Female"


person = Person()
male = Male()
female = Female()
print(person.getgender())
print(male.getgender())
print(female.getgender())
