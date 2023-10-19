from geometry_shapes import Circle, Rectangle

# Main ska ligga som en egen. 
def main():
    
    # Controls from labb3 assignment instructions. All passed.
    cirkel1 = Circle(x=0,y=0, radius=1) # enhetscirkel
    cirkel2 = Circle(x=1,y=1, radius=1)
    rektangel = Rectangle(x=0,y=0,width=1, height=1)
    print(cirkel1==cirkel2) # True
    print(cirkel2==rektangel) # False
    print(cirkel1.is_inside(0.5, 0.5)) # True
    print(cirkel1.is_inside(5, 5)) # False
    cirkel1.translate("TRE",5) # ge ValueError med lämplig kommentar
    # cirkel1.plot()
    # cirkel1.plot(0.3,0.3)
    # rektangel.plot()
    # rektangel.translate(1,0)
    # rektangel.plot()
    
if __name__ == "__main__":               # To avoid "loose code" from running when importing module
    main()
