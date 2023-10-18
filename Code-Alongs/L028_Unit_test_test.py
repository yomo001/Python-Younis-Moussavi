from L027_Module_test import square, greet

# Det går att testa sin kod själv, genom att koda olika scenarion. 
# Men går även att automatisera, "Unit-testing" kommer in här.
# Man testar för att se att resultat av kod är det man förväntar sig.

# Finns något i Python som heter Assert / Påstår/hävdar

# print("start")   # Denna del var bara för att påvisa de koder mellan start och end

# assert 1 > 0           # inget händer om de stämmer

#  assert 1 < 0           # Kod krashar om det inte stämmer

# Går också att fånga med try-except
# try: 
#     assert 1 > 0
# except AssertionError:
#     print("1 is not less than zero")

# Men det finns också bibliotek för testning i Python, pytest som vi ska titta närmare på. Unittest är den andra.
# IPytest - fångar upp mina asserts i koden och kan göra saker med den.
# Först installeras det: pipenv install pytest, den letar var pipfiler ligger i någon av undermapparna - och sedan installerar där
# pipfilen finns. Så därför, så länge man är i rätt ställe så hittar den. 

# print("end")  # Denna del var bara för att påvisa de koder mellan start och end



# Här är testet för att en funktion funkar som den ska, om nedan går igenom. 
# Tänk dig att du t.ex. gör sådana testfunktioner och sedan kör dom, för att 
# jämföra om resultatet blev som du ville. MEN
# Pytest gör det dock automatiskt och enklare
# Man kör den via terminalen (eller extension) och 
# Den går igenom nedan funktioner och sammanställer resultat.

def test_positive_square():
    assert square(2) == 4
    assert square(5) == 25 , "Square of 5 is not 25"

def test_negative_square():
    assert square(-2) == 4
    assert square(-5) == 25, "Square of 5 is not 25"

def test_zero_square():
    assert square(0) == 0

def test_greet_default():
     assert greet() == "Hello, World"

def test_greet_argument():
     assert greet("Fredrik") == "Hello, Fredrik"


# Mer OM HUR PYTEST FUNKAR:
# Den kollar på vilket värde MAN FÅR UT, vid en viss INPUT,
# MEd detta så ska det vara enklare kod för att se VAD man vill få ut, än HUR man ska få ut det.
# VILKA FILER OCH FUNKTIONER TESTAR DEN?
# När man skriver pytest i terminalen, så letar den upp alla filer i dess root directory 
# eller mappar under (sub directory). Filer som antingen börjar eller slutar på test letar den efter.
# I dessa filer kommer den LETA UPP ALLA FUNKTIONER SOM BÖRJAR PÅ TEST_ och antar att detta är vad den ska testa.
        # Viktigt att hålla sig till detta då - att kalla varje funktion som ska testas för test_något.
        # Rött F  betyder failed, grön punkt betyder gick igenom. För varje funktion med test fås ett F eller grön punkt.
        # Bara för att testerna går igenom betyder inte att koden funkar som den ska 
# Vid refaktoring (cleanande av kod utan att funktion påverkas), är såna tester särskilt bra. Då kan man upptäcka om en funktionalitet försvann i samband med det.
# Varje "enhet"/funktion testas för sig - FÅR INTE HA SIDE-effects om det ska gå att testa ("lös kod")







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
    
    @property                                   # Area property
    def area(self):
        return "This is meant to be overridden"

    def translate(self, new_x, new_y):         # Method for translating the shape
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
        return math.pi * self._radius**2

    @property                                   # Circumference property
    def circumference(self):
        return 2 * math.pi * self._radius

    def circumference(self):
        return 2 * math.pi * self._radius

    def __repr__(self):                         # __repr__ override
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def __str__(self):                          # __str__ override
        return f"This is a circle with the coordinates {self._x}, {self._y} and radius {self._radius} units"

    def is_unit_circle(self):                   # Method for assessing if circle is a unit circle
        if self._x == 0 and self._y == 0 and self._radius == 1: 
            return True
        else: 
            return False
    
    def is_inside(self, test_x, test_y):        # Method for assessing if a point is within the circle
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2)
        if distance <= self._radius:
            self.plot(test_x, test_y)           # Plot to visualize the point in relation to the circle 
            return True
        else: 
            self.plot(test_x, test_y)           # Plot to visualize the point in relation to the circle
            return False
        
    def plot(self, test_x = None, test_y = None):    # Method for plotting the circle
        # The figure and graphics
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

        # The plot
        circle_for_plot = pltCircle((self._x, self._y), self._radius, fill=False, color='blue')
        ax.add_patch(circle_for_plot)
        plt.show()


    
# Rectangle class - subclass of GeometricShapes
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
            self.plot(test_x, test_y)                      # Plot to visualize the point in relation to the rectangle
            return True
        else: 
            self.plot(test_x, test_y)                      # Plot to visualize the point in relation to the rectangle
            return False
        
    def plot(self, test_x = None, test_y = None):          # Method for plotting the rectangle
        # The figure and graphics
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

        # The plot
        x_min = self._x - self._side/2
        y_min = self._y - self._side/2
        rectangle = pltRectangle((x_min, y_min), self._side, self._side, fill = False)
        ax.add_patch(rectangle)
        plt.show()



