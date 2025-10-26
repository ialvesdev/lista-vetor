x = float(input())
vet = []
vet.append(x)
metade = x
for y in range(1, 100):
    metade = metade / 2
    vet.append(metade)
    
for i in range(100):
    print(f"N[{i}] = {vet[i]:.4f}")