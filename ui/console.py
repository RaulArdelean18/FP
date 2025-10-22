from data_base.services import *
from utilitati.date_converter import *

def citeste_data_validata(mesaj_prompt):
    """
    Citeste si valideaza o data de la utilizator.
    """
    data_obj = None
    while data_obj is None:
        data_str = input(mesaj_prompt)
        data_obj = converteste_string_in_data(data_str)
        if data_obj is None:
            print("Format data invalid. Te rog reincearca.")
    return data_obj

def ui_adauga_pachet(lista_pachete):
    """
    Citeste datele de la utilizator și adaugă un pachet nou, cu validare completa.
    """
    print("\n--- Adaugare pachet nou ---")
    destinatie = input("Introduceti destinatia: ")

    while True:
        data_inceput = citeste_data_validata("Introduceti data de inceput (zz/ll/aaaa): ")
        data_sfarsit = citeste_data_validata("Introduceti data de sfarsit (zz/ll/aaaa): ")
        if data_sfarsit > data_inceput:
            break
        else:
            print("Data de sfarsit trebuie sa fie dupa data de inceput. Va rugam reintroduceti perioada.")

    try:
        pret = float(input("Introduceti pretul: "))
        adauga_pachet(lista_pachete, destinatie, data_inceput, data_sfarsit, pret)
        print("Pachet adaugat cu succes!")
    except ValueError:
        print("Pretul trebuie sa fie un numar.")

def ui_afiseaza_pachete(lista_pachete, titlu="--- Lista de pachete ---"):
    """
    Afiseaza toate pachetele dintr-o lista data.
    """
    print(f"\n{titlu}")
    if not lista_pachete:
        print("Lista este goala.")
        return False # Returneaza False daca lista e goala

    for i, pachet_curent in enumerate(lista_pachete):
        destinatia = pachet_curent['destinatie']
        perioada_start = format_data_manual(pachet_curent['data_inceput'])
        perioada_stop = format_data_manual(pachet_curent['data_sfarsit'])
        pretul = pachet_curent['pret']

        text_de_afisat = (
            f"{i + 1}. Destinație: {destinatia}, "
            f"Perioada: {perioada_start} - {perioada_stop}, "
            f"Preț: {pretul:.2f}"
        )
        print(text_de_afisat)
    return True # Returneaza True daca a afisat ceva

def ui_sterge_dupa_durata(lista_pachete):
    """
    Citeste durata si actualizeaza lista principala.
    """
    try:
        durata = int(input("Introduceti durata minima a pachetelor de pastrat (zile): "))
        lista_actualizata = sterge_dupa_durata(lista_pachete, durata)
        print(f"Au fost eliminate {len(lista_pachete) - len(lista_actualizata)} pachete.")
        return lista_actualizata
    except ValueError:
        print("Durata trebuie sa fie un numar intreg.")
        return lista_pachete

def ui_sterge_dupa_destinatie(lista_pachete):
    """
    Citeste destinatia si actualizeaza lista principala.
    """
    destinatie = input("Introduceti destinatia pe care vreti sa o stergeti: ")
    lista_actualizata = sterge_dupa_destinatie(lista_pachete, destinatie)
    pachete_eliminate = len(lista_pachete) - len(lista_actualizata)

    if pachete_eliminate > 0:
        print(f"Au fost eliminate {pachete_eliminate} pachete cu destinatia '{destinatie}'.")
    else:
        print(f"Nu a fost gasit niciun pachet cu destinatia '{destinatie}'.")
    return lista_actualizata

def ui_sterge_dupa_pret(lista_pachete):
    """
    Citeste destinatia si actualizeaza lista principala.
    """
    try:
        pret = int(input("Introduceti pretul maxim pe care il doriti sa il aveti in lista: "))
        lista_actualizata = sterge_dupa_pret(lista_pachete, pret)
        pachete_eliminate = len(lista_pachete) - len(lista_actualizata)
        if pachete_eliminate > 0:
            print(f"Au fost eliminate {pachete_eliminate} pachete cu pretul mai mare de '{pret}'.")
        else:
            print(f"Nu a fost gasit niciun pachet care are pretul mai mare de '{pret}'.")
        return lista_actualizata
    except ValueError:
        print("Pretul trebuie sa fie un numar.")
        return lista_pachete



def ui_modifica_pachet(lista_pachete):
    """
    Interfata cu utilizatorul pentru a modifica un pachet.
    """
    print("\n--- Modificare pachet existent ---")

    # Iese din functie daca lista e goala
    if not ui_afiseaza_pachete(lista_pachete, "Selectati numarul pachetului de modificat:"):
        return

    # Cere utilizatorului sa aleaga un pachet
    try:
        numar_pachet = int(input("Introduceti numarul pachetului: "))
        index_pachet = numar_pachet - 1

        # Verifica daca indexul este valid
        if not (0 <= index_pachet < len(lista_pachete)):
            print("Eroare: Numarul pachetului nu este valid.")
            return

    except ValueError:
        print("Eroare: Trebuie sa introduceti un numar.")
        return

    # Citeste noile date
    print("\nIntroduceti noile date pentru pachet (lasati gol pentru a pastra valoarea veche).")

    # Modifica destinatia
    destinatie_noua = input(f"Destinatie noua (veche: {lista_pachete[index_pachet]['destinatie']}): ")
    if destinatie_noua == "":
        destinatie_noua = lista_pachete[index_pachet]['destinatie']

    # Modifica datele de calatorie
    while True:
        data_inceput_str = input(f"Data inceput noua (veche: {format_data_manual(lista_pachete[index_pachet]['data_inceput'])}): ")
        if data_inceput_str == "":
            data_inceput_noua = lista_pachete[index_pachet]['data_inceput']
        else:
            data_inceput_noua = converteste_string_in_data(data_inceput_str)
            if data_inceput_noua is None:
                print("Format data invalid. Modul corect este zz/ll/aaaa. Incercati din nou.")
                continue

        data_sfarsit_str = input(f"Data sfarsit noua (veche: {format_data_manual(lista_pachete[index_pachet]['data_sfarsit'])}): ")
        if data_sfarsit_str == "":
            data_sfarsit_noua = lista_pachete[index_pachet]['data_sfarsit']
        else:
            data_sfarsit_noua = converteste_string_in_data(data_sfarsit_str)
            if data_sfarsit_noua is None:
                print("Format data invalid. Modul corect este zz/ll/aaaa. Incercati din nou.")
                continue

        # Validare ca data de sfarsit sa fie dupa cea de inceput
        if data_sfarsit_noua > data_inceput_noua:
            break
        else:
            print("Data de sfarsit trebuie sa fie dupa data de inceput. Va rugam reintroduceti perioada.")

    # Modifica pretul
    while True:
        pret_nou_str = input(f"Pret nou (vechi: {lista_pachete[index_pachet]['pret']:.2f}): ")
        if pret_nou_str == "":
            pret_nou = lista_pachete[index_pachet]['pret']
            break
        try:
            pret_nou = float(pret_nou_str)
            break
        except ValueError:
            print("Pretul trebuie sa fie un numar (ex: 150.99). Incercati din nou.")

    # Apeleaza functia de modificare
    modifica_pachet(lista_pachete, index_pachet, destinatie_noua, data_inceput_noua, data_sfarsit_noua, pret_nou)
    print("Pachetul a fost modificat cu succes!")


def ui_cauta_dupa_interval(lista_pachete):
    """
    UI pentru cautarea pachetelor intr-un interval de timp.
    """
    print("\n--- Cautare pachete intr-un interval ---")
    while True:
        data_inceput = citeste_data_validata("Introduceti data de inceput a intervalului (zz/ll/aaaa): ")
        data_sfarsit = citeste_data_validata("Introduceti data de sfarsit a intervalului (zz/ll/aaaa): ")
        if data_sfarsit > data_inceput:
            break
        else:
            print("Data de sfarsit a intervalului trebuie sa fie dupa data de inceput. Reincercati.")

    rezultate = cauta_dupa_interval(lista_pachete, data_inceput, data_sfarsit)
    ui_afiseaza_pachete(rezultate, titlu=f"--- Pachete gasite in intervalul {format_data_manual(data_inceput)} - {format_data_manual(data_sfarsit)} ---")


def ui_cauta_dupa_destinatie_si_pret(lista_pachete):
    """
    UI pentru cautarea pachetelor dupa destinatie si pret maxim.
    """
    print("\n--- Cautare pachete dupa destinatie si pret ---")
    destinatie = input("Introduceti destinatia dorita: ")
    try:
        pret_maxim = float(input("Introduceti bugetul maxim: "))
        rezultate = cauta_dupa_destinatie_si_pret(lista_pachete, destinatie, pret_maxim)
        ui_afiseaza_pachete(rezultate, titlu=f"--- Pachete gasite pentru '{destinatie}' cu pret sub {pret_maxim:.2f} ---")
    except ValueError:
        print("Eroare: Pretul trebuie sa fie un numar.")


def ui_cauta_dupa_data_sfarsit(lista_pachete):
    """
    UI pentru cautarea pachetelor dupa data de sfarsit.
    """
    print("\n--- Cautare pachete dupa data de sfarsit ---")
    data_sfarsit = citeste_data_validata("Introduceti data de sfarsit exacta (zz/ll/aaaa): ")
    rezultate = cauta_dupa_data_sfarsit(lista_pachete, data_sfarsit)
    ui_afiseaza_pachete(rezultate, titlu=f"--- Pachete gasite care se termina pe {format_data_manual(data_sfarsit)} ---")

def ui_meniu():
    print("\n===============================")
    print("   MENIU AGENTIE DE TURISM   ")
    print("===============================")
    print("1. Adauga pachet nou")
    print("2. Modifica un pachet existent")
    print("3. Afiseaza toate pachetele")
    print("--- Optiuni Stergere ---")
    print("4. Sterge pachetele mai scurte decât o durata")
    print("5. Sterge pachetele cu o destinatie specifica")
    print("6. Sterge pachetele care au pretul mai mare decat o suma data")
    print("--- Optiuni Cautare ---")
    print("7. Cauta pachete intr-un interval de timp")
    print("8. Cauta pachete dupa destinatie si pret")
    print("9. Cauta pachete dupa data de sfarsit")
    print("0. Iesire din aplicatie")
