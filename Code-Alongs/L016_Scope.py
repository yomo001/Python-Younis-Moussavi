# Scope, life-time a variable
# In python we have 2 types of scopes
# Local scope: Only available locally in a function
# Global scope: Available through execution of program.


# Recommended to start defining functions first and the code, for clarity,
# HA INTE MED GLOBALA VARIABLER I FUNKTION MEN SKICKA MED DOM SOM ARGUMENT IFALL MAN VILL HA DET 
# Man kommer åt global inuti funktionen, men sätter man lokal med samma namn bestämmer den.

name = "Fredrik"

def main():
    global name      #Här talar man om at man vill använda global name i funktionen, normalt vill man inte göra så. Man vill att en funktion ska funka fristående utan sådana beroenden.
    name = "Kalle"   #Även om global name variabel finns gå det använda lokal också 
    print(name)   #Här skrivs Fredrik ut, den kommer åt global OM inte lokal variabel med samma namn finns, behöver ej ange global

print(name)

main()

# print(name)   NameError - variabel inuti function available locally and not gilty outside, only when function is called
#  Lägger sedan till ny variabel  = "Fredrik" globally längst upp

print(name)

# Output: Hossein Fredrik

# Python doesnt have block scopes but this is used in most other languages, such as c#, c++, java
# Variabler som definieras i ett "block-scope" är bara giltigt inuti blocket i andra språk, MEN I PYTHON FUNKAR ÄVEN UTANFÖR
if name == "Fredrik":
    last_name = "Johansson"

print(last_name)

for i in range(10):
    print(i)

print(f"{i = }")         # Skriver ut det sista värdet

