N = int(input())         
vet = list(map(int, input().split()))
controle = vet[0]
local = 0

for y in range(1, len(vet)):
    if vet[y] < controle:
        controle = vet[y]
        local = y

print(f"Menor valor: {controle}")
print(f"Posicao: {local}")
