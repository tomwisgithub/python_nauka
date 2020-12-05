samochod = {'name': 'Mercedes',
            'przebieg': 100000,
            'type': 'osobowy'}

print(samochod['name'])
print(samochod['type'])

print("="*20)

for key in samochod:
    print("{0}:{1}".format(key, samochod[key]))

print("="*20)

for key, value in samochod.items():
    print("{0}:{1}".format(key, value))