def printGreeting():
    print('Buna ziua! Bine ati venit!')

def printGreetingByName(nume, prenume):
    print(f'Buna ziua {nume} {prenume}')

def mediaNr(a, b, c):
    return (a + b + c) / 3

def piValue():
    return 3.14

# zona de apelare (desktop)
printGreeting()
printGreeting()
printGreetingByName('Deea', 'M')
printGreetingByName('Deea', 'Monica')
printGreetingByName('Deea', 'Asha')
print(mediaNr(3,3,4))
print(piValue())

# exercitiu
# daca pers e majora, afisati true, altfel false
def verificareMajor(varsta):
    if varsta >= 18:
        return True
    else:
        return False
print(verificareMajor(17))

# se ia varsta utlizatorului
age = int(input('introduceti varsta dvs'))
if verificareMajor(age):
    print('Cont creat. Bine ai venit in aplicatie')
else:
    print('Nu ai varsta minima necesara')

# oop
# variabile => atributite, proprietati sau fields
# functii => metode