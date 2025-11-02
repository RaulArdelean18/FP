from ui.console import *

def run():
    pachete_turistice = []

    # Cream o lista care va tine minte starile anterioare (retinem o stiva cu pachetele anteriore)
    istoric_stari = []

    while True:
        ui_meniu()
        optiune = input(">>> Alegeti o optiune: ")

        # Definim ce operatii modifica lista
        operatii_cu_modificari = ['1', '2', '4', '5', '6']

        # Daca utilizatorul alege o operatie care modifica lista,
        # salvam starea CURENTA in istoric INAINTE de a o executa.
        if optiune in operatii_cu_modificari:
            istoric_stari.append(pachete_turistice)


        match optiune:
            case '1':
                pachete_turistice = ui_adauga_pachet(pachete_turistice)
            case '2':
                pachete_turistice = ui_modifica_pachet(pachete_turistice)
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
            case '13':
                ui_raport_numar_oferte(pachete_turistice)
            case '14':
                ui_raport_medie_pret(pachete_turistice)

            case '15':
                if len(istoric_stari) > 0:
                    # Scoatem ultima stare salvata in stack si o setam ca fiind starea curenta
                    pachete_turistice = istoric_stari.pop()
                    print("\nOperatia anterioara a fost anulata cu succes.")
                    ui_afiseaza_pachete(pachete_turistice, titlu="--- Lista a revenit la starea anterioara ---")
                else:
                    print("\nNu exista operatii pentru anulat.")

            case '0':
                print("Programul s-a oprit.")
                break
            case _:
                print("Optiune invalida. Va rugam alegeti din lista.")