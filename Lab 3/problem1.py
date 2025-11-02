# verify if n is a prime number
def verify_prime_number(n):
    if n < 2:
        return False
    elif n == 2 or n == 3:
        return True
    elif n % 2 == 0 or n % 3 == 0:
        return False

    # we need to verify if n is a multiple of 6 * k + 5, 6 * k + 7, or 6 * k + 9
    # 6 * k + 9 is a multiple of 3, so we can skip it
    # therefore, we only need to check if n is a multiple of 6 * k + 5 or 6 * k + 7

    d=5
    while d * d <= n:
        if n % d == 0 or n % (d+2) == 0:
            return False
        d += 6

    return True

# we verify if the criteria a[idx-1] == a[idx] is true
def operatiunea5(arr, idx):
    if idx == 0:
        return True

    if arr[idx] != arr[idx - 1]:
        return False
    else:
        return True

def operatiunea7(arr, idx):
    if idx == 0:
        return True
    if verify_prime_number(abs(arr[idx] - arr[idx - 1])):
        return True
    else:
        return False

# we print the array to check if it's stored correctly in memory
def write(arr):
    print(f"Lista ta este: {arr}")

def citeste_lista():
    while True:
        try:
            n = int(input("Introduceti size-ul listei: "))
            break
        except ValueError:
            print("Va rugam sa introduceti un numar intreg.")
            continue

    while True:
        try:
            arr = list(map(int, input("Introduceti lista: ").split()))
            if len(arr) != n:
                print(f"Dimensiunea listei este incorecta. Introduceti exact {n} numere.")
                continue
            break
        except ValueError:
            print("Va rugam introduceti doar numere intregi separate prin spatiu.")

    return n, arr

n, arr = citeste_lista()

write(arr)

while True:
    try:
        cerinta = int(input("\nIntroduceti task-ul dorit (1 - daca vrei sa citesti o alta lista, numerele 4, 5, 7 pentru cerintele posibile sau alt numar pentru oprirea programului): "))
    except ValueError:
        print("Va rugam sa introduceti un numar intreg.")
        continue

    if cerinta == 1:
        n, arr = citeste_lista()
        continue

    if not (cerinta == 4 or cerinta == 5 or cerinta == 7):
        print("Programul s-a oprit.")
        break

    contor = 0
    lungime_maxima = 1
    pointer_stanga = 0
    pointer_dreapta = -1
    v = []

    for i in range(n):
        if cerinta == 4:
            if verify_prime_number(arr[i]):
                contor += 1
            else:
                contor = 0
        elif cerinta == 5:
            if operatiunea5(arr, i):
                contor += 1
            else:
                contor = 1
        elif cerinta == 7:
            if operatiunea7(arr, i):
                contor += 1
            else:
                contor = 1

        if lungime_maxima < contor:
            lungime_maxima = contor
            pointer_dreapta = i
            pointer_stanga = i - contor + 1
            v = [(pointer_stanga, pointer_dreapta)]
        elif lungime_maxima == contor:
            pointer_dreapta = i
            pointer_stanga = i - contor + 1
            v.append((pointer_stanga, pointer_dreapta))

    # afisare rezultat
    print(f"Secventele de lungime maxima pentru cerinta {cerinta} sunt: [", end="")
    for i in range(len(v)):
        index_stanga, index_dreapta = v[i]
        print("[", end="")
        print(",".join(map(str, arr[index_stanga:index_dreapta + 1])), end="]")
        if i != len(v) - 1:
            print(", ", end="")
    print("]")