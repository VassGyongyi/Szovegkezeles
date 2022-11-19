

#nagybetűssé alakít
szoveg=""

def hossz(szoveg):
    print(szoveg)
    if (len(szoveg) > 10):
        print(f'A szöveg hossza: {len(szoveg)}')

def nagybetu():
    szoveg = input('Kerek egy szöveget: ')
    print(szoveg.upper())
    hossz(szoveg)

def harom_betu():
    szo=""
    while (len(szo) <= 3):
        szo = input('Kérek egy legalább 3 betűs szót: ')
    print(szo)

def keres():
    i = 0
    index = -1
    szov = input('Kérek egy szöveget: ')
    while ( i < len(szov) and szov[i].upper() != 'A'):
        i += 1
    if i < len(szov):
            print(f'Az első "a" karakter a {i+1}.')
    else:
            print('Nem tartalmaz "a" betűt.')

def keres_ossz():
    i = 0
    index = -1
    darab = 0
    szov = input('Kérek egy szöveget: ')
    while (i < len(szov)):
        if (szov[i].upper() == 'A'):
            darab += 1
        i += 1
    if darab != 0:
        print(f'{darab} db "a" karaktert tartalmaz.')
    else:
        print('Nem tartalmaz "a" betűt.')

"""def nev_be():
    be = ""
    nev =""
    nevek= []
    be = input('Adj meg neveket @ karkterig:' )
    while (be != "@"):
        nev= be
        while (be != " "):
            nev = be
    nevek.append(nev)"""
