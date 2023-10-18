import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle, Rectangle as pltRectangle
import math

# GeometricShapes class - superclass

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
            
    def __eq__(self, other):                   # Operator overload of ==
        return type(self) is type(other)

    def __lt__(self, other):                   # Operator overload of <
        return self.area < other.area

    def __le__(self, other):                   # Operator overload of <=
        return self.area <= other.area

    def __gt__(self, other):                   # Operator overload of >
        return self.area > other.area

    def __ge__(self, other):                   # Operator overload of >=
        return self.area >= other.area


# Circle class - subclass of GeometricShapes

class Circle(GeometricShapes):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        try:   
            self._radius = float(radius)        # Specifik for circle, added to __init__ inheritance from superclass
        except ValueError as e:
            print(f"{e}")

    @property                                   # Area property
    def area(self):
        return math.pi * self.radius**2

    @property                                   # Circumference property
    def circumference(self):
        return 2 * math.pi * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):                         # __repr__ override
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def __str__(self):                          # __str__ override
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def is_unit_circle(self):                   # Method for assessing if circle is a unit circle
        if self._x == 0 and self._y == 0 and self._radius == 1:
            print("This is a unit circle")
        else:
            print("This is not a unit circle")
    
    def is_inside(self, test_x, test_y):        # Method for assessing if a point is within the circle
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2)
        if distance <= self._radius:
            self.plot(test_x, test_y)           # Plot to visualize the point in relation to the circle 
            return True
        else: 
            self.plot(test_x, test_y)           # Plot to visualize the point in relation to the circle
            return False
        
    def plot(self, test_x = None, test_y = None):    # Method for plotting the circle
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')

        #Själva plotten
        circle_for_plot = pltCircle((self._x, self._y), self._radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        plt.show()


    
# Rectangle class
class Rectangle(GeometricShapes):
    def __init__(self, x, y, width, height):
        super().__init__(x, y)
        try:   
            self._width = float(width)                      # Specifik for rectangle, added to __init__ inheritance from superclass
            self._height = float(height)                    # Specifik for rectangle, added to __init__ inheritance from superclass
        except ValueError as e:
            print(f"{e}")

    @property                                               # Area property
    def area(self):
        return self._width * self._height
    
    @property                                               # Circumference property
    def circumference(self):
        return 2*(self._width + self._height)

    def __repr__(self):                                     # __repr__ override
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"

    def __str__(self):                                      # __str__ override
        return f"This is a rectangle with the coordinates {self._x},{self._y} and area {self.area} squared units"
              
    def is_square(self):                                    # Method to check if shape is a square
        if self._width == self._height:
            print("This is a square")
        else:
            print("This is not a square")
    
    def is_inside(self, test_x, test_y):                    # Method for assessing if a point is within the rectangle
        distance_x = test_x-self._x
        distance_y = test_y-self._y
        if distance_x <= self._width/2 and distance_y <= self._height/2:      # Distance from x/y min, max for assessment
            self.plot(test_x, test_y)                      # Plot to visualize the point in relation to the circle
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def plot(self, test_x = None, test_y = None): 
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')

        # Själva plotten
        x_min = self._x - self._side/2
        y_min = self._y - self._side/2
        rectangle = pltRectangle((x_min, y_min), self._side, self._side, fill = False)
        ax.add_patch(rectangle)
        plt.show()



# Cube class

class Cube(GeometricShapes):
    def __init__(self, x, y, z, side):
        super().__init__(x, y)
        try:   
            self._z = z
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
        return f"This is a cube with the coordinates {self._x},{self._y},{self._z} and area {self.area} squared units"

    def __str__(self):
        return f"This is a cube with the coordinates {self._x},{self._y},{self._z} and area {self.area} squared units"
              
    def is_cube(self):
        if self.circumference/self._side == 12:
            print("This is a cube")
        else:
            print("This is not a cube")

    def is_inside(self, test_x, test_y, test_z):
        distance_x = test_x-self._x
        distance_y = test_y-self._y
        distance_z = test_z-self._z
        if distance_x <= self._side/2 and distance_y <= self._side/2 and distance_z <= self._side/2:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def translate(self, new_x, new_y, new_z):
        super().translate(new_x, new_y)
        try:
            self.z_coordinate = float(new_z)
        except ValueError:
            print(f"Error, you entered '{new_x}','{new_y}' and' '{new_z}', both have to be numerics.")
    
    # Samma som för rektangel, plottar i 2D, blir samma bild, missar dock djupet men ser iaf. på 2D planet 
    def plot(self, test_x = None, test_y = None):
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')

        # Själva plotten
        x_min = self._x - self._side/2
        y_min = self._y - self._side/2
        rectangle = pltRectangle((x_min, y_min), self._side, self._side, fill = False)
        ax.add_patch(rectangle)
        plt.show()


# Sphere class
class Sphere(GeometricShapes):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y)
        try:   
            self._z = float(z)
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
    
    @property
    def z_coordinate(self):
        return self._z

    @z_coordinate.setter
    def z_coordinate(self, new_z):
        self._z = new_z

    def __repr__(self):
        return f"This is a sphere with the coordinates {self._x}, {self._y},{self._z} and radius {self._radius} units"

    def __str__(self):
        return f"This is a sphere with the coordinates {self._x}, {self._y},{self._z} and radius {self._radius} units"

    def is_unit_sphere(self):
        if self._x == 0 and self._y == 0 and self._z == 0 and self._radius == 1:
            print("This is a unit sphere")
        else:
            print("This is not a unit sphere")

    def is_inside(self, test_x, test_y, test_z):
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2+(test_z-self._z)**2)   # https://stackoverflow.com/questions/26818772/python-checking-if-a-point-is-in-sphere-with-center-x-y-z
        if distance <= self._radius:
            self.plot(test_x, test_y)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def translate(self, new_x, new_y, new_z):
        super().translate(new_x, new_y)
        try:
            self.z_coordinate = float(new_z)
        except ValueError:
            print(f"Error, you entered '{new_x}','{new_y}' and' '{new_z}', both have to be numerics.")

        # Samma som för cirkel, plottar i 2D, blir samma bild, missar dock djupet men ser iaf. på 2D planet
    def plot(self, test_x = None, test_y = None):
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)
        if test_x is not None and test_y is not None:
            plt.plot(test_x, test_y, 'ro')

        #Själva plotten
        circle_for_plot = pltCircle((self._x, self._y), self._radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
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


