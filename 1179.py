par = []
impar = []
for _ in range(15):
    x = int(input())
    
    if x % 2 == 0:
        if len(par) == 5:
            for i in range(5):
                print(f"par[{i}] = {par[i]}")
            par.clear()
            par.append(x)
        else:
            par.append(x)
    else:
        if len(impar) == 5:
            for y in range(5):
                print(f"impar[{y}] = {impar[y]}")
            impar.clear()
            impar.append(x)
        else:
            impar.append(x)
            
n = 0
k = 0
while k < len(impar):
    print(f"impar[{k}] = {impar[k]}")
    k+=1
while n < len(par):
    print(f"par[{n}] = {par[n]}")
    n+=1