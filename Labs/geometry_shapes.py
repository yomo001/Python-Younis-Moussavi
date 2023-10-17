import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle, Rectangle as pltRectangle
import math

# GeometricShapes class

class GeometricShapes:
    def __init__(self, x, y):
        self._x = x
        self._y = y 

    @property
    def x_coordinate(self):
        return self._x

    @x_coordinate.setter
    def x_coordinate(self, new_x):
        self._x = new_x

    @property
    def y_coordinate(self):
        return self._y

    @y_coordinate.setter
    def y_coordinate(self, new_y):
        self._y = new_y

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
class Circle(GeometricShapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        try:   
            self._radius = float(radius)
        except ValueError as e:
            print(f"{e}")

    @property
    def area(self):
        return math.pi * self.radius**2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius
    
    def translate(self, new_x, new_y):
        try:
            self.x_coordinate = float(new_x)
            self.y_coordinate = float(new_y)
        except ValueError:
            print(f"Error, you entered '{new_x}' and '{new_y}', both have to be numerics.")

    def __repr__(self):
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def __str__(self):
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def is_unit_circle(self):
        if self._x == 0 and self._y == 0 and self._radius == 1:
            print("This is a unit circle")
        else:
            print("This is not a unit circle")
    
    def is_inside(self, test_x, test_y):
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2)
        if distance <= self._radius:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None):
        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        circle_for_plot = pltCircle((self._x, self._y), self._radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        ax.axhline(0, linewidth=1)  
        ax.axvline(0, linewidth=1) 
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')  
        plt.show()

    
# Rectangle class
class Rectangle(GeometricShapes):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        try:   
            self._width = float(width)
            self._height = float(height)
        except ValueError as e:
            print(f"{e}")

    @property
    def area(self):
        return self._width * self._height
    
    @property
    def circumference(self):
        return 2*(self._width + self._height)

    def __repr__(self):
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"

    def __str__(self):
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"
              
    def is_square(self):
        if self._width == self._height:
            print("This is a square")
        else:
            print("This is not a square")
    
    def is_inside(self, test_x, test_y):
        distance_x = test_x-self.x
        distance_y = test_y-self.y
        if distance_x <= self._width/2 or distance_y <= self._height/2:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None):
        
        x_min = self._x - self._width/2
        y_min = self._y - self._height/2 

        fig, ax = plt.subplots()

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)

        rectangle = pltRectangle((x_min, y_min), self._width, self._height, fill = False)
        ax.add_patch(rectangle)
        ax.axhline(0, linewidth=1)  
        ax.axvline(0, linewidth=1) 
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')  
        plt.show()


# Cube class

class Cube(GeometricShapes):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        try:   
            self._side = float(side)
        except ValueError as e:
            print(f"{e}")

    @property
    def area(self):
        return 6*self._side**2
    
    @property
    def circumference(self):
        return 12*(self._side)

    def __repr__(self):
        return f"This is a Cube with the coordinates {self._x},{self._y} and area {self.area} squared units"

    def __str__(self):
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"
              
    def is_cube(self):
        if self.circumference/self._side == 12:
            print("This is a cube")
        else:
            print("This is not a cube")
    
    def is_inside(self, test_x, test_y):
        distance_x = test_x-self.x
        distance_y = test_y-self.y
        if distance_x <= self._width/2 or distance_y <= self._height/2:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None):
        x_min = self._x - self._side/2
        y_min = self._y - self._side/2 

        fig, ax = plt.subplots()

        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)

        rectangle = pltRectangle((x_min, y_min), self._side, self._side, fill = False)
        ax.add_patch(rectangle)
        ax.axhline(0, linewidth=1)  
        ax.axvline(0, linewidth=1) 
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')  
        plt.show()


# Sphere class
class Sphere(GeometricShapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        try:   
            self._radius = float(radius)
        except ValueError as e:
            print(f"{e}")

    @property
    def area(self):
        return math.pi*4*self.radius**2

    @property
    def circumference(self):
        return 2 * math.pi * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius
    
    def translate(self, new_x, new_y):
        try:
            self.x_coordinate = float(new_x)
            self.y_coordinate = float(new_y)
        except ValueError:
            print(f"Error, you entered '{new_x}' and '{new_y}', both have to be numerics.")

    def __repr__(self):
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def __str__(self):
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def is_unit_sphere(self):
        if self._x == 0 and self._y == 0 and self._radius == 1:
            print("This is a unit sphere")
        else:
            print("This is not a unit sphere")
    
    def is_inside(self, test_x, test_y):
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2)
        if distance <= self._radius:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None):
        fig, ax = plt.subplots()
        ax.set_xlim(-5, 5)
        ax.set_ylim(-5, 5)
        circle_for_plot = pltCircle((self._x, self._y), self._radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        ax.axhline(0, linewidth=1)  
        ax.axvline(0, linewidth=1) 
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')  
        plt.show()



def main():
    
    # Kontroll enligt labben
    cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
    cirkel2 = Circle(x=1,y=1, radius=1)
    rektangel = Rectangle(x=0,y=0,width=1, height=1)
    print(cirkel1==cirkel2) # True
    print(cirkel2==rektangel) # False
    print(cirkel1.is_inside(0.5, 0.5)) # True
    cirkel1.translate(5,5)
    print(cirkel1.is_inside(0.5, 0.5)) # False
    cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar

if __name__ == "__main__":
    main()