# Cube class - subclass of Rectangle

class Cube(Rectangle):
    def __init__(self, x, y, z, width, height, depth):
        super().__init__(x, y, width, height)
        try:   
            self._z = z                     # Specifik for cube, added to __init__ inheritance from superclass
            self._depth = float(depth)      # Specifik for cube, added to __init__ inheritance from superclass
        except ValueError as e:
            print(f"{e}")

    @property                               # Area property
    def area(self):
        return 2*self._width**2 + 2*self._height**2 + 2*self._depth**2      # area of all sides added 
    
    @property                               # Circumference property
    def circumference(self):
        return 4* self._width               # If it is a cube, then width, height and depth are the same, so 4 x optional side

    @property                               # Property for z coordinate
    def z_coordinate(self):
        return self._z

    @z_coordinate.setter
    def z_coordinate(self, new_z):
        self._z = new_z

    def __repr__(self):                     # __repr__ overload
        return f"This is a cube with the coordinates {self._x},{self._y},{self._z} and area {self.area} squared units"

    def __str__(self):                      # __str__ overload
        return f"This is a cube with the coordinates {self._x},{self._y},{self._z} and area {self.area} squared units"
              
    def is_cube(self):                      # Method for assessing if the shape is a cube
        if self.circumference/self._side == 12:
            print("This is a cube")
        else:
            print("This is not a cube")

    def is_inside(self, test_x, test_y, test_z):        # Method for assessing if a point is within the cube
        distance_x = test_x-self._x                     # Assesing distance from x,y,z min, max 
        distance_y = test_y-self._y
        distance_z = test_z-self._z
        if distance_x <= self._side/2 and distance_y <= self._side/2 and distance_z <= self._side/2:
            self.plot(test_x, test_y)                   # Plotting the point to visualize relation to cube (obs 2D, depth not visualized)
            return True
        else: 
            self.plot(test_x, test_y)
            return False
        
    def translate(self, new_x, new_y, new_z):           # Polymorphism of translate method
        super().translate(new_x, new_y)
        try:
            self.z_coordinate = float(new_z)
        except ValueError:
            print(f"Error, you entered '{new_x}','{new_y}' and' '{new_z}', both have to be numerics.")
    
# Sphere class
class Sphere(GeometricShapes):
    def __init__(self, x, y, z, radius):
        super().__init__(x, y)
        try:   
            self._z = float(z)                      # Specifik for sphere, added to __init__ inheritance from superclass
            self._radius = float(radius)            # Specifik for sphere, added to __init__ inheritance from superclass
        except ValueError as e:
            print(f"{e}")

    @property                                       # Area property
    def area(self):
        return math.pi*4*self.radius**2

    @property                                       # Circumference property
    def circumference(self):
        return 2 * math.pi * self.radius

    def circumference(self):
        return 2 * math.pi * self.radius
    
    @property                                       # Property for z coordinate
    def z_coordinate(self):
        return self._z

    @z_coordinate.setter
    def z_coordinate(self, new_z):
        self._z = new_z

    def __repr__(self):                             # __repr__ overload
        return f"This is a sphere with the coordinates {self._x}, {self._y},{self._z} and radius {self._radius} units"

    def __str__(self):                              # __str__ overload
        return f"This is a sphere with the coordinates {self._x}, {self._y},{self._z} and radius {self._radius} units"

    def is_unit_sphere(self):                       # Method for checking if sphere is a unit sphere
        if self._x == 0 and self._y == 0 and self._z == 0 and self._radius == 1:
            print("This is a unit sphere")
        else:
            print("This is not a unit sphere")

    def is_inside(self, test_x, test_y, test_z):    # Method for checking if point is within sphere
        distance = math.sqrt((test_x-self._x)**2+(test_y-self._y)**2+(test_z-self._z)**2)   # https://stackoverflow.com/questions/26818772/python-checking-if-a-point-is-in-sphere-with-center-x-y-z
        if distance <= self._radius:
            self.plot(test_x, test_y)               # Plot to visualize point in relation to square (obs, 2D, depth not visualized)
            return True
        else: 
            self.plot(test_x, test_y)               # Plot to visualize point in relation to square (obs, 2D, depth not visualized)
            return False
        
    def translate(self, new_x, new_y, new_z):       # Polymorphism of translate method
        super().translate(new_x, new_y)
        try:
            self.z_coordinate = float(new_z)
        except ValueError:
            print(f"Error, you entered '{new_x}','{new_y}' and' '{new_z}', both have to be numerics.")

    # Method for plotting "sphere" (actually circle since in 2D, depth not visualized)
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
    
    # Controls from labb3 assignment instructions. All passed.
    cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
    cirkel2 = Circle(x=1,y=1, radius=1)
    rektangel = Rectangle(x=0,y=0,width=1, height=1)
    print(cirkel1==cirkel2) # True
    print(cirkel2==rektangel) # False
    print(cirkel1.is_inside(0.5, 0.5)) # True
    cirkel1.translate(5,5)
    print(cirkel1.is_inside(0.5, 0.5)) # False
    cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar

if __name__ == "__main__":               # To avoid "loose code" from running when importing module
    main()


