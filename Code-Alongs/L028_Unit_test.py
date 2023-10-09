import L027_Module
# import L027_Module as m           # Här kan vi kalla modulen för m i filen när vi vill använda den
# from L027_Module import square    # Här importerar vi enbart funktionen square från metoden. Om det t.ex. är jätte
                                    # -stora bibliotek och man inte vill belasta minnet för mkt med sånt man ej behöver använda.

# När vi enbart importerar, när python då exekverar den raden ("import L027_Module")
# Då exekerar den koden i den modulen. 
# Därför normalt i en modul vill man inte ha kod som exekverar 

# Däremot funktioner som definieras, de körs inte om vi inte anropar dom. 
# Så om det inte funnits exekverande kod, och enbart finns en definierad funktion
        # Då hade inget körts om vi importerar modulen utan att anropa funktionen

# Vad händer om vi har exekverande kod, men även anropar en funktion i modulen? 
print(L027_Module.square(3))    # Efter att den kört samtlig exekverande kod i modulen, kör den sedan denna funktion som anropas
                                # Därför ska man inte ha exekverande kod i modulen som gör det rörigt

# print(m.square(3))             # om man importerat såhär istället: import L027_Module as m 

# print(square(3))              # om man importerat såhär istället: from L027_Module import square

