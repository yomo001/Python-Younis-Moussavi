# "Recursive calls" : Generellt vill ej ha sådana, för att inte få sådana här fel (se hans fil), men om det är skrivet vettigt kan det gå. 
# Men i största mån låt inte funktioner anropa varandra runt i cirkel

def main():
    print("Start of main()")

    func_b()
    func_a()
    func_b()

    print("End of main()")
    #...    #punkter betyder pass, jene låt vara 

def func_a():
    print("Start of func_a()")

    func_b()

    print("End of func_a()")

def func_b():
    print("Start of func_b()")
    print("End of func_b()")

def recursive():
    print("Hello")
    recursive()

#recursive()    #fyller på tills stacken fylls upp, blir stack overflow

def print_hello(n):
    for i in range(n):
        print("hello")

def print_hello_recursive(n):     #Som ovan men genom recursive, tar mer minne i call stacken och mer svårläst. Kan ge call stack problem. 
    print("hello")
    if n > 1: print_hello_recursive(n-1)
    return

print_hello_recursive(4)


main()



