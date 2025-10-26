vet = []

for _ in range(0,10):
    x = int(input())
    if x <= 0:
        vet.append(1)
    else:
        vet.append(x)
    
for x in range(0,10):
    print(f"X[{x}] = {vet[x]}")