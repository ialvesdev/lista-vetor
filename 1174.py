vet = []
controle = 0
for _ in range(100):
    entrada = float(input())
    vet.append(entrada)
    
for x in range(100):
    if vet[x] <= 10:
        print(f"A[{x}] = {vet[x]}")