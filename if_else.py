# Flow control: if esle
# evalueaza conditii si bifurca codul in functie de rezultat

# if
piesa_faina = True

print('pornim radio')
if piesa_faina == True:
    print('dam mai tare')
    print('fredonam')
print('oprim radio')

# if else
# daca nr este par, printam acest lucru
# altfel printam impar
nr = 1200
# ce inseamna par? se imparte exact la 2
# ce inseamna ca se imparte la 2? ne da restul 0
if nr % 2 == 0:
    print('nr este par')
else:
    print('impar')

# este un nr pozitiv?
if (nr > 0):
    print('pozitiv')
else:
    print('nr nu este pozitiv')

# daca utilizatorul are sub 18 ani, nu poate paria

# if, else if, else
# cum ne saluta robotelul in functie de ora?

# luam date de la tastatura
# ne asiguram ca sunt transformate din str in int
# ora = int(input('introdu ora'))
# # print(ora == 17)
# if ora < 0:
#     print('ora invalida. ora negativa')
# elif ora <= 11:
#     print('buna dimineata')
# elif ora <= 18:
#     print('buna ziua')
# elif ora <= 21:
#     print('buan seara')
# elif ora <= 24:
#     print('noapte buna')
# else:
#     print('ora invalida. ora mai mare decat 24')
# CTRL + / se comenteaza sau decomenteaza

# robotel telefonic
optiunea = int(input('alege o optiune'))
if optiunea == 0:
    print('meniu anterior')
elif optiunea == 1:
    print('lb romana')
elif optiunea == 2:
    print('lb engleza')
else:
    print('nu am identificat optiunea, mai incearca')

