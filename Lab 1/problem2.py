#problem2 lab1 FP
def prime(n):
    if n < 2:
        return False
    d=2
    while d*d<=n :
        if n%d==0:
            return False
        d+=1

    return True

n = int(input("Introduceti un numar: "))
if prime(n):
    print(f"Numarul {n} este prim")
else:
    print(f"Numarul {n} nu este prim")