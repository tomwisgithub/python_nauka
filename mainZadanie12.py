produkty = input("Podaj produkty oddzielając je przecinkiem. Np.: chleb,mleko,woda.: ")

koszyk  = produkty.split(",")

print("W Twoim koszyku znajdują się:")

for produkt in koszyk:
    print(produkt)