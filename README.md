# 🧠 Fundamentele Programării (FP)

## 📘 Descriere
Acest depozit conține lucrările de laborator realizate în cadrul materiei **Fundamentele Programării**, folosind limbajul **Python**.  
Scopul principal al proiectului este exersarea conceptelor fundamentale de programare și construirea treptată a unei aplicații complete, prin aplicarea principiilor de dezvoltare software corecte.

---

## 🗂️ Structura proiectului

### 🧩 Lab 1
- Exerciții introductive în Python  
- Operații simple cu liste și numere  
- Exersarea funcțiilor și a apelurilor recursive

### 🧩 Lab 2
- Aplicație pentru **gestionarea cheltuielilor unei familii**  
- Operații: adăugare, modificare, filtrare, afișare  
- Introducerea validărilor și a testării cu `assert`

### 🧩 Lab 3
- Extinderea aplicației din Lab 2  
- Adăugare de funcționalități suplimentare: filtrare și sortare  
- Separarea codului în module logice  
- Scriere de teste unitare pentru fiecare funcție principală

### 🧩 Lab 4–6 — Aplicația „Agenție de Turism”
Proiectul final al semestrului, dezvoltat incremental în 3 etape:

#### 🔹 Lab 4 – Baza aplicației
- Implementarea funcțiilor de bază: **Adăugare**, **Ștergere**, **Căutare**, **Filtrare**  
- Crearea **arhitecturii pe 3 straturi**:
  - `UI` – interfața utilizator (input/output)
  - `Logică` – implementarea funcțiilor principale
  - `Controller` – legătura dintre UI și logică  
- Primele teste unitare (`assert`) pentru verificarea funcțiilor principale

#### 🔹 Lab 5 – Extindere și refactorizare
- Adăugarea **rapoartelor** (ex: listarea pachetelor după preț, destinație etc.)  
- Introducerea **stratului de domeniu**, cu funcții precum:
  - `creeaza_pachet()`
  - `get_destinatie()`
  - `get_pret()`
- Refactorizarea codului pentru a elimina accesul direct la dicționare  
- Respectarea principiului **separării responsabilităților**

#### 🔹 Lab 6 – Finalizare
- Implementarea funcționalității **Undo**  
- Transformarea funcțiilor pentru a fi **imutabile** (returnează o listă nouă în loc să modifice pe cea existentă)  
- Integrarea completă a testelor și finalizarea aplicației

---

## ⚙️ Rulare
1. Clonează proiectul:
   ```bash
   git clone https://github.com/RaulArdelean18/FP.git
   cd FP
