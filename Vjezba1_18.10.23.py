## Vježbe_01 18.10. Zadaci

### 01. List Operations

# Imate unaprijed definiranu listu bodova (bodovi). 

bodovi = [80, 73, 61, 95, 41, 31]

# *a)* Dodajte nove vrijednosti bodova ( 100 i 22 ) u listu.

bodovi.append (100)
bodovi.append(22)

print(bodovi)

# *b* Ispišite sve parne bodove iz liste i spremite ih u novu listu korištenjem petlje.

parni_brojevi = [x for x in bodovi if x % 2 == 0]
print(parni_brojevi)

#*c)* Izbrišite bodove manje od 40 iz liste *bodovi*.

i = 0 
while i < len(bodovi):
    if bodovi[i] < 40:
        del bodovi[i]
    else:
        i += 1

print(bodovi)

#*d)* Prođite kroz listu *bodovi* korištenjem petlje i ispišite ocjene ovisno o bodovnom pragu.
"""
    90-100 -> Odličan
    80-89 -> Vrlo Dobar
    65-79 -> Dobar
    50-64 -> Dovoljan
    50 -> Nedovoljan 
"""
bodovi = [80, 73, 61, 95, 41, 31]

for bod in bodovi:
    if 90 <= bod <= 100:
        print(f"{bod} -> Odličan")
    elif 80 <= bod <= 89:
        print(f"{bod} -> Vrlo Dobar")
    elif 65 <= bod <= 79:
        print(f"{bod} -> Dobar")
    elif 50 <= bod <= 64:
        print(f"{bod} -> Dovoljan")
    else:
        print(f"{bod} -> Nedovoljan")


### 02. Library Management
#Napišite program koji demonstrira upravljanje informacijama o knjigama u obliku rječnika. 

knjiznica = {
    'Harry Potter': {'autor': 'J.K. Rowling', 'godina': 2001, 'dostupno': 5},
    'Lord of the Rings': {'autor': 'J.R.R. Tolkien', 'godina': 1954, 'dostupno': 3}
}
        
"""
*a)* Dodajte novu knjigu u knjižnicu:

    * Naslov: Witcher
    * Autor: Andrzej Sapkowski
    * Godina izdanja: 1994
    * Stanje dostupnosti: 0
"""

nova_knjiga = {
    "Naslov" : "Witcher",
    "autor" : "Andrzej Sapkowski",
    "godina": "1994",
    "dostupno" : 0
    }

knjiznica['Witcher'] = nova_knjiga

print(knjiznica)

#*c)* Izbrišite knjigu iz knjižnice (samostalno odaberite).

del knjiznica ["Lord of the Rings"]

print(knjiznica)

#*d)* Prođite kroz sve naslove u knjižnici i provjerite dostupnost knjiga. Ako knjiga ima barem jedan primjerak ispišite u konzolu naslov knjige te da je dostupna, inače napišite da naslov nije dostupan.


for naslov, knjiga in knjiznica.items():
    if 'dostupno' in knjiga and knjiga['dostupno'] > 0:
        print(f"{naslov} je dostupna.")
    else:
        print(f"{naslov} nije dostupna.")


#### 03. List Comprehension
#Napravite listu brojeva od 1 do 100.

brojevi = list(range(1, 101))
print (brojevi)

filtrirani_brojevi = [broj for broj in brojevi if 49 <= broj <= 80]

print(filtrirani_brojevi)


#4.

studenti = {
    "Ana": 100,
    "Marko": 25,
    "Petra": 49,
    "Ivan": 56,
    "Mia": 89,
    "Lovro": 80,
    "Stipe": 73,
    "Lea": 60,
    "Tomislav": 51,
    "Leo": 99
}

filtrirani_studenti = {ime: bodovi for ime, bodovi in studenti.items() if len(ime) > 3 and bodovi >= 50}

print(filtrirani_studenti)
