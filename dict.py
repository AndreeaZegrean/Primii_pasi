# dictionare
lista_goala = []
dict_gol = {}

# declaram si initializam un dict
note_elevi = {'Gigel': 10,'Costel': 9, 'Ana': 10 }

# adaugam elemente
note_elevi['Sebi'] = 7

# printam dict
print(note_elevi)

# aflam notele
print(note_elevi['Sebi'])
print(note_elevi.get('Gigel'))

# actualizam valori
note_elevi['Costel'] = 10
print(note_elevi)

# aflam dimensiunea
print(len(note_elevi))

# sterg valori
note_elevi.pop('Gigel')
print(note_elevi.get('Gigel', 'nu  mai avem acest elev')) # merge si cu pop in loc de get
print(note_elevi)

# returneaza doar cheile
print(note_elevi.keys())