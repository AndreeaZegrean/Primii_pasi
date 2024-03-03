from oop.cont_bancar import ContBancar

cont1 = ContBancar('Deea', 'RO001')
cont2 = ContBancar('Monica', 'RO002')

cont1.activareCont(7777)
cont2.activareCont(3333)
cont2.activareCont(7777)

cont1.alimentareCont(300)
cont2.alimentareCont(700)
cont2.alimentareCont(300)

cont1.plataCard(500)
cont1.plataCard(300) # 0
cont2.plataCard(100)
cont2.plataCard(200) # 700

cont1.interogareSold()
cont2.interogareSold()

# tema
# clasa angajat
# nume, prenume, salariu, vechime, functie
# constructor: nue, prenume, salariu, functie, vechime
# metode
# descriere
# marire salariu in functie de vechime
# actualizare vechime ( parametru noua vechime)
    # self.vechime = noua_vechime
# daca are vechime sub 5 ani, marim cu 300 lei, daca are peste 5 ani - 500 lei