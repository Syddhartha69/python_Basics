class rectangle:
    def __init__(self,length,breadth):
        self.length = length
        self.breadth = breadth
    def area(self):
        rect_area = self.length * self.breadth
        print("the area is {}".format(rect_area))
a = rectangle(10,5)
b = rectangle(2,2)

a.area()
b.area()