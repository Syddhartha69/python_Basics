class Employee:
    def __init__(self,name,salary,tax):
        self.name = name
        self.salary = salary
        self.tax = tax
    def netsalary(self):
        net_salary = self.salary - (self.salary * self.tax)/100 
        print("your net salary is {}".format(net_salary))
    
a = Employee("ram",20000,10)
b = Employee("hari",10000,20)

a.netsalary()
b.netsalary()