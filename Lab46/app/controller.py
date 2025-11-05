from Lab46.ui.console import *
from Lab46.app.pachete_manager import *

def run():
    pachete_turistice = []
    manager_stare = creeaza_manager_stare()

    while True:
        ui_meniu()
        optiune = input(">>> Alegeti o optiune: ")

        # Definim ce operatii modifica lista
        operatii_cu_modificari = ['1', '2', '4', '5', '6']

        # Daca utilizatorul alege o operatie care modifica lista,
        # salvam starea CURENTA in istoric INAINTE de a o executa.
        if optiune in operatii_cu_modificari:
            # Preluam starea curenta din manager
            lista_de_salvat = get_lista_curenta(manager_stare)
            # Adaugam o copie a ei in lista de undo
            adauga_la_undo(manager_stare, lista_de_salvat.copy())

        match optiune:
            case '1':
                # Extragem starea curenta, o trimitem la UI, primim starea noua
                lista_curenta = get_lista_curenta(manager_stare)
                lista_noua = ui_adauga_pachet(lista_curenta)
                # Setam noua stare in manager
                set_lista_curenta(manager_stare, lista_noua)

            case '2':
                lista_curenta = get_lista_curenta(manager_stare)
                lista_noua = ui_modifica_pachet(lista_curenta)
                set_lista_curenta(manager_stare, lista_noua)

            case '3':
                # Pentru afisare, doar citim starea curenta
                ui_afiseaza_pachete(get_lista_curenta(manager_stare))

            case '4':
                lista_curenta = get_lista_curenta(manager_stare)
                lista_noua = ui_sterge_dupa_durata(lista_curenta)
                set_lista_curenta(manager_stare, lista_noua)

                ui_afiseaza_pachete(get_lista_curenta(manager_stare), titlu="--- Lista actualizata de pachete ---")

            case '5':
                lista_curenta = get_lista_curenta(manager_stare)
                lista_noua = ui_sterge_dupa_destinatie(lista_curenta)
                set_lista_curenta(manager_stare, lista_noua)

                ui_afiseaza_pachete(get_lista_curenta(manager_stare), titlu="--- Lista actualizata de pachete ---")

            case '6':
                lista_curenta = get_lista_curenta(manager_stare)
                lista_noua = ui_sterge_dupa_pret(lista_curenta)
                set_lista_curenta(manager_stare, lista_noua)

                ui_afiseaza_pachete(get_lista_curenta(manager_stare), titlu="--- Lista actualizata de pachete ---")

            # --- Cautarile si Rapoartele ---
            case '7':
                ui_cauta_dupa_interval(get_lista_curenta(manager_stare))
            case '8':
                ui_cauta_dupa_destinatie_si_pret(get_lista_curenta(manager_stare))
            case '9':
                ui_cauta_dupa_data_sfarsit(get_lista_curenta(manager_stare))
            case '10':
                ui_filtrare_oferte_dupa_pret_si_destinatie(get_lista_curenta(manager_stare))
            case '11':
                ui_filtrare_dupa_luna(get_lista_curenta(manager_stare))
            case '12':
                ui_raport_perioada_sortat(get_lista_curenta(manager_stare))
            case '13':
                ui_raport_numar_oferte(get_lista_curenta(manager_stare))
            case '14':
                ui_raport_medie_pret(get_lista_curenta(manager_stare))

            # --- Undo ---
            case '15':
                # Verificam folosind functia managerului
                if are_stari_undo(manager_stare):
                    # Scoatem ultima stare salvata si o setam ca fiind starea curenta
                    lista_anterioara = pop_din_undo(manager_stare)
                    set_lista_curenta(manager_stare, lista_anterioara)

                    ui_mesaj_undo_succes()
                    ui_afiseaza_pachete(get_lista_curenta(manager_stare),
                                        titlu="--- Lista a revenit la starea anterioara ---")
                else:
                    ui_mesaj_undo_esec()

            case '0':
                ui_mesaj_oprire()
                break
            case _:
                ui_mesaj_optiune_invalida()