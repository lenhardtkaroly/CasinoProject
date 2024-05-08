import random

def dob_kockak():
    return [random.randint(1, 6) for _ in range(5)]

def ellenoriz_dupla(kockak):
    for kocka in kockak:
        if kockak.count(kocka) == 2:
            return True
    return False

def ellenoriz_tripla(kockak):
    for kocka in kockak:
        if kockak.count(kocka) == 3:
            return True
    return False

def ellenoriz_dupla_tirpla(kockak):
    return ellenoriz_dupla(kockak) and ellenoriz_tripla(kockak)

def ellenoriz_kis_sor(kockak):
    kockak.sort()
    for i in range(len(kockak)-1):
        if kockak[i] + 1 != kockak[i+1]:
            return False
    return True

def ellenoriz_nagy_sor(kockak):
    kockak.sort()
    for i in range(len(kockak)-1):
        if kockak[i] != kockak[i+1] - 1:
            return False
    return True

def kockapoker(kockak):
    kockak_str = ", ".join(str(k) for k in kockak)
    if ellenoriz_dupla_tirpla(kockak):
        return f"Dobások: {kockak_str}. Eredmény: Dupla tirpla"
    elif ellenoriz_kis_sor(kockak):
        return f"Dobások: {kockak_str}. Eredmény: Kis sor"
    elif ellenoriz_nagy_sor(kockak):
        return f"Dobások: {kockak_str}. Eredmény: Nagy sor"
    elif ellenoriz_tripla(kockak):
        return f"Dobások: {kockak_str}. Eredmény: Tripla"
    elif ellenoriz_dupla(kockak):
        return f"Dobások: {kockak_str}. Eredmény: Dupla"
    else:
        return f"Dobások: {kockak_str}. Eredmény: Nincs semmi"

# Szimuláció
dobasok_szama = 10

for i in range(dobasok_szama):
    kockak = dob_kockak()
    print(kockapoker(kockak))
