qtdTermo = int(input())
termos = []
for _ in range(qtdTermo):
    n = int(input())
    termos.append(n)

fibonacci = [0, 1]
i = 1
for _ in range(59):
    valor = fibonacci[i] + fibonacci[i-1]
    fibonacci.append(valor)
    i += 1
    
for m in range(qtdTermo):
    print(f"Fib({termos[m]}) = {fibonacci[termos[m]]}")