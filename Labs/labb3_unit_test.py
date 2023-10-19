from geometry_shapes import Circle, Rectangle, Cube, Sphere
import math
#matplotlib.use('Agg')  # https://stackoverflow.com/questions/4930524/how-can-i-set-the-matplotlib-backend    
#Because of problem assessing functions where the plots are plotted, i want to assess the boolean not the plot 
# so this does not affect the functionality of the test




# Test of Circle class
my_circle1 = Circle(x=0,y=0, radius=1)              #  GÖR DETTA I VARJE ENSKILD FUNKTION ISTÄLLET. 
my_circle2 = Circle(x=1,y=1, radius=1)

def test_circle_area():
    assert  my_circle1.area == math.pi                    

def test_circle_is_unit():
    assert my_circle1.is_unit_circle() == True         # TRUE OCH FALSE  (INTE I SAMMA FÖR DEF IS_NOT_UNIT)         

def test_circle_is_inside():                           # IS INSIDE OCH NOT INSIDE   , MED POSITIVT OCH NEGATIVT-  FYRA VARIANTER
    assert my_circle1.is_inside(0.5,0.5) == True   

def test_equality_override():                           # HA DETTA MED.  BRA ATT HA HÄR VID REFACTORING,    
    assert my_circle1.__eq__(my_circle2) == True        # assessing my_circle1 == my_circle2
       
def test_translate_circle():    
    assert my_circle1.translate("TRE",5) == f"Error, you entered 'TRE' and '5', both have to be numerics."

# Test of Rectangle class
my_rectangle1 = Rectangle(x=0,y=0,width=1, height=1)
my_rectangle2 = Rectangle(x=1,y=1,width=1, height=2)

def test_rectangle_area():
    assert  my_rectangle1.area == 1                  

def test_rectangle_is_inside():
    assert my_rectangle1.is_inside(0.5, 0.5) == True     

def test_equality_override2():
    assert my_circle2.__eq__(my_rectangle2) == False         # assessing my_circle2 == my_rectangle2

def test_translate_rectangle():
    assert my_rectangle1.translate(3,"FEM") == f"Error, you entered '3' and 'FEM', both have to be numerics."

# Test of Cube class
my_cube1 = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
my_cube2 = Cube(x=1,y=1, z=1, width=2, height=3, depth=2)

def test_cube_area():
    assert  my_cube1.area == 6                  

def test_cube_is_inside():
    assert my_cube1.is_inside(0.5,0.5,0.5) == True   

def test_translate_cube():
    assert my_cube1.translate(0.5,0.5,"d") == f"Error, you entered '0.5','0.5' and' 'd', all have to be numerics."

# Test of Sphere class
my_sphere1 = Sphere(x=0,y=0, z=0, radius=1)
my_sphere2 = Sphere(x=1,y=1, z=1, radius=1)

def test_sphere_area():
    assert  my_sphere1.area == math.pi*4               

def test_sphere_is_inside():
    assert my_sphere1.is_inside(0.5,0.5,0.5) == True  

def test_translate_sphere():
    assert my_sphere1.translate("younis",0.5,0.5) == f"Error, you entered 'younis','0.5' and' '0.5', all have to be numerics."
