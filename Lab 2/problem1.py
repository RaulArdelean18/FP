#lab2 FP
n = int(input("Introdecti numarul n: "))

a = 1
b = 1

while b<=n:
    c = a + b
    a = b
    b = c

print(f"Cel mai mic numar fibonacci mai mare decat {n} este: {c}")