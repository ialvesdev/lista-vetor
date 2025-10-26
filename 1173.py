vet = []
p = int(input())
vet.append(p)
for y in range(0, 9):
    prox = vet[y] * 2
    vet.append(prox)

for x in range(0, 10):
    print(f"N[{x}] = {vet[x]}")
    
    