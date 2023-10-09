# En Module är: 
# En egen py fil med funktioner. Istället för att köra den från terminalen som innan så importerar vi den. 
# Använder då de funktioner vi själva skrivit i annan fil
# Varför vill man göra så? 
    # Kan återanvända samt gömma undan detaljer. Vid t.ex. stort projekt, kan man dela upp många smådelar.
    # En klass t.ex. kan vara i en egen fil som heter som klassen, sen importeras den när man vill använda den. 
        # Inte två klasser eller funktionaliteter i samma fil.
# Bibliotek: Ngt man laddar in och kan återanvända. 
    # I python pratar man specifkt om Module och package som bibliotek: modul är en py - fil, package är många fler filer.

import math                           # Man kan importera moduler i modulfiler. Då kommer filen man importerar den till
                                      # att läsa av den, exekvera den och sedan exekvera övrigt i modulen
                                      # Om math även importeras separat tillsammans med denna modul, DÅ kan man använda dess 
                                      # funktioner även i den andra filen dit modulen importeras. Det blir inte dubbelt i minnet
                                      # Python skriver bara över det (se L028_Unit_test)

def main():                           
    for i in range(5):                  
        print(f"{i} = {square(i)}")


def square(n):                        # Denna läggs till minnet när modulen(filen) körs. MEN den körs inte OM vi INTE ANROPAR DEN. 
    return n*n                        # Däremot gör den objektet (funktionen i minnet i filen dit den importeras) - så den går att anropa där.

#print("Hello World!")                 # Dessa exkvekreras direkt i filer där man importerar denna modul. Vill undvika sånt

#for i in range(5):                    # Dessa exkvekreras direkt i filer där man importerar denna modul. Vill undvika sånt
#    print(i)                          # Man gör inte så normalt sätt i moduler, vill ej ha koder som exkverdreras 



#print(__name__)                        # Python sätter denna automatiskt så fort filen läses in. 
                                       # Om man exekverar koden i denna fil, så kommer denna print att ge output: 
                                       # "__main__"
                                       # OBS - om denna modul/fil körs i en annan fil som importerar modulen, blir output istället:
                                       # "L027_Module" - namnet på modulen. 
                                       # Alltså om den körs direkt i samma fil, sätter den till "__name__", 
                                       # Annars sätter den det till modulnamnet, "L027_Module" i detta fall
                                       # Ibland vill man att koden ska gå att köra som modul men också direkt från commandline.
                                       # Se högst upp def main() för detta. 


if __name__ == "__main__":             # Nu printar jag inte __name__ från koden ovan. 
   main()                              # Istället väljer att köra funktionen OM __name__ för denna fil jag står 
                                       # i == __main__, vilket innebär att det ska vara modulfilen.
                                       # När man då kör en fil som importerar modulen, laddar den in de funktioner som finns
                                       # men kör inte main

# ALLTSÅ
# När man importerar en fil, kör den den kod som finns i filen. 
        # Sätt att undvika detta är att sätta if satsen:
            # if __name__ == "__main__": 
                # main() 
                # Då kommer den att köras enbart om man kör den i modulfilen. 
                # Filer där man importerar modulen kommer bara köra kod från de funktioner man anropar.
                # Här var bara exempel på for loopen för att visa hur __main__ if sats gör att 
                # koden för mainfunktionen bara körs i modulfilen och inte i filer man importerar till.
# ALLTSÅ 
# Med detta kan utvecklaren i modulfilen exekvera funktioner, se output men göra det under main funktionen. 
# Då kommer inte samma kod exekveras i den fil där man importerar modulen, inga "side effects"
    # Man använder då istället medvetet de funktioner man faktiskt vill använda i de filer man importerar moduler till.


