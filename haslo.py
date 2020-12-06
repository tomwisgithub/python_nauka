haslo = input("Podaj haslo: ")
if len(haslo) < 3:
    print('Za krótkie hasło.')
else:

    znaki_do_ukrycia = haslo[1:-1]
    #print(znaki_do_ukrycia)

    ukryte = znaki_do_ukrycia.replace(znaki_do_ukrycia,'*'*len(znaki_do_ukrycia))
    #print(ukryte)

    print("Twoje haslo to: ",haslo[0]+ukryte+haslo[-1])