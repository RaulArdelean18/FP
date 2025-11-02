# problem3 lab1 FP
# algoritmul lui euclid
def gcd(a, b):
    while b != 0:
        r = a % b
        a = b
        b = r
    return a

a = int(input("Introdecti primul numar: "))
b = int(input("Introdecti al doilea numar: "))
print(f"Cel mai mare divizor comun a numerelor {a} si {b} este {gcd(a, b)}")