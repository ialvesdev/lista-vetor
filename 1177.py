vet = []
t = int(input())
cont = 0
amg = 0
while cont < 1000:
    if amg == t:
        amg = 0
    vet.append(amg)
    amg += 1
    cont += 1
    
for j in range(1000):
    print(f"N[{j}] = {vet[j]}")
    