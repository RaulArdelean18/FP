from datetime import datetime


def converteste_string_in_data(data_str):
    """Converteste un string 'zi/luna/an' intr-un obiect datetime."""
    try:
        parti = data_str.split('/')
        zi = int(parti[0])
        luna = int(parti[1])
        an = int(parti[2])
        return datetime(an, luna, zi)
    except (ValueError, IndexError):
        return None


def format_data_manual(data_obiect):
    """Modifica obiect datetime intr-un string 'zi/luna/an'."""
    return f"{data_obiect.day}/{data_obiect.month}/{data_obiect.year}"


def adauga_pachet(lista_pachete, destinatie, data_inceput, data_sfarsit, pret):
    """Adauga un pachet nou in lista."""
    pachet = {
        "destinatie": destinatie,
        "data_inceput": data_inceput,
        "data_sfarsit": data_sfarsit,
        "pret": float(pret)
    }
    lista_pachete.append(pachet)


def sterge_dupa_durata(lista_pachete, durata_minima_zile):
    """
    Returneaza o lista noua eliminand pachetele mai scurte de un numar de zile.
    """
    pachete_pastrate = []

    for pachet in lista_pachete:
        durata_sejur = (pachet['data_sfarsit'] - pachet['data_inceput']).days
        if durata_sejur >= durata_minima_zile:
            pachete_pastrate.append(pachet)

    return pachete_pastrate

def citeste_data_validata(mesaj_prompt):
    data_obj = None
    while data_obj is None:
        data_str = input(mesaj_prompt)
        data_obj = converteste_string_in_data(data_str)
        if data_obj is None:
            print("Format data invalid.")
    return data_obj


def ui_adauga_pachet(lista_pachete):
    """Citeste datele de la utilizator și adaugă un pachet nou, cu validare completa."""
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
    """Afiseaza toate pachetele dintr-o lista data."""
    print(f"\n{titlu}")
    if not lista_pachete:
        print("Lista este goala.")
        return

    numar_pachet = 1

    for pachet_curent in lista_pachete:
        destinatia = pachet_curent['destinatie']
        perioada_start = format_data_manual(pachet_curent['data_inceput'])
        perioada_stop = format_data_manual(pachet_curent['data_sfarsit'])
        pretul = pachet_curent['pret']

        text_de_afisat = (
            f"{numar_pachet}. Destinație: {destinatia}, "
            f"Perioada: {perioada_start} - {perioada_stop}, "
            f"Preț: {pretul:.2f}"
        )
        print(text_de_afisat)

        numar_pachet += 1

def ui_sterge_dupa_durata(lista_pachete):
    """Citeste durata si actualizeaza lista principala."""
    try:
        durata = int(input("Introduceti durata minima a pachetelor de pastrat (zile): "))
        lista_actualizata = sterge_dupa_durata(lista_pachete, durata)
        print(f"Au fost eliminate {len(lista_pachete) - len(lista_actualizata)} pachete.")
        return lista_actualizata
    except ValueError:
        print("Durata trebuie sa fie un numar intreg.")
        return lista_pachete


def ui_meniu():
    print("\n===============================")
    print("   MENIU AGENTIE DE TURISM   ")
    print("===============================")
    print("1. Adauga pachet nou")
    print("2. Afiseaza toate pachetele")
    print("3. Sterge pachetele mai scurte decât o durata")
    print("0. Iesire din aplicatie")


pachete_turistice = []

while True:
    ui_meniu()
    optiune = input(">>> Alegeti o optiune: ")

    match optiune:
        case '1':
            ui_adauga_pachet(pachete_turistice)
        case '2':
            ui_afiseaza_pachete(pachete_turistice)
        case '3':
            pachete_turistice = ui_sterge_dupa_durata(pachete_turistice)
            ui_afiseaza_pachete(pachete_turistice, titlu="--- Lista actualizata de pachete ---")
        case '0':
            print("Programul s-a oprit.")
            break
        case _:
            print("Optiune invalida. Va rugam alegeti din lista.")