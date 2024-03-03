# variabila = zona din memorie care tine date
# variabila = cutiuta in care punem valori

# am declarat si initializat variabila marca
marca_masina = 'Volvo'
model_masina = 'XC 60'

# nu putem sa punem spatiu in numele variabilei
# o variabila incepe cu litera mica

# loosly typed - nu trebuie sa specificam tipurile de date

print (f'Am cumparat o masina marca : {marca_masina}')
print (f'Este modelul : {model_masina}')

# suprascriere
model_masina = 'XC 60 facelift'

print (f'Am cumparat o masina marca : {marca_masina}')
print (f'Este modelul : {model_masina}')

nume = 'Zegrean'
prenume = 'Andreea'
varsta = 35
print (nume + ' ' + prenume)
print (f' {prenume} {nume} are varsta de {varsta} ani')