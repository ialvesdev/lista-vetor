vet = [int(input()) for _ in range(20)]

for i in range(10):
    vet[i], vet[19 - i] = vet[19 - i], vet[i]

for i, v in enumerate(vet):
    print(f"N[{i}] = {v}")
