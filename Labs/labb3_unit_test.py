from geometry_shapes import Circle, Rectangle, Cube, Sphere
import math


# Test of Circle class

def test_circle__repr__():
    my_circle = Circle(0, 0, 1)
    assert  my_circle.__repr__()== 'Circle(0, 0, 1)'

def test_circle_area():
    my_circle = Circle(x=0,y=0, radius=1)
    assert  my_circle.area == math.pi    

def test_circle_circumference():
    my_circle = Circle(x=0,y=0, radius=1)
    assert  my_circle.circumference == 2*math.pi * my_circle.radius             

def test_circle_is_unit():
    my_circle = Circle(x=0,y=0, radius=1)
    assert my_circle.is_unit_circle() == True                 

def test_circle_is_not_unit():
    my_circle = Circle(x=0,y=0, radius=2)
    assert my_circle.is_unit_circle() == False       

def test_circle_is_inside_pos():                         
    my_circle = Circle(x=0,y=0, radius=1)
    assert my_circle.is_inside(0.5,0.5) == True

def test_circle_is_not_inside_pos():                         
    my_circle = Circle(x=0,y=0, radius=1)
    assert my_circle.is_inside(4,4) == False

def test_circle_is_inside_neg():                         
    my_circle = Circle(x=0,y=0, radius=1)
    assert my_circle.is_inside(-0.5, -0.5) == True

def test_circle_is_not_inside_neg():                         
    my_circle = Circle(x=0,y=0, radius=1)
    assert my_circle.is_inside(-4,-4) == False

def test_circle_equality():                            
    my_circle1 = Circle(x=0,y=0, radius=1)
    my_circle2 = Circle(x=0,y=0, radius=1)
    my_rectangle = Rectangle(x=0,y=0,width=2, height=2)
    assert my_circle1.__eq__(my_circle2) == True
    assert my_circle1.__eq__(my_rectangle) == False

def test_circle_less_than():                            
    my_circle1 = Circle(x=0,y=0, radius=1)
    my_circle2 = Circle(x=0,y=0, radius=1)
    my_rectangle = Rectangle(x=0,y=0,width=2, height=2)
    assert my_circle1.__lt__(my_circle2) == False
    assert my_circle1.__lt__(my_rectangle) == True

def test_circle_greater_than():                            
    my_circle1 = Circle(x=0,y=0, radius=1)
    my_circle2 = Circle(x=0,y=0, radius=1)
    my_rectangle = Rectangle(x=0,y=0,width=2, height=2)
    assert my_circle1.__gt__(my_circle2) == False
    assert my_circle1.__gt__(my_rectangle) == False

def test_translate_circle():    
    my_circle = Circle(x=0,y=0, radius=1)
    assert my_circle.translate("TRE",5) == f"Error, you entered 'TRE' and '5', both have to be numerics."



# Test of Rectangle class

def test_rectangle__repr__():
    my_rectangle = Rectangle(0, 0, 1, 1)
    assert  my_rectangle.__repr__()== 'Rectangle(0, 0, 1, 1)'

def test_rectangle_area():
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert  my_rectangle.area == my_rectangle.width * my_rectangle.height   

def test_rectangle_circumference():
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert  my_rectangle.circumference == 2*my_rectangle.width + 2*my_rectangle.height             

def test_rectangle_is_square():
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle.is_square() == True               

def test_rectangle_is_not_square():
    my_rectangle = Rectangle(x=0,y=0,width=1, height=2)
    assert my_rectangle.is_square() == False      

def test_rectangle_is_inside_pos():                         
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle.is_inside(0.3,0.3) == True

def test_rectangle_is_not_inside_pos():                         
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle.is_inside(1,1) == False

def test_rectangle_is_inside_neg():                         
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle.is_inside(-0.3,-0.3) == True

def test_rectangle_is_not_inside_neg():                         
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle.is_inside(-1,-1) == False

def test_rectangle_equality():                            
    my_rectangle1 = Rectangle(x=0,y=0,width=1, height=1)
    my_rectangle2 = Rectangle(x=0,y=0,width=1, height=1)
    my_rectangle3 = Rectangle(x=0,y=0,width=2, height=1)
    assert my_rectangle1.__eq__(my_rectangle2) == True
    assert my_rectangle3.__eq__(my_rectangle2) == False

def test_rectangle_less_than():                            
    my_rectangle1 = Rectangle(x=0,y=0,width=2, height=2)
    my_rectangle2 = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle1.__lt__(my_rectangle2) == False
    assert my_rectangle2.__lt__(my_rectangle1) == True

def test_rectangle_greater_than():                            
    my_rectangle1 = Rectangle(x=0,y=0,width=2, height=2)
    my_rectangle2 = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle1.__gt__(my_rectangle2) == True
    assert my_rectangle2.__gt__(my_rectangle1) == False

