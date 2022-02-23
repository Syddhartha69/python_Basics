class circle:
    def __init__(self,radius,):
        self.radius = radius
    def area(self):
        circle_area = (3.1415) * self.radius ** 2 
        print("the area is {}".format(circle_area))
a = circle(5)
b = circle(2)

a.area()
b.area()