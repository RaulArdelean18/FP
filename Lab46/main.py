from Lab46.app.controller import run_UI
from Lab46.app.parsare_controller import run_parsing

if __name__ == "__main__":
    print("Selectati modul de rulare:")
    print("  1. Mod Interactiv (Meniu UI)")
    print("  2. Mod Parsing (Sir de comenzi)")

    mod = input(">>> Alegeti modul (1 sau 2): ")

    if mod == '1':
        run_UI()
    elif mod == '2':
        print("\nIntrare in Modul Comanda...")
        run_parsing()
    else:
        print("Mod invalid. Programul se va opri.")