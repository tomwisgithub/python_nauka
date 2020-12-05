pilkarze = ['Maradona', 'Pele', 'Boniek', 'Zidane', 'Buffon', 'Giggs', 'Deyna', 'Khan', 'Charlton', 'Lato']

print(pilkarze[0])
print(pilkarze[1])
print(pilkarze[2])
print("="*15)

for p in pilkarze:
    print(p)

print("="*15)

for idx in range( len(pilkarze) ) :
    print("idx: " + str(idx) + ":" + pilkarze[idx])

print("="*15)

addNew = input("Dodaj nazwisko ulubionego pilkarza do listy: ")
pilkarze.insert(0, addNew)

for p in pilkarze:
    print(p)