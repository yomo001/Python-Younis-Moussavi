# Skriver en egen py fil med massa funktioner. Istället för att köra den från terminalen som innan så importerar vi den. 
# Använder då de funktioner vi själva skrivit i annan fil
# Varför vill man göra så? 
# Anledning till bibliotek : Kan återanvända samt gömma undan detaljer. Vid t.ex. stort projekt, kan man dela upp många smådelar. E
# En klass t.ex. kan vara i en egen fil som heter som klassen, sen importeras den när man vill använda den. Inte två klasser eller funktionaliteter i samma fil.
# Bibliotek: Ngt man laddar in och kan åteanvända: Module och package: modul är en py - fil, package är många fler filer.



def square(n):                        # Denna läggs till minnet när modulen(filen) körs. 
    return n*n 

print("Hello World!")              # Dessa exkvekreras

for i in range(5):
    print(i)

# Man gör inte så normalt sätt i moduler, vill ej ha koder som exkverdreras 

