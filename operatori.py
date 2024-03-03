'''
operatori:
aritmetici: +, -, /, *, %
de comparare: <>, ==, !=, >=, <=
logigi: and, or, !
'''

a = 3
b = 5

print(a + b) # =>8
print(a == b) # a este egal cu b? => False
print(a < b and a < 4) # 3<5 si 3<4? => True Si True => True
print(a < b or a < 2) # 3<5 si 3<2? => True SAU False => True

# cu mama sau tata sau cu ( bunicul si bunica )
mama = True
tata = False
bunicul = False
bunica = False
print( mama or tata or ( bunicul and bunica))