szam=int(input("Mennyi nevet szeretnél listába rakni: "))
lista=[]

for i in range(szam):
    n=input(f"A(z) {i+1}. név a listába:  ")
    lista.append(n)

print(lista)
