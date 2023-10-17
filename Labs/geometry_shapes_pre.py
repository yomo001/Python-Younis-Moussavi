import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle, Rectangle as pltRectangle
import math

# Geometric shapes class

class GeometricShapes:
    def __init__(self, x, y):
        self.x = x
        self.y = y 

    @property
    def x_coordinate(self):
        return self.x

    @x_coordinate.setter
    def x_coordinate(self, new_x):
        self.x = new_x

    @property
    def y_coordinate(self):
        return self.y

    @y_coordinate.setter
    def y_coordinate(self, new_y):
        self.y = new_y

    def translate(self, new_x, new_y):
            try:
                self.x_coordinate = float(new_x)
                self.y_coordinate = float(new_y)
            except ValueError:
                print(f"Error, you entered '{new_x}' and '{new_y}', both have to be numerics.")
            
    def __eq__(self, other):
        return type(self) is type(other)

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area



# Circle class
class Circle:
    def __init__(self, x, y, radius):
        try:   
            self.x = float(x)
            self.y = float(y)
        except ValueError as e:
            print(f"{e}")

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    @property
    def x_coordinate(self):
        return self.x

    @x_coordinate.setter
    def x_coordinate(self, new_x):
        self.x = new_x

    @property
    def y_coordinate(self):
        return self.y

    @y_coordinate.setter
    def y_coordinate(self, new_y):
        self.y = new_y

    def circumference(self):
        return 2 * math.pi * self.radius
    
    def translate(self, new_x, new_y):
        try:
            self.x_coordinate = float(new_x)
            self.y_coordinate = float(new_y)
        except ValueError:
            print(f"Error, you entered '{new_x}' and '{new_y}', both have to be numerics.")
        
    def __eq__(self, other):
        return type(self) is type(other)

    def __lt__(self, other):
        return self.area < other.area

    def __le__(self, other):
        return self.area <= other.area

    def __gt__(self, other):
        return self.area > other.area

    def __ge__(self, other):
        return self.area >= other.area

    def __repr__(self):
        return f"This is a circle with the coordinates {self.x}, {self.y} and radius {self.radius} units"

    def __str__(self):
        return f"This is a circle with the coordinates {self.x}, {self.y} and radius {self.radius} units"

    def isunitcircle(self):
        if self.x == 0 and self.y == 0 and self.radius == 1:
            print("This is a unit circle")
        else:
            print("This is not a unit circle")
    
    def isinside(self, test_x, test_y):
        distance = math.sqrt((test_x-self.x)**2+(test_y-self.y)**2)
        if distance <= self.radius:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None):
        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        circle_for_plot = pltCircle((self.x, self.y), self.radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        ax.axhline(0, linewidth=1)  
        ax.axvline(0, linewidth=1) 
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')  
        plt.show()

    

# Rectangle class
class Rectangle():
    def __init__(self, x, y, width, height):
        try:   
            self.x = float(x)
            self.y = float(y)
            self.width = float(width)
            self.height = float(height)
        except ValueError as e:
            print(f"{e}")

    @property
    def area(self):
        return self.width * self.height
    
    @property
    def circumference(self):
        return 2*(self.width + self.height)

    @property
    def x_coordinate(self):
        return self.x

    @x_coordinate.setter
    def x_coordinate(self, new_x):
        self.x = new_x

    @property
    def y_coordinate(self):
        return self.y

    @y_coordinate.setter
    def y_coordinate(self, new_y):
        self.y = new_y
    
    def translate(self, new_x, new_y):
        try:
            self.x_coordinate = float(new_x)
            self.y_coordinate = float(new_y)
        except ValueError:
            print(f"Error, you entered '{new_x}' and '{new_y}', both have to be numerics.")
    
    def __eq__(self, other):
        return type(self) is type(other)

    def __lt__(self, other):
        return self.area < other.area
    
    def __le__(self, other): 
        return self.area <= other.area

    def __gt__(self, other):
        return self.area > other.area
    
    def __ge__(self, other): 
        return self.area >= other.area

    def __repr__(self):
        return f"This is a rectangle with the coordinates {self.x},{self.y} and area {self.area} squared units"

    def __str__(self):
        return f"This is a rectangle with the coordinates {self.x},{self.y} and area {self.area} squared units"
              
    def issquare(self):
        if self.width == self.height:
            print("This is a square")
        else:
            print("This is not a square")
    
    def isinside(self, test_x, test_y):
        distance_x = test_x-self.x
        distance_y = test_y-self.y
        if distance_x <= self.width/2 or distance_y <= self.height/2:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None):
        
        x_min = self.x - self.width/2
        y_min = self.y - self.height/2 

        fig, ax = plt.subplots()

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)

        rectangle = pltRectangle((x_min, y_min), self.width, self.height, fill = False)
        ax.add_patch(rectangle)
        ax.axhline(0, linewidth=1)  
        ax.axvline(0, linewidth=1) 
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')  
        plt.show()
    

def main():
    my_circle = Circle(0,0,1)
    my_circle.isinside(1,1)

if __name__ == "__main__":
    main()