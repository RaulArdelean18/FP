# problem1 lab1 FP
n = int(input("Cate numere vrei sa aduni? "))  # am citit n, n = cate numere citim din consola
v = list(map(int, input(f"Introdu cele {n} numere ").split()))
# in suma o sa am suma finala a celor n numere din vector
suma = 0

#parcurgem vectorul pentru a aduna valorile in suma
for i in range(n):
    suma += v[i]

#afisez suma celor n numere
print(f"Suma celor {n} valori introduse este {suma}")