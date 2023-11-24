szamok = []
def Szam():
    for i in range(5):
        szam = int(input(f"Kérem adja meg az {i + 1}. számot: "))
        szamok.append(szam)

print("Az Ön által megadott számok:", szamok)
