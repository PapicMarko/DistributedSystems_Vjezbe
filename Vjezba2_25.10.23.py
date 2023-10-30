#Vjezba 2 _ 25.10.23.


### 01. Filtriranje liste
#Napravite Python funkciju koja prima listu brojeva i izvodi sljedeće operacije:

#1. Filtrira sve parne brojeve iz liste.
#2. Kvadrira svaki preostali broj.
#3. Sortira rezultirajuću listu od najmanjeg prema najvećem broju.


lista = [25, 22, 13, 44, 51, 36, 77, 18, 99, 16]


def obradi_listu(lista):
    # Korak 1: Filtriranje parnih brojeva
    parni_brojevi = list(filter(lambda x: x % 2 == 0, lista))
    
    # Korak 2: Kvadriranje preostalih brojeva
    kvadrirani_brojevi = list(map(lambda x: x ** 2, lista))
    
    # Korak 3: Sortiranje kvadriranih brojeva
    kvadrirani_brojevi.sort()
    
    return parni_brojevi, kvadrirani_brojevi


lista = [25, 22, 13, 44, 51, 36, 77, 18, 99, 16]
parni, kvadrirani = obradi_listu(lista)


print ("Parni brojevi su: ", parni)
print ("Kvadriranje preostalih brojeva: ", kvadrirani)





"""
02. Brojač slova 

`count_letter(rijec, slovo)`: Ova funkcija prima dva argumenta, riječ ili frazu (`rijec`) i slovo (`slovo`), te vraća broj pojavljivanja slova u riječi ili frazi. Usporedba treba biti nesensitivna na velika i mala slova, što znači da se slova 'A' i 'a' smatraju istim slovom. ( HINT : Pogledaj funkciju ".lower()" )

Riječ/Frazu i slovo možete definirati unaprijed ili napisati funkciju koja prima input od korisnika

"""
    


def count_letter(rijec, slovo):
    # Pretvaramo cijelu riječ u mala slova kako bismo omogućili nesensitivnu usporedbu
    rijec = rijec.lower()
    slovo = slovo.lower()

    count = 0
    for karakter in rijec:
        if karakter == slovo:
            count += 1
    return count

# Unos riječi i slova od korisnika
rijec = input("Unesite riječ ili frazu: ")
slovo = input("Unesite slovo koje želite prebrojati: ")

# Poziv funkcije i ispis rezultata
broj = count_letter(rijec, slovo)
print(f"Slovo '{slovo}' se pojavljuje {broj} puta u riječi ili frazi '{rijec}'.")



"""03. Lambda string
Imate listu stringova, Vaš zadatak je filtrirati tu listu i vratiti samo one stringove koji sadrže određeni znak, poput slova 'a'.
"""

stringovi = ["banana", "jabuka", "kruška", "naranča", "limun"]

# Znak koji tražimo
trazeni_znak = 'b'

# Koristite lambda izraz za filtriranje stringova koji sadrže trazeni_znak
filtrirani_stringovi = list(filter(lambda x: trazeni_znak in x, stringovi))

# Ispišite rezultat
print(f"Stringovi koji sadrže znak '{trazeni_znak}':")
for string in filtrirani_stringovi:
    print(string)



"""04. Lambda kvadrat
Imate listu brojeva, Vaš zadatak je kvadrirati sve brojeve te liste.
Nakon toga napravite još i filtraciju liste kvadriranih brojeva u zasebnom lambda izrazu gdje izdvajate neparne i brojeve manje od 100."""

lista_br = [5, 7, 17, 24, 256, 22, 31, 55, 150, 53]

kvadriranje_liste = list(map(lambda x: x ** 2, lista_br))
filtracija_liste = list(filter(lambda x: x % 2 == 1 and x < 100, lista_br))

print(kvadriranje_liste)
print(filtracija_liste)