def test_translate_rectangle():    
    my_rectangle = Rectangle(x=0,y=0,width=1, height=1)
    assert my_rectangle.translate(3,"FEM") == f"Error, you entered '3' and 'FEM', both have to be numerics."



# Test of Cube class

def test_cube__repr__():
    my_cube = Cube(0, 0, 0, 1, 1, 1)
    assert  my_cube.__repr__()== 'Cube(0, 0, 0, 1, 1, 1)'

def test_cube_area():
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert  my_cube.area ==  2*my_cube.width*my_cube.height + 2*my_cube.depth*my_cube.height+2*my_cube.depth*my_cube.width

def test_cube_volume():
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert  my_cube.volume == my_cube.width * my_cube.height * my_cube.depth         

def test_cube_is_cube():
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube.is_cube() == True          

def test_cube_is_not_cube():
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=2)
    assert my_cube.is_cube() == False      

def test_cube_is_inside_pos():                         
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube.is_inside(0.3,0.3,0.3) == True

def test_cube_is_not_inside_pos():                         
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube.is_inside(4,4,4) == False

def test_cube_is_inside_neg():                         
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube.is_inside(-0.3,-0.3,-0.3) == True

def test_cube_is_not_inside_neg():                         
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube.is_inside(-4,-4,-4) == False

def test_cube_equality():                            
    my_cube1 = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    my_cube2 = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    my_cube3 = Cube(x=0,y=0, z=0, width=3, height=1, depth=1)
    assert my_cube1.__eq__(my_cube2) == True
    assert my_cube3.__eq__(my_cube2) == False

def test_cube_less_than():                            
    my_cube1 = Cube(x=0,y=0, z=0, width=1, height=2, depth=2)
    my_cube2 = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube1.__lt__(my_cube2) == False
    assert my_cube2.__lt__(my_cube1) == True

def test_cube_greater_than():                            
    my_cube1 = Cube(x=0,y=0, z=0, width=1, height=2, depth=2)
    my_cube2 = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube1.__gt__(my_cube2) == True
    assert my_cube2.__gt__(my_cube1) == False

def test_translate_cube():    
    my_cube = Cube(x=0,y=0, z=0, width=1, height=1, depth=1)
    assert my_cube.translate(3,"FEM",3) == f"Error: you entered '3', 'FEM' and '3', all have to be numerics."


# Test of Sphere class

def test_sphere__repr__():
    my_sphere = Sphere(0, 0, 0, 1)
    assert  my_sphere.__repr__()== 'Sphere(0, 0, 0, 1)'

def test_sphere_area():
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert  my_sphere.area == 4*math.pi*my_sphere.radius**2

def test_sphere_volume():
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert  my_sphere.volume == (4/3) * math.pi * my_sphere.radius**3         

def test_sphere_is_unit_sphere():
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere.is_unit_sphere() == True            

def test_sphere_is_not_unit_sphere():
    my_sphere = Sphere(x=0,y=0, z=0, radius=2)
    assert my_sphere.is_unit_sphere() == False       

def test_sphere_is_inside_pos():                         
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere.is_inside(0.3,0.3,0.3) == True

def test_sphere_is_not_inside_pos():                         
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere.is_inside(4,4,4) == False

def test_sphere_is_inside_neg():                         
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere.is_inside(-0.3,-0.3,-0.3) == True

def test_sphere_is_not_inside_neg():                         
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere.is_inside(-4,-4,-4) == False

def test_sphere_equality():                            
    my_sphere1 = Sphere(x=0,y=0, z=0, radius=1)
    my_sphere2 = Sphere(x=0,y=0, z=0, radius=1)
    my_sphere3 = Sphere(x=0,y=0, z=0, radius=2)
    assert my_sphere1.__eq__(my_sphere2) == True
    assert my_sphere3.__eq__(my_sphere2) == False

def test_sphere_less_than():                            
    my_sphere1 = Sphere(x=0,y=0, z=0, radius=2)
    my_sphere2 = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere1.__lt__(my_sphere2) == False
    assert my_sphere2.__lt__(my_sphere1) == True

def test_sphere_greater_than():                            
    my_sphere1 = Sphere(x=0,y=0, z=0, radius=2)
    my_sphere2 = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere1.__gt__(my_sphere2) == True
    assert my_sphere2.__gt__(my_sphere1) == False

def test_translate_sphere():    
    my_sphere = Sphere(x=0,y=0, z=0, radius=1)
    assert my_sphere.translate("TRE",5,3) == f"Error: you entered 'TRE', '5' and '3', all have to be numerics."