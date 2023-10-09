# När det gäller testning av koden, brukar man säga att man vill testa
# gränsfall, "Edge cases", där man täcker in viktiga scenarion som ser om koden funkar som den ska.


import math                           

def main():
    greet()                    
    print(square(2))
    print(square(3))
    print(square(-3))
    print(square(0))
    print(square(1.2))


def square(n):                        
    return n * n                       

def sqrt(n):                        
    return math.sqrt(n)                     

def greet(name = "world"):                        
    return(f"Hello, {name}")   

if __name__ == "__main__":             
    main()

