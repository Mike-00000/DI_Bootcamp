class Circle:
    def __init__(self, radius=0, diameter=0, name=''):
        self.radius = float(radius)
        self.diameter = float(diameter)
        self.name = name

    @classmethod
    def from_radius(cls, radius, name=''):
        '''Calculate the diameter getting the radius as arg'''
        return cls(radius = radius, diameter = radius*2, name=name)
    
    @classmethod
    def from_diameter(cls, diameter, name=''):
        '''Calculate the radius getting the diameter as arg'''
        return cls(diameter = diameter, radius = diameter/2, name=name)
    
    def get_area(self) -> float:
        '''Calculate the area'''
        return 3.14 * self.radius ** 2
    
    def __add__(self, other_circle) -> float:
        '''Adds two circle areas'''
        return self.get_area() + other_circle.get_area()
    
    # def compare(self, other_circle):
    #     '''Compare two circles'''
    #     if self.get_area() > other_circle.get_area():
    #         print(f"{self} is the bigger")
    #     else:
    #         print(f"{self} is smaller")

    def compare(self, other_circle):
        '''Compare two circles'''
        if self.get_area() > other_circle.get_area():
            print(f"{self.name} is bigger than {other_circle.name}")
        elif self.get_area() < other_circle.get_area():
            print(f"{self.name} is smaller than {other_circle.name}")
        else:
            print(f"{self.name} is equal in size to {other_circle.name}")

circleA = Circle.from_diameter(diameter = 4, name='circleA')
circleB = Circle.from_radius(radius = 4, name='circleB')
circleC = Circle(3,6, name='circleC')
circleA.get_area()
print("CircleA radius : ", circleA.radius, "CircleA diameter: ", circleA.diameter)
print("CircleB radius : ", circleB.radius, "CircleB diameter: ", circleB.diameter)
print("CircleC radius : ", circleC.radius, "CircleC diameter: ", circleC.diameter)
print("circleA.get_area : ", circleA.get_area())
print("circleB.get_area : ", circleB.get_area())
print('add A and B: ', round(circleA + circleB, 2)) # adding Circles and rouding the float
circleA.compare(circleB)