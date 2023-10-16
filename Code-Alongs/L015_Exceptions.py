#print("Hello)    #syntax error, skrivit fel i koden, ger syntax error
#print(f"Your name is {x}")      #Run time error ("name error", name inte definierad), ej fel i kod men under körning krashar för ngt är fel

#name = input("Enter name: ") 
#print("Your name is {x}")      # Logical error, program körs (ingen syntax eller run time error), men ej det resultat vi ville ha

def input_int(prompt = "Input: "):
    while True:
        try:   # try används när man vet att ngt kan gå fel, man ber den testa ngt under visst villkor
            #my_int = int(input(prompt))   #man kan förutspå vad som hade kunnat ge runtime error, t.ex. att ngn anger en 
            # sträng här och hantera detta i koden
            #print(x)                #bästa är dock att ha varje sak i egen try-except, eftersom det är olika saker.
            return int(input(prompt))          #istället för under else går att ha här, även istället för my_int =
        except ValueError:       #man specificerar att det är vid denna typ av fel vi vill köra try/except, och lägger den kod man faktiskt tror kan få fel i kodblocket
            print("my_int is not an integer.")
        #except NameError:       # Flera except går att ha. Den tar dock den första som är true
            #print("x is not defined")
        #except:
        # print("Some other kind of error")

        #else:            #try o except hänger alltid ihop, men går lägga till else t.ex.i python, som körs om inget går fel
            #break      Behövs ej med en return
            #return my_int     #avbryter    hela funktionen och ger tillbaka värdet, därför hade inte break behövts


age = input_int("Input age: ")
length = input_int("Input length: ")
weight = input("Input weight: ")

print(f"age = {age}, length = {length}, weigt = {weight}")

