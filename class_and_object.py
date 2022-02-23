class Students:
    def __init__(self,name,age):
        self.name  = name
        self.age = age
    def greet(self):
        print("hello {}".format(self.name))

a = Students("myname",25)
b = Students("second student",26)

a.greet()
b.greet()