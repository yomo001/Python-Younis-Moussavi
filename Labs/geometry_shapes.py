import matplotlib.pyplot as plt
from matplotlib.patches import Circle as pltCircle, Rectangle as pltRectangle
import math

# In this module you will find
    # 1. Class Shapes2D
        # 2. Class Circle (Inheriting from Shapes2D)
        # 3. Class Rectangle (Inheriting from Shapes2D)
    # 4. Class Shapes3D
        # 5. Class Cube (Inheriting from Shapes3D)
        # 6. Class Sphere (Inheriting from Shapes3D)


# 1. Class Shapes2D

class Shapes2D:          
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    @property                                   # Area property
    def area(self):
        return "This is meant to be overridden"

    def translate(self, move_x, move_y):         # Method for translating the shape
            try:
                self.x = self.x + float(move_x)
                self.y = self.y + float(move_y)
            except ValueError:
                error_alert = f"Error, you entered '{move_x}' and '{move_y}', both have to be numerics."
                print(error_alert)            # Because assessment question in labb3 required printing it out when entering it.
                return error_alert
          
    def __eq__(self, other):                   # Operator overload of ==
        return self.area == other.area        
 
    def __lt__(self, other):                   # Operator overload of <
        return self.area < other.area

    def __le__(self, other):                   # Operator overload of <=
        return self.area <= other.area

    def __gt__(self, other):                   # Operator overload of >
        return self.area > other.area

    def __ge__(self, other):                   # Operator overload of >=
        return self.area >= other.area

# 2. Class Circle (Inheriting from Shapes2D)

