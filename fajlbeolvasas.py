nevek = []
nemek = []
korok = []

def beolvas(fajlnev):
    fajlom= open(fajlnev,"r", encoding='utf-8')
    print(fajlom)
    '''fejlec= fajlom.readline().strip()
    print(fejlec)'''
    fejlec=fajlom.readline().strip()
    print(fejlec)
    '''sor= fajlom.readline().strip()
    print(sor)'''
    sorok=fajlom.readlines()
    print(sorok)
    feldolgoz(sorok)
    fajlom.close()


def feldolgoz(sorok):
    #tárold el zaz adatkorokokat, nevek, nemek,
    i = 0
    while i<len(sorok):
        print(sorok[i].strip())
        sor = sorok[i].strip().split(", ")
        print(sor)
        nevek.append(sor[0])
        nemek.append(sor[1])
        korok.append(sor[2])
        i+=1

    print(nevek)
    print(nemek)
    print(korok)


#Hány adat van rögzítve a fájlban?
def adatszam():
    print(f"Ennyi adat van összesen: {len(nemek)}")


#Mekkora az emberek átlagos életkora?
def atlagkor():
    i = 0
    osszeg = 0
    while i < len(korok):
        osszeg += korok[i]
        i += 1
    atlag = osszeg / len(korok)
    print(f"Az átlag életkot: {atlag}.")