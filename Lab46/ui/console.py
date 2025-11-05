from Lab46.data_base.services import *
from Lab46.utilitati.date_converter import *

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
    Citeste datele, apeleaza serviciul pentru adaugare si
    RETURNeaza noua lista de pachete.
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
        lista_noua = adauga_pachet(lista_pachete, destinatie, data_inceput, data_sfarsit, pret)

        print("Pachet adaugat cu succes!")
        return lista_noua

    except ValueError:
        print("Pretul trebuie sa fie un numar.")
        return lista_pachete

def ui_afiseaza_pachete(lista_pachete, titlu="--- Lista de pachete ---"):
    """
    Afiseaza toate pachetele dintr-o lista data.
    Folosesc gettere in loc de acces direct la chei.
    """
    print(f"\n{titlu}")
    if not lista_pachete:
        print("Lista este goala.")
        return False

    for i, pachet_curent in enumerate(lista_pachete):
        destinatia = get_destinatie(pachet_curent)
        perioada_start = format_data_manual(get_data_inceput(pachet_curent))
        perioada_stop = format_data_manual(get_data_sfarsit(pachet_curent))
        pretul = get_pret(pachet_curent)

        text_de_afisat = (
            f"{i + 1}. Destinație: {destinatia}, "
            f"Perioada: {perioada_start} - {perioada_stop}, "
            f"Preț: {pretul:.2f}"
        )
        print(text_de_afisat)
    return True

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
    Returneaza noua lista de pachete dupa modificare.
    """
    print("\n--- Modificare pachet existent ---")

    # Daca lista e goala, returnam lista goala (nemodificata)
    if not ui_afiseaza_pachete(lista_pachete, "Selectati numarul pachetului de modificat:"):
        return lista_pachete

    try:
        numar_pachet = int(input("Introduceti numarul pachetului: "))
        index_pachet = numar_pachet - 1

        # Verifica daca indexul este valid
        if not (0 <= index_pachet < len(lista_pachete)):
            print("Eroare: Numarul pachetului nu este valid.")
            return lista_pachete  # Returneaza lista nemodificata

    except ValueError:
        print("Eroare: Trebuie sa introduceti un numar.")
        return lista_pachete  # Returneaza lista nemodificata

    # MODIFICAT: Extragem pachetul vechi o singura data
    pachet_vechi = lista_pachete[index_pachet]

    # Citeste noile date
    print("\nIntroduceti noile date pentru pachet (lasati gol pentru a pastra valoarea veche).")

    # Modifica destinatia
    # Folosim getter
    destinatie_noua = input(f"Destinatie noua (veche: {get_destinatie(pachet_vechi)}): ")
    if destinatie_noua == "":
        destinatie_noua = get_destinatie(pachet_vechi)  # Folosim getter

    # Modifica datele de calatorie
    while True:
        # Folosim gettere
        data_inceput_str = input(f"Data inceput noua (veche: {format_data_manual(get_data_inceput(pachet_vechi))}): ")
        if data_inceput_str == "":
            data_inceput_noua = get_data_inceput(pachet_vechi)  # Folosim getter
        else:
            data_inceput_noua = converteste_string_in_data(data_inceput_str)
            if data_inceput_noua is None:
                print("Format data invalid. Modul corect este zz/ll/aaaa. Incercati din nou.")
                continue

        # Folosim gettere
        data_sfarsit_str = input(f"Data sfarsit noua (veche: {format_data_manual(get_data_sfarsit(pachet_vechi))}): ")
        if data_sfarsit_str == "":
            data_sfarsit_noua = get_data_sfarsit(pachet_vechi)  # Folosim getter
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
        # Folosim getter
        pret_nou_str = input(f"Pret nou (vechi: {get_pret(pachet_vechi):.2f}): ")
        if pret_nou_str == "":
            pret_nou = get_pret(pachet_vechi)  # Folosim getter
            break
        try:
            pret_nou = float(pret_nou_str)
            break
        except ValueError:
            print("Pretul trebuie sa fie un numar (ex: 150.99). Incercati din nou.")

    # Apeleaza functia de modificare
    # Prindem noua lista returnata de serviciu
    lista_noua = modifica_pachet(lista_pachete, index_pachet, destinatie_noua, data_inceput_noua, data_sfarsit_noua,
                                 pret_nou)

    print("Pachetul a fost modificat cu succes!")

    # Returnam noua lista catre controller
    return lista_noua

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

def ui_filtrare_oferte_dupa_pret_si_destinatie(lista_pachete):
    '''
    UI pentru filtrare oferte dupa pret si destinatie.
    Dorim sa afisam o noua lista fara a modifica lista curenta astfel incat sa avem doar pachetele cu un pret mai mare decat cel introdus de utilizator, respectiv destinatiile sa nu coincida cu destinatioa introdusa de utilizator
    :param lista_pachete: lista pachetelor actuale
    :return: lista filtrata cu datele introduse de utilizator
    '''

    print("\n--- Filtrare dupa pret si destinatie ---")
    destinatie = input("Introduceti destinatia in care nu doriti sa mergeti: ")
    try:
        pret_maxim = float(input("Introduceti bugetul maxim: "))
    except ValueError:
        print("Eroare: Pretul trebuie sa fie un numar.")

    rezultate = filtrare_oferte_dupa_pret_si_destinatie(lista_pachete, destinatie,pret_maxim)
    ui_afiseaza_pachete(rezultate,titlu=f"--- Pachetele care au un pret mai mic sau egal cu {pret_maxim} si cu o destinatie diferita fata de {destinatie} ---")


def ui_filtrare_dupa_luna(lista_pachete):
    """
    UI pentru filtrarea (afisarea) pachetelor care NU au zile intr-o anumita luna.
    NU modifica lista originala.
    """
    print("\n--- Filtrare pachete (excludere luna) ---")
    try:
        luna = int(input("Introduceti luna (1-12) pentru care doriti sa *excludeti* ofertele: "))
        if not (1 <= luna <= 12):
            print("Eroare: Luna trebuie sa fie un numar intre 1 si 12.")
            return # Iese din functie

        # Apeleaza functia de logica
        lista_filtrata = filtrare_dupa_luna(lista_pachete, luna)

        # Afiseaza direct rezultatul filtrat
        ui_afiseaza_pachete(lista_filtrata, titlu=f"--- Pachete care NU se desfasoara in luna {luna} ---")

    except ValueError:
        print("Eroare: Trebuie sa introduceti un numar intreg (1-12).")


def ui_raport_perioada_sortat(lista_pachete):
    """
    UI pentru afisarea pachetelor dintr-un interval, sortate dupa pret.
    """
    print("\n--- Raport: Pachete dintr-un interval (sortate dupa pret) ---")
    while True:
        data_inceput = citeste_data_validata("Introduceti data de inceput a intervalului (zz/ll/aaaa): ")
        data_sfarsit = citeste_data_validata("Introduceti data de sfarsit a intervalului (zz/ll/aaaa): ")
        if data_sfarsit > data_inceput:
            break
        else:
            print("Data de sfarsit a intervalului trebuie sa fie dupa data de inceput. Reincercati.")

    # Apeleaza functia de logica pentru rapoarte
    rezultate_sortate = raport_perioada_sortat_pret(lista_pachete, data_inceput, data_sfarsit)

    # Afiseaza rezultatele
    titlu = (
        f"--- Pachete in intervalul {format_data_manual(data_inceput)} - {format_data_manual(data_sfarsit)} "
        f"(sortate crescator dupa pret) ---"
    )
    ui_afiseaza_pachete(rezultate_sortate, titlu=titlu)


def ui_raport_numar_oferte(lista_pachete):
    """
    UI pentru afisarea numarului de oferte pe destinatie.
    """
    print("\n--- Raport: Numar oferte pe destinatie ---")
    destinatie = input("Introduceti destinatia: ")

    numar_oferte = raport_numar_oferte_destinatie(lista_pachete, destinatie)

    if numar_oferte == 0:
        print(f"Nu exista oferte pentru destinatia '{destinatie}'.")
    else:
        print(f"Numarul de oferte pentru destinatia '{destinatie}' este: {numar_oferte}")


def ui_raport_medie_pret(lista_pachete):
    """
    UI pentru afisarea pretului mediu pe destinatie.
    """
    print("\n--- Raport: Medie pret pe destinatie ---")
    destinatie = input("Introduceti destinatia: ")

    medie_pret = raport_medie_pret_destinatie(lista_pachete, destinatie)

    if medie_pret == 0:
        print(f"Nu exista oferte pentru destinatia '{destinatie}' pentru a calcula media.")
    else:
        print(f"Pretul mediu pentru destinatia '{destinatie}' este: {medie_pret:.2f}")

def ui_citeste_optiune(mesaj_prompt):
    """
    Citeste optiunea utilizatorului.
    """
    return input(mesaj_prompt)

def ui_mesaj_undo_succes():
    """
    Afiseaza mesajul de succes pentru operatia de Undo.
    """
    print("\nOperatia anterioara a fost anulata cu succes.")

def ui_mesaj_undo_esec():
    """
    Afiseaza mesajul de eroare cand nu se poate face Undo.
    """
    print("\nNu exista operatii pentru anulat.")

def ui_mesaj_oprire():
    """
    Afiseaza mesajul de iesire din program.
    """
    print("Programul s-a oprit.")

def ui_mesaj_optiune_invalida():
    """
    Afiseaza mesajul pentru optiune invalida.
    """
    print("Optiune invalida. Va rugam alegeti din lista.")

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
    print("--- Optiuni Filtrare ---")
    print("10. Filtrare dupa pret si destinatie")
    print("11. Filtrare pachete dintr-o luna")
    print("--- Optiuni Rapoarte ---")
    print("12. Raport: Pachete pe perioada (sortate dupa pret)")
    print("13. Raport: Numar oferte pe destinatie")
    print("14. Raport: Medie pret pe destinatie")
    print("--- Optiune de Undo ---")
    print("15. Undo (anuleaza ultima modificare)")
    print("0. Iesire din aplicatie")