# 🧠 Fundamentele Programării (FP)

## 📘 Descriere
Acest depozit conține lucrările de laborator realizate în cadrul materiei **Fundamentele Programării**, folosind limbajul **Python**.  
Scopul proiectului este înțelegerea conceptelor fundamentale de programare, prin exerciții practice și dezvoltarea treptată a unei aplicații mai complexe.

---

## 🗂️ Structura proiectului

### 🧩 Lab 1
- Exerciții introductive în Python  
- Operații simple cu liste și numere  
- Exersarea funcțiilor și apelurilor recursive

### 🧩 Lab 2
- Program care citește un număr `n` și determină **cel mai mic număr Fibonacci mai mare decât `n`**  
- Implementare iterativă, folosind variabile `a`, `b`, `c` pentru generarea șirului Fibonacci

### 🧩 Lab 3
- Program interactiv care lucrează cu **liste de numere întregi**  
- Funcționalități principale:
  - citirea și validarea unei liste de la tastatură;
  - verificarea numerelor prime (`verify_prime_number`);
  - identificarea **celor mai lungi secvențe** din listă care respectă anumite criterii:
    - cerința 4 → secvență de numere prime;
    - cerința 5 → secvență de elemente egale consecutive;
    - cerința 7 → secvență în care diferența absolută dintre elemente consecutive este număr prim.
- Afișează toate secvențele maxime care respectă criteriul ales de utilizator.

### 🧩 Lab 4–6 — Aplicația „Agenție de Turism”
Proiect dezvoltat în trei etape (iterații), având ca obiectiv construirea unei aplicații complete, respectând două principii software esențiale:

#### 🔹 Test-Driven Development (TDD)
- Testele au fost scrise cu `assert` pentru a verifica funcțiile înainte de testarea manuală.

#### 🔹 Arhitectura pe 3 straturi
- **UI (`ui/console.py`)** — gestionează interacțiunea cu utilizatorul (input/output).  
- **Logică (`data_base/services.py`)** — conține operațiile principale (adăugare, ștergere, filtrare etc.).  
- **Controller (`app/controller.py`)** — leagă interfața de logica aplicației.

#### 🔹 Evoluția proiectului:
- **Lab 4 (Baza):** Implementarea funcțiilor de bază (Adăugare, Ștergere, Căutare, Filtrare) și primele teste.  
- **Lab 5 (Extindere și Refactorizare):** Introducerea stratului de domeniu (`creeaza_pachet`, `get_destinatie`, `get_pret`) și a rapoartelor.  
- **Lab 6 (Finalizare):** Implementarea funcționalității **Undo** și modificarea funcțiilor pentru a fi **imutabile** (returnează liste noi în loc de modificarea celor existente).

---

## ⚙️ Rulare
1. Clonează proiectul:
   ```bash
   git clone https://github.com/RaulArdelean18/FP.git
   cd FP
