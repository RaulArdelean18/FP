'''
P6 Agentie de Turism
Ardelean Raul

TO DO:
    ===============================
       MENIU AGENTIE DE TURISM
    ===============================
    1. Adauga pachet nou
    2. Modifica un pachet existent
    3. Afiseaza toate pachetele
    --- Optiuni Stergere ---
    4. Sterge pachetele mai scurte decât o durata
    5. Sterge pachetele cu o destinatie specifica
    6. Sterge pachetele care au pretul mai mare decat o suma data
    --- Optiuni Cautare ---
    7. Cauta pachete intr-un interval de timp
    8. Cauta pachete dupa destinatie si pret
    9. Cauta pachete dupa data de sfarsit
    --- Optiuni Filtrare ---
    10. Filtrare dupa pret si destinatie
    0. Iesire din aplicatie
    ----------------------------------------(done)

    Adaugare: (done)
        -> Adaugare pachet de calatorie (done)
        -> Modifica pachet de calatorie (done)
    Stergere: (done)
        -> Stergerea pachetelor in functie de destinatie (done)
        -> Stergerea pachetelor in functie de durata (done)
        -> Stergerea pachetelor in functie de pret (done)
    Cautare: (done)
        -> Afisarea pachetelor in functie de interval de timp (done)
        -> Afisarea pachetelor in functie de destinatie si buget maxim alocat (done)
        -> Afisarea pachetelor in functie de data de sfarsit (done)

'''

from ui.console import *

def run():
    pachete_turistice = []

    while True:
        ui_meniu()
        optiune = input(">>> Alegeti o optiune: ")

        match optiune:
            case '1':
                ui_adauga_pachet(pachete_turistice)
            case '2':
                ui_modifica_pachet(pachete_turistice)
            case '3':
                ui_afiseaza_pachete(pachete_turistice)
            case '4':
                pachete_turistice = ui_sterge_dupa_durata(pachete_turistice)
                ui_afiseaza_pachete(pachete_turistice, titlu="--- Lista actualizata de pachete ---")
            case '5':
                pachete_turistice = ui_sterge_dupa_destinatie(pachete_turistice)
                ui_afiseaza_pachete(pachete_turistice, titlu="--- Lista actualizata de pachete ---")
            case '6':
                pachete_turistice = ui_sterge_dupa_pret(pachete_turistice)
                ui_afiseaza_pachete(pachete_turistice, titlu="--- Lista actualizata de pachete ---")
            case '7':
                ui_cauta_dupa_interval(pachete_turistice)
            case '8':
                ui_cauta_dupa_destinatie_si_pret(pachete_turistice)
            case '9':
                ui_cauta_dupa_data_sfarsit(pachete_turistice)
            case '10':
                ui_filtrare_oferte_dupa_pret_si_destinatie(pachete_turistice)
            case '11':
                ui_filtrare_dupa_luna(pachete_turistice)
            case '12':
                ui_raport_perioada_sortat(pachete_turistice)
            case '0':
                print("Programul s-a oprit.")
                break
            case _:
                print("Optiune invalida. Va rugam alegeti din lista.")