class Circle(Shapes2D):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self.radius = radius                    # Specifik for circle, added to __init__ inheritance from superclass

    @property                                   # Area property
    def area(self):
        return math.pi * self.radius**2

    @property                                   # Circumference property
    def circumference(self):
        return 2 * math.pi * self.radius

    def __repr__(self):                         # __repr__ override                                       
        return f"Circle({self.x}, {self.y}, {self.radius})"

    def __str__(self):                          # __str__ override
        return f"This is a circle with the coordinates {self.x}, {self.y} and radius {self.radius} units"

    def is_unit_circle(self):                   # Method for assessing if circle is a unit circle
        return self.x == 0 and self.y== 0 and self.radius == 1

    def is_inside(self, x, y):                  # Method for assessing if a point is within the circle
        distance = math.sqrt((x-self.x)**2+(y-self.y)**2)
        return distance <= self.radius

    def plot(self, x = None, y = None):         # x and y if we want to compare coordinates in relation to shape
        # The figure and graphics
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)

        # The plot
        ax.scatter(x, y, color='green', marker='o')
        circle_for_plot = plt.Circle((self.x, self.y), self.radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        plt.show()

    
# 3. Class Rectangle (Inheriting from Shapes2D)

class Rectangle(Shapes2D):
    def __init__(self, x, y, width, height):
        super().__init__(x, y) 
        self.width = width                                  # Specifik for rectangle, added to __init__ inheritance from superclass
        self.height = height                                # Specifik for rectangle, added to __init__ inheritance from superclass

    @property                                               # Area property
    def area(self):
        return self.width * self.height
    
    @property                                               # Circumference property
    def circumference(self):
        return 2*(self.width + self.height)

    def __repr__(self):                                     # __repr__ override
        return f"Rectangle({self.x}, {self.y}, {self.width}, {self.height})"

    def __str__(self):                                      # __str__ override
        return f"This is a rectangle with the coordinates {self.x},{self.y} and area {self.area} squared units"
              
    def is_square(self):                                    # Method to check if shape is a square
        return self.width == self.height
    
    def is_inside(self, x, y):                              # Method for assessing if a point is within the rectangle
        distance_x = abs(x-self.x)
        distancey = abs(y-self.y)
        return distance_x <= self.width/2 and distancey <= self.height/2      # Distance from x/y min, max for assessment
        
    def plot(self, x = None, y = None):         # x and y if we want to compare coordinates in relation to shape
        # The figure and graphics
        fig, ax = plt.subplots()
        ax.set_xticks(range(-5, 6)) 
        ax.set_yticks(range(-5, 6)) 
        ax.set_xlabel('X-axis')
        ax.set_ylabel('Y-axis')
        ax.axhline(0, linewidth=1)
        ax.axvline(0, linewidth=1) 
        ax.grid(True)

        # The plot
        ax.scatter(x, y, color='green', marker='o')
        x_min = self.x - self.width/2
        y_min = self.y- self.height/2
        rectangle = pltRectangle((x_min, y_min), self.width, self.height, fill = False)
        ax.add_patch(rectangle)
        plt.show()



# 4. Class Shapes3D

class Shapes3D:          
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    
    @property                                   # Area property
    def area(self):
        return "This is meant to be overridden"

    def translate(self, move_x, move_y, movez):         # Method for translating the shape
            try:
                self.x = self.x + float(move_x)
                self.y = self.y + float(move_y)
                self.z = self.z + float(movez)
            except ValueError:
                error_alert = f"Error: you entered '{move_x}', '{move_y}' and '{movez}', all have to be numerics."
                print(error_alert)            # Because assessment question in labb3 required printing it out when entering it.
                return error_alert
          
    def __eq__(self, other):                   # Operator overload of ==
        return self.area == other.area        
 
    def __lt__(self, other):                   # Operator overload of <
        return self.area < other.area

    def __le__(self, other):                   # Operator overload of <=
        return self.area <= other.area

    def __gt__(self, other):                   # Operator overload of >
        return self.area > other.area

    def __ge__(self, other):                   # Operator overload of >=
        return self.area >= other.area



# 5. Class Cube (Inheriting from Shapes3D) 

class Cube(Shapes3D):
    def __init__(self, x, y, z, width, height, depth):
        super().__init__(x, y, z)   
        self.width = width                     # Specifik for cube, added to __init__ inheritance from superclass
        self.height = height                   # Specifik for cube, added to __init__ inheritance from superclass
        self.depth = depth                     # Specifik for cube, added to __init__ inheritance from superclass


    @property                                  # Area property
    def area(self):
        return 2*self.width*self.height + 2*self.depth*self.height+2*self.depth*self.width   # area of all sides added 
    
    @property                                  # Volume property
    def volume(self):
        return self.width*self.height*self.depth                  

    def __repr__(self):                     # __repr__ overload
        return f"Cube({self.x}, {self.y}, {self.z}, {self.width}, {self.height}, {self.depth})"

    def __str__(self):                      # __str__ overload
        return f"This is a cube with the coordinates {self.x},{self.y},{self.z} and area {self.area} squared units"
              
    def is_cube(self):                      # Method for assessing if the shape is a cube
        return self.width == self.height == self.depth

    def is_inside(self, x, y, z):                   # Method for assessing if a point is within the cube.                                
        distance_x = abs(x-self.x)                  # Assessing distance from x,y,z min, max 
        distancey = abs(y-self.y)
        distancez = abs(z-self.z)
        return distance_x <= self.width/2 and distancey <= self.height/2 and distancez <= self.depth/2



# 6. Class Sphere (Inheriting from Shapes3D)

class Sphere(Shapes3D):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y, z)
        self.radius = radius                        # Specific for sphere, added to __init__ inheritance from superclass

    @property                                       # Area property
    def area(self):
        return 4*math.pi*self.radius**2

    @property                                       # Volume property
    def volume(self):
        return (4/3) * math.pi * self.radius**3
    
    def __repr__(self):                             # __repr__ overload
        return f"Sphere({self.x}, {self.y}, {self.z}, {self.radius})"

    def __str__(self):                              # __str__ overload
        return f"This is a sphere with the coordinates {self.x}, {self.y},{self.z} and radius {self.radius} units"

    def is_unit_sphere(self):                       # Method for checking if sphere is a unit sphere
        return self.x == 0 and self.y== 0 and self.z == 0 and self.radius == 1

    def is_inside(self, x, y, z):       # Method for checking if point is within sphere
        distance = math.sqrt((x-self.x)**2+(y-self.y)**2+(z-self.z)**2)    # excercise 0 and https://stackoverflow.com/questions/26818772/python-checking-if-a-point-is-in-sphere-with-center-x-y-z
        return distance <= self.radius              
