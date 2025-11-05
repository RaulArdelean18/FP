from Lab46.app.pachete_manager import *
from Lab46.data_base.services import *
from Lab46.utilitati.date_converter import *
from Lab46.ui.console import ui_afiseaza_pachete, ui_mesaj_undo_succes, ui_mesaj_undo_esec


def _valideaza_si_converteste_pachet(params):
    if len(params) != 4:
        raise ValueError("Comanda 'add' necesita 4 parametri: destinatie, data_start, data_sf, pret")
    destinatie = params[0]
    data_inceput = converteste_string_in_data(params[1])
    data_sfarsit = converteste_string_in_data(params[2])
    if data_inceput is None or data_sfarsit is None:
        raise ValueError(f"Format data invalid pentru '{params[1]}' sau '{params[2]}'. Folositi zz/ll/aaaa.")
    if data_sfarsit <= data_inceput:
        raise ValueError("Data de sfarsit trebuie sa fie dupa data de inceput.")
    try:
        pret = float(params[3])
    except ValueError:
        raise ValueError(f"Pretul '{params[3]}' trebuie sa fie un numar.")
    return destinatie, data_inceput, data_sfarsit, pret


def _valideaza_date_interval(params):
    if len(params) != 2:
        raise ValueError("Comanda necesita 2 parametri: data_start si data_sfarsit (zz/ll/aaaa).")
    data_start = converteste_string_in_data(params[0])
    data_sfarsit = converteste_string_in_data(params[1])
    if data_start is None or data_sfarsit is None:
        raise ValueError(f"Format data invalid pentru '{params[0]}' sau '{params[1]}'.")
    if data_sfarsit <= data_start:
        raise ValueError("Data de sfarsit trebuie sa fie dupa data de inceput.")
    return data_start, data_sfarsit


#
# --- LEGENDA ---
#
def _afiseaza_legenda_parsing():
    """
    Afiseaza legenda completa a comenzilor parsing.
    """
    print("\n--- Legenda Comenzi Parsing ---")
    print("Sintaxa: comanda [param1] [param2] ...")
    print("Puteti introduce mai multe comenzi pe o linie, separate prin ';'")

    print("\n  [ Gestiune & Vizualizare ]")
    print("  add [dest] [start_date] [end_date] [pret]")
    print("      Ex: add Paris 10/12/2025 15/12/2025 500")
    print("  print")
    print("      (Afiseaza toate pachetele curente)")

    print("\n  [ Stergere ] (Operatiuni cu Undo)")
    print("  sterge_destinatie [dest]")
    print("  sterge_durata [zile_min_pastrat]")
    print("  sterge_pret [pret_max_pastrat]")

    print("\n  [ Cautare ] (Doar afiseaza, fara Undo)")
    print("  cauta_interval [start_date] [end_date]")
    print("  cauta_dest_pret [dest] [pret_max]")
    print("  cauta_data_sf [end_date]")

    print("\n  [ Filtrare ] (Doar afiseaza, fara Undo)")
    print("  filtrare_pret_dest [dest_exclusa] [pret_max]")
    print("  filtrare_luna [luna_exclusa]")

    print("\n  [ Rapoarte ] (Doar afiseaza, fara Undo)")
    print("  raport_sortat [start_date] [end_date]")
    print("  raport_numar [dest]")
    print("  raport_medie [dest]")

    print("\n  [ Utilitare ]")
    print("  undo    (Anuleaza ultima operatie de Adaugare/Stergere)")
    print("  help    (Afiseaza aceasta legenda)")
    print("  exit    (Opreste modul parsing)")
    print("-------------------------------------------\n")


#
# --- RUN Parsing ---
#
def run_parsing():
    """
    Ruleaza aplicatia in mod 'parsing', citind comenzi una cate una intr-o bucla.
    """
    manager = creeaza_manager_stare()

    print("--- Mod Comanda (parsing) ---")
    print("Tastati 'help' pentru legenda sau 'exit' pentru a iesi.")
    print("Puteti introduce mai multe comenzi pe o linie, separate prin ';'")

    while True:
        # 1. Citeste intreaga linie de la utilizator
        linie_intreaga = input("Parsing> ")
        linie_intreaga = linie_intreaga.strip()

        if not linie_intreaga:
            continue

        # 2. Imparte linia in comenzi individuale folosind ';'
        comenzi_de_pe_linie = linie_intreaga.split(';')

        # 3. Executa fiecare comanda, pe rand
        for comanda_bruta in comenzi_de_pe_linie:
            comanda_bruta = comanda_bruta.strip()  # Curata spatiile din jur

            if not comanda_bruta:  # Ignora segmentele goale (ex: cmd1 ; ; cmd2)
                continue

            parti = comanda_bruta.split()
            cmd = parti[0].lower().strip()
            params = parti[1:]

            try:
                # Comenzi de control
                if cmd == 'exit' or cmd == '0':
                    print("Iesire din modul parsing...")
                    return  # Iese complet din functie (opreste bucla while)

                if cmd == 'help':
                    _afiseaza_legenda_parsing()
                    continue  # Continua cu urmatoarea comanda din 'for'

                # Salvam starea inainte de operatiile care modifica
                operatii_cu_modificari = ['add', 'sterge_durata', 'sterge_destinatie', 'sterge_pret']
                if cmd in operatii_cu_modificari:
                    stare_curenta = get_lista_curenta(manager)
                    adauga_la_undo(manager, stare_curenta.copy())

                # add si print
                if cmd == 'add':
                    dest, data_start, data_sfarsit, pret = _valideaza_si_converteste_pachet(params)
                    lista_noua = adauga_pachet(get_lista_curenta(manager), dest, data_start, data_sfarsit, pret)
                    set_lista_curenta(manager, lista_noua)
                    print(f"[*] OK: Pachet adaugat: {dest}")
                elif cmd == 'print':
                    ui_afiseaza_pachete(get_lista_curenta(manager))

                # Stergeri
                elif cmd == 'sterge_destinatie':
                    if len(params) != 1: raise ValueError(
                        "Comanda 'sterge_destinatie' necesita 1 parametru (destinatia).")
                    lista_noua = sterge_dupa_destinatie(get_lista_curenta(manager), params[0])
                    set_lista_curenta(manager, lista_noua)
                    print(f"[*] OK: Pachete sterse pentru: {params[0]}")
                elif cmd == 'sterge_durata':
                    if len(params) != 1: raise ValueError("Comanda 'sterge_durata' necesita 1 parametru (numar zile).")
                    durata = int(params[0])
                    lista_noua = sterge_dupa_durata(get_lista_curenta(manager), durata)
                    set_lista_curenta(manager, lista_noua)
                    print(f"[*] OK: Pachete sterse (durata < {durata} zile)")
                elif cmd == 'sterge_pret':
                    if len(params) != 1: raise ValueError(
                        "Comanda 'sterge_pret' necesita 1 parametru (pretul maxim de pastrat).")
                    pret = float(params[0])
                    lista_noua = sterge_dupa_pret(get_lista_curenta(manager), pret)
                    set_lista_curenta(manager, lista_noua)
                    print(f"[*] OK: Pachete sterse (pret > {pret})")

                # Cautari
                elif cmd == 'cauta_interval':
                    data_start, data_sfarsit = _valideaza_date_interval(params)
                    rezultat = cauta_dupa_interval(get_lista_curenta(manager), data_start, data_sfarsit)
                    ui_afiseaza_pachete(rezultat, titlu=f"--- Rezultate Cautare Interval ---")
                elif cmd == 'cauta_dest_pret':
                    if len(params) != 2: raise ValueError(
                        "Comanda 'cauta_dest_pret' necesita 2 parametri (destinatie, pret_max).")
                    pret = float(params[1])
                    rezultat = cauta_dupa_destinatie_si_pret(get_lista_curenta(manager), params[0], pret)
                    ui_afiseaza_pachete(rezultat, titlu=f"--- Rezultate Cautare Dest/Pret ---")
                elif cmd == 'cauta_data_sf':
                    if len(params) != 1:
                        raise ValueError("Comanda 'cauta_data_sf' necesita 1 parametru (data_sfarsit).")
                    data_sfarsit = converteste_string_in_data(params[0])
                    if data_sfarsit is None:
                        raise ValueError(f"Format data invalid: {params[0]}")
                    rezultat = cauta_dupa_data_sfarsit(get_lista_curenta(manager), data_sfarsit)
                    ui_afiseaza_pachete(rezultat, titlu=f"--- Rezultate Cautare Data Sfarsit ---")

                # Filtrari
                elif cmd == 'filtrare_pret_dest':
                    if len(params) != 2: raise ValueError(
                        "Comanda 'filtrare_pret_dest' necesita 2 parametri (dest_exclusa, pret_max).")
                    pret = float(params[1])
                    rezultat = filtrare_oferte_dupa_pret_si_destinatie(get_lista_curenta(manager), params[0], pret)
                    ui_afiseaza_pachete(rezultat, titlu=f"--- Rezultate Filtrare Pret/Dest ---")
                elif cmd == 'filtrare_luna':
                    if len(params) != 1:
                        raise ValueError("Comanda 'filtrare_luna' necesita 1 parametru (luna).")
                    luna = int(params[0])
                    if not (1 <= luna <= 12):
                        raise ValueError("Luna trebuie sa fie intre 1 si 12.")
                    rezultat = filtrare_dupa_luna(get_lista_curenta(manager), luna)
                    ui_afiseaza_pachete(rezultat, titlu=f"--- Rezultate Filtrare Luna {luna} (Exclusa) ---")

                # Rapoarte
                elif cmd == 'raport_sortat':
                    data_start, data_sfarsit = _valideaza_date_interval(params)
                    rezultat = raport_perioada_sortat_pret(get_lista_curenta(manager), data_start, data_sfarsit)
                    ui_afiseaza_pachete(rezultat, titlu=f"--- Raport Sortat Dupa Pret ---")
                elif cmd == 'raport_numar':
                    if len(params) != 1: raise ValueError("Comanda 'raport_numar' necesita 1 parametru (destinatia).")
                    numar = raport_numar_oferte_destinatie(get_lista_curenta(manager), params[0])
                    print(f"[*] Raport Numar Oferte pentru '{params[0]}': {numar}")
                elif cmd == 'raport_medie':
                    if len(params) != 1:
                        raise ValueError("Comanda 'raport_medie' necesita 1 parametru (destinatia).")
                    medie = raport_medie_pret_destinatie(get_lista_curenta(manager), params[0])
                    if medie == 0:
                        print(f"[*] Raport Medie Pret pentru '{params[0]}': Nu exista date.")
                    else:
                        print(f"[*] Raport Medie Pret pentru '{params[0]}': {medie:.2f}")

                # Undo
                elif cmd == 'undo':
                    if executa_undo(manager):
                        ui_mesaj_undo_succes()
                    else:
                        ui_mesaj_undo_esec()

                else:
                    raise ValueError(f"Comanda necunoscuta: '{cmd}'")

            except (ValueError, IndexError, TypeError) as e:
                print(f"\n[EROARE] La comanda: '{comanda_bruta}'")
                print(f"  -> {e}")
                print("Comanda nu a putut fi executata. Restul comenzilor de pe linie au fost anulate.")
                _afiseaza_legenda_parsing()
                break  # Opreste procesarea restului comenzilor de pe linie
