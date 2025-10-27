from data_base.services import *
from utilitati.date_converter import converteste_string_in_data


# --- O functie ajutatoare pentru a crea datele de test ---
def setup_date_pachete():
    """Creeaza un set de pachete si date pentru teste."""

    # Datele
    d_01_01 = converteste_string_in_data("01/01/2025")
    d_05_01 = converteste_string_in_data("05/01/2025")
    d_10_01 = converteste_string_in_data("10/01/2025")
    d_15_01 = converteste_string_in_data("15/01/2025")

    p1 = creeaza_pachet("Grecia", d_01_01, d_05_01, 100.0)
    p2 = creeaza_pachet("Italia", d_01_01, d_10_01, 200.0)
    p3 = creeaza_pachet("Grecia", d_05_01, d_15_01, 150.0)

    # Lista initiala
    lista_pachete = [p1, p2, p3]

    return lista_pachete, d_01_01, d_05_01, d_10_01, d_15_01


# --- Teste pentru Gettere si Creare (Nou) ---
# Aceasta inlocuieste functia ta 'verify()'
def test_gettere_si_creare_pachet():
    # 1. Testam creatorul de pachet
    d_start = converteste_string_in_data("01/01/2025")
    d_end = converteste_string_in_data("05/01/2025")

    pachet_test = creeaza_pachet("Testonia", d_start, d_end, 99.5)

    # 2. Testam noile gettere pe pachetul creat
    assert get_destinatie(pachet_test) == "Testonia"
    assert get_pret(pachet_test) == 99.5
    assert get_data_inceput(pachet_test) == d_start
    assert get_data_sfarsit(pachet_test) == d_end


# --- Teste pentru Servicii ---

def test_adauga_pachet():
    lista_test = []
    d_start = converteste_string_in_data("01/01/2025")
    d_end = converteste_string_in_data("05/01/2025")

    adauga_pachet(lista_test, "Spania", d_start, d_end, 500)

    assert len(lista_test) == 1
    assert get_destinatie(lista_test[0]) == "Spania"
    assert get_pret(lista_test[0]) == 500.0

    adauga_pachet(lista_test, "Turcia", d_start, d_end, 300)
    assert len(lista_test) == 2
    assert get_destinatie(lista_test[1]) == "Turcia"


def test_modifica_pachet():
    lista_test, d_01_01, d_05_01, _, _ = setup_date_pachete()

    d_new_start = converteste_string_in_data("02/01/2025")
    d_new_end = converteste_string_in_data("06/01/2025")

    modifica_pachet(lista_test, 0, "Spania", d_new_start, d_new_end, 999.0)

    assert len(lista_test) == 3
    assert get_destinatie(lista_test[0]) == "Spania"
    assert get_pret(lista_test[0]) == 999.0
    assert get_data_inceput(lista_test[0]) == d_new_start

    # Verificam ca pachetul 2 (index 1) nu a fost afectat
    assert get_destinatie(lista_test[1]) == "Italia"


def test_sterge_dupa_durata():
    lista_test, _, _, _, _ = setup_date_pachete()

    rezultat = sterge_dupa_durata(lista_test, 5)
    assert len(rezultat) == 2
    assert get_destinatie(rezultat[0]) == "Italia"  # p2
    assert get_destinatie(rezultat[1]) == "Grecia"  # p3

    rezultat_2 = sterge_dupa_durata(lista_test, 10)
    assert len(rezultat_2) == 1
    assert get_destinatie(rezultat_2[0]) == "Grecia"  # p3

    assert len(lista_test) == 3


def test_sterge_dupa_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()

    rezultat = sterge_dupa_destinatie(lista_test, "Grecia")
    assert len(rezultat) == 1
    assert get_destinatie(rezultat[0]) == "Italia"

    rezultat_2 = sterge_dupa_destinatie(lista_test, "Spania")
    assert len(rezultat_2) == 3
    assert len(lista_test) == 3


def test_sterge_dupa_pret():
    lista_test, _, _, _, _ = setup_date_pachete()

    rezultat = sterge_dupa_pret(lista_test, 160)
    assert len(rezultat) == 2
    assert get_pret(rezultat[0]) == 100.0  # p1
    assert get_pret(rezultat[1]) == 150.0  # p3

    assert len(lista_test) == 3


def test_cauta_dupa_interval():
    lista_test, d_01_01, d_05_01, d_10_01, d_15_01 = setup_date_pachete()

    rezultat = cauta_dupa_interval(lista_test, d_01_01, d_15_01)
    assert len(rezultat) == 3

    rezultat_2 = cauta_dupa_interval(lista_test, d_01_01, d_05_01)
    assert len(rezultat_2) == 1
    assert get_destinatie(rezultat_2[0]) == "Grecia"
    assert get_pret(rezultat_2[0]) == 100.0

    rezultat_3 = cauta_dupa_interval(lista_test, d_05_01, d_10_01)
    assert len(rezultat_3) == 0


def test_cauta_dupa_destinatie_si_pret():
    lista_test, _, _, _, _ = setup_date_pachete()

    rezultat = cauta_dupa_destinatie_si_pret(lista_test, "Grecia", 160)
    assert len(rezultat) == 2

    rezultat_2 = cauta_dupa_destinatie_si_pret(lista_test, "Grecia", 120)
    assert len(rezultat_2) == 1
    assert get_pret(rezultat_2[0]) == 100.0

    rezultat_3 = cauta_dupa_destinatie_si_pret(lista_test, "Italia", 100)
    assert len(rezultat_3) == 0


def test_cauta_dupa_data_sfarsit():
    lista_test, _, d_05_01, d_10_01, d_15_01 = setup_date_pachete()

    rezultat = cauta_dupa_data_sfarsit(lista_test, d_10_01)
    assert len(rezultat) == 1
    assert get_destinatie(rezultat[0]) == "Italia"

    rezultat_2 = cauta_dupa_data_sfarsit(lista_test, d_05_01)
    assert len(rezultat_2) == 1
    assert get_pret(rezultat_2[0]) == 100.0


def test_filtrare_oferte_dupa_pret_si_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()

    rezultat = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Grecia", 250)
    assert len(rezultat) == 1
    assert get_destinatie(rezultat[0]) == "Italia"

    rezultat_2 = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Spania", 160)
    assert len(rezultat_2) == 2


def test_filtrare_dupa_luna():
    p1 = creeaza_pachet("A", converteste_string_in_data("15/01/2025"), converteste_string_in_data("25/01/2025"), 100)
    p2 = creeaza_pachet("B", converteste_string_in_data("15/02/2025"), converteste_string_in_data("05/03/2025"), 200)
    p3 = creeaza_pachet("C", converteste_string_in_data("10/04/2025"), converteste_string_in_data("20/04/2025"), 300)
    p4 = creeaza_pachet("D", converteste_string_in_data("15/12/2024"), converteste_string_in_data("10/01/2025"), 400)

    lista_test = [p1, p2, p3, p4]

    rezultat_ian = filtrare_dupa_luna(lista_test, 1)
    assert len(rezultat_ian) == 2
    assert get_destinatie(rezultat_ian[0]) == "B"
    assert get_destinatie(rezultat_ian[1]) == "C"

    rezultat_mar = filtrare_dupa_luna(lista_test, 3)
    assert len(rezultat_mar) == 3
    assert get_destinatie(rezultat_mar[0]) == "A"
    assert get_destinatie(rezultat_mar[1]) == "C"
    assert get_destinatie(rezultat_mar[2]) == "D"

    assert len(lista_test) == 4


def test_raport_perioada_sortat_pret():
    data_1 = converteste_string_in_data("01/01/2025")
    data_5 = converteste_string_in_data("05/01/2025")
    data_10 = converteste_string_in_data("10/01/2025")
    data_15 = converteste_string_in_data("15/01/2025")

    # MODIFICAT: Folosim 'creeaza_pachet'
    p1 = creeaza_pachet("A", data_1, data_5, 200)
    p2 = creeaza_pachet("B", data_5, data_10, 100)
    p3 = creeaza_pachet("C", data_10, data_15, 50)
    p4 = creeaza_pachet("D", data_1, data_10, 300)

    lista_test = [p1, p2, p3, p4]

    data_start_cautare = data_1
    data_end_cautare = data_10

    rezultat_sortat = raport_perioada_sortat_pret(lista_test, data_start_cautare, data_end_cautare)

    assert len(rezultat_sortat) == 3

    # MODIFICAT: Folosim gettere
    assert get_pret(rezultat_sortat[0]) == 100  # p2
    assert get_pret(rezultat_sortat[1]) == 200  # p1
    assert get_pret(rezultat_sortat[2]) == 300  # p4

    assert get_destinatie(rezultat_sortat[0]) == "B"
    assert get_destinatie(rezultat_sortat[1]) == "A"
    assert get_destinatie(rezultat_sortat[2]) == "D"


    # Test caz fara rezultate
    data_start_cautare_noua = converteste_string_in_data("01/06/2025")
    data_end_cautare_noua = converteste_string_in_data("10/06/2025")
    rezultat_gol = raport_perioada_sortat_pret(lista_test, data_start_cautare_noua, data_end_cautare_noua)
    assert len(rezultat_gol) == 0