from data_base.services import *
from utilitati.date_converter import converteste_string_in_data


# --- O functie ajutatoare pentru a crea datele de test ---
def setup_date_pachete():
    """Creeaza un set de pachete si date pentru teste."""

    # Datele
    d_01_01 = converteste_string_in_data("01/01/2025")
    d_05_01 = converteste_string_in_data("05/01/2025")  # Durata 4 zile
    d_10_01 = converteste_string_in_data("10/01/2025")  # Durata 9 zile
    d_15_01 = converteste_string_in_data("15/01/2025")  # Durata 14 zile

    # Pachetele (liste)
    p1 = {"destinatie": "Grecia", "data_inceput": d_01_01, "data_sfarsit": d_05_01, "pret": 100.0}
    p2 = {"destinatie": "Italia", "data_inceput": d_01_01, "data_sfarsit": d_10_01, "pret": 200.0}
    p3 = {"destinatie": "Grecia", "data_inceput": d_05_01, "data_sfarsit": d_15_01, "pret": 150.0}

    # Lista initiala
    lista_pachete = [p1, p2, p3]

    return lista_pachete, d_01_01, d_05_01, d_10_01, d_15_01


def test_adauga_pachet():
    lista_test = []
    d_start = converteste_string_in_data("01/01/2025")
    d_end = converteste_string_in_data("05/01/2025")

    adauga_pachet(lista_test, "Spania", d_start, d_end, 500)

    assert len(lista_test) == 1
    assert lista_test[0]["destinatie"] == "Spania"
    assert lista_test[0]["pret"] == 500.0

    adauga_pachet(lista_test, "Turcia", d_start, d_end, 300)
    assert len(lista_test) == 2
    assert lista_test[1]["destinatie"] == "Turcia"


def test_modifica_pachet():
    lista_test, d_01_01, d_05_01, _, _ = setup_date_pachete() #penultima si ultima data nu se iau in considerare

    d_new_start = converteste_string_in_data("02/01/2025")
    d_new_end = converteste_string_in_data("06/01/2025")

    # Modificam primul pachet (index 0)
    modifica_pachet(lista_test, 0, "Spania", d_new_start, d_new_end, 999.0)

    assert len(lista_test) == 3  # Numarul de pachete nu se schimba
    assert lista_test[0]["destinatie"] == "Spania"
    assert lista_test[0]["pret"] == 999.0
    assert lista_test[0]["data_inceput"] == d_new_start

    # Verificam ca pachetul 2 (index 1) nu a fost afectat
    assert lista_test[1]["destinatie"] == "Italia"


def verify():
    lista_test, _, _, _, _ = setup_date_pachete()

    # Test pe pachetul 0 (Grecia, 100, 01/01, 05/01)
    assert pachet_destinatie_pe_pozitie(lista_test, 0) == "Grecia"
    assert pachet_pret_pe_pozitie(lista_test, 0) == 100.0

    # Test pe pachetul 1 (Italia, 200, 01/01, 10/01)
    assert pachet_destinatie_pe_pozitie(lista_test, 1) == "Italia"
    assert pachet_pret_pe_pozitie(lista_test, 1) == 200.0
    assert pachet_inceput_sejur_pe_pozitie(lista_test, 1) == converteste_string_in_data("01/01/2025")
    assert pachet_final_sejur_pe_pozitie(lista_test, 1) == converteste_string_in_data("10/01/2025")


# --- Teste pentru Stergeri ---

def test_sterge_dupa_durata():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: 4 zile (05 - 01)
    # p2: 9 zile (10 - 01)
    # p3: 10 zile (15 - 05)

    # Pastram pachetele >= 5 zile (ar trebui sa stearga p1)
    rezultat = sterge_dupa_durata(lista_test, 5)
    assert len(rezultat) == 2
    assert rezultat[0]["destinatie"] == "Italia"  # p2
    assert rezultat[1]["destinatie"] == "Grecia"  # p3

    # Pastram pachetele >= 10 zile (ar trebui sa stearga p1, p2)
    rezultat_2 = sterge_dupa_durata(lista_test, 10)
    assert len(rezultat_2) == 1
    assert rezultat_2[0]["destinatie"] == "Grecia"  # p3

    # Pastram pachetele >= 100 zile (ar trebui sa stearga tot)
    rezultat_3 = sterge_dupa_durata(lista_test, 100)
    assert len(rezultat_3) == 0

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 3


def test_sterge_dupa_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, p2: Italia, p3: Grecia

    # Stergem "Grecia" (ar trebui sa ramana p2)
    rezultat = sterge_dupa_destinatie(lista_test, "Grecia")
    assert len(rezultat) == 1
    assert rezultat[0]["destinatie"] == "Italia"

    # Stergem "Spania" (nu exista, nu sterge nimic)
    rezultat_2 = sterge_dupa_destinatie(lista_test, "Spania")
    assert len(rezultat_2) == 3

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 3


def test_sterge_dupa_pret():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: 100, p2: 200, p3: 150

    # Pastram pachetele <= 160 (ar trebui sa stearga p2)
    rezultat = sterge_dupa_pret(lista_test, 160)
    assert len(rezultat) == 2
    assert rezultat[0]["pret"] == 100.0  # p1
    assert rezultat[1]["pret"] == 150.0  # p3

    # Pastram pachetele <= 99 (ar trebui sa stearga tot)
    rezultat_2 = sterge_dupa_pret(lista_test, 99)
    assert len(rezultat_2) == 0

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 3


# --- Teste pentru Cautari ---

def test_cauta_dupa_interval():
    lista_test, d_01_01, d_05_01, d_10_01, d_15_01 = setup_date_pachete()
    # p1: 01/01 - 05/01
    # p2: 01/01 - 10/01
    # p3: 05/01 - 15/01

    # Cautam intervalul [01/01, 15/01] (ar trebui sa le gaseasca pe toate)
    rezultat = cauta_dupa_interval(lista_test, d_01_01, d_15_01)
    assert len(rezultat) == 3

    # Cautam intervalul [01/01, 05/01] (ar trebui sa gaseasca p1)
    rezultat_2 = cauta_dupa_interval(lista_test, d_01_01, d_05_01)
    assert len(rezultat_2) == 1
    assert rezultat_2[0]["destinatie"] == "Grecia"
    assert rezultat_2[0]["pret"] == 100.0

    # Cautam intervalul [05/01, 10/01] (nu gaseste niciunul, p3 depaseste)
    rezultat_3 = cauta_dupa_interval(lista_test, d_05_01, d_10_01)
    assert len(rezultat_3) == 0


def test_cauta_dupa_destinatie_si_pret():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, 100
    # p2: Italia, 200
    # p3: Grecia, 150

    # Cautam "Grecia" si pret <= 160 (ar trebui sa gaseasca p1 si p3)
    rezultat = cauta_dupa_destinatie_si_pret(lista_test, "Grecia", 160)
    assert len(rezultat) == 2

    # Cautam "Grecia" si pret <= 120 (ar trebui sa gaseasca p1)
    rezultat_2 = cauta_dupa_destinatie_si_pret(lista_test, "Grecia", 120)
    assert len(rezultat_2) == 1
    assert rezultat_2[0]["pret"] == 100.0

    # Cautam "Italia" si pret <= 100 (nu gaseste nimic)
    rezultat_3 = cauta_dupa_destinatie_si_pret(lista_test, "Italia", 100)
    assert len(rezultat_3) == 0


def test_cauta_dupa_data_sfarsit():
    lista_test, _, d_05_01, d_10_01, d_15_01 = setup_date_pachete()
    # p1: sfarsit 05/01
    # p2: sfarsit 10/01
    # p3: sfarsit 15/01

    # Cautam sfarsit pe 10/01 (ar trebui sa gaseasca p2)
    rezultat = cauta_dupa_data_sfarsit(lista_test, d_10_01)
    assert len(rezultat) == 1
    assert rezultat[0]["destinatie"] == "Italia"

    # Cautam sfarsit pe 05/01 (ar trebui sa gaseasca p1)
    rezultat_2 = cauta_dupa_data_sfarsit(lista_test, d_05_01)
    assert len(rezultat_2) == 1
    assert rezultat_2[0]["pret"] == 100.0

    # Cautam sfarsit pe 06/01 (nu gaseste nimic)
    d_06_01 = converteste_string_in_data("06/01/2025")
    rezultat_3 = cauta_dupa_data_sfarsit(lista_test, d_06_01)
    assert len(rezultat_3) == 0


# --- Teste pentru Filtrare ---

def test_filtrare_oferte_dupa_pret_si_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, 100
    # p2: Italia, 200
    # p3: Grecia, 150

    # Filtram: destinatie != "Grecia" SI pret <= 250 (ar trebui sa gaseasca p2)
    rezultat = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Grecia", 250)
    assert len(rezultat) == 1
    assert rezultat[0]["destinatie"] == "Italia"

    # Filtram: destinatie != "Spania" SI pret <= 160 (ar trebui sa gaseasca p1, p3)
    rezultat_2 = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Spania", 160)
    assert len(rezultat_2) == 2

    # Filtram: destinatie != "Grecia" SI pret <= 100 (nu gaseste nimic)
    rezultat_3 = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Grecia", 100)
    assert len(rezultat_3) == 0

def test_filtrare_dupa_luna():
    # --- Setup ---
    # Pachet 1: 15 Ian - 25 Ian (complet in Ianuarie)
    p1 = {"destinatie": "A", "data_inceput": converteste_string_in_data("15/01/2025"), "data_sfarsit": converteste_string_in_data("25/01/2025"), "pret": 100}
    # Pachet 2: 15 Feb - 5 Mar (trece din Feb in Mar)
    p2 = {"destinatie": "B", "data_inceput": converteste_string_in_data("15/02/2025"), "data_sfarsit": converteste_string_in_data("05/03/2025"), "pret": 200}
    # Pachet 3: 10 Apr - 20 Apr (complet in Aprilie)
    p3 = {"destinatie": "C", "data_inceput": converteste_string_in_data("10/04/2025"), "data_sfarsit": converteste_string_in_data("20/04/2025"), "pret": 300}
    # Pachet 4: 15 Dec - 10 Ian (trece peste an, atinge Dec si Ian)
    p4 = {"destinatie": "D", "data_inceput": converteste_string_in_data("15/12/2024"), "data_sfarsit": converteste_string_in_data("10/01/2025"), "pret": 400}

    lista_test = [p1, p2, p3, p4]

    # 1. Filtram luna Ianuarie (1). Ar trebui sa elimine p1 si p4. Raman p2, p3.
    rezultat_ian = filtrare_dupa_luna(lista_test, 1)
    assert len(rezultat_ian) == 2
    assert rezultat_ian[0]["destinatie"] == "B" # p2
    assert rezultat_ian[1]["destinatie"] == "C" # p3

    # 2. Filtram luna Martie (3). Ar trebui sa elimine p2. Raman p1, p3, p4.
    rezultat_mar = filtrare_dupa_luna(lista_test, 3)
    assert len(rezultat_mar) == 3
    assert rezultat_mar[0]["destinatie"] == "A" # p1
    assert rezultat_mar[1]["destinatie"] == "C" # p3
    assert rezultat_mar[2]["destinatie"] == "D" # p4

    # 3. Filtram luna Decembrie (12). Ar trebui sa elimine p4. Raman p1, p2, p3.
    rezultat_dec = filtrare_dupa_luna(lista_test, 12)
    assert len(rezultat_dec) == 3
    assert rezultat_dec[0]["destinatie"] == "A" # p1
    assert rezultat_dec[1]["destinatie"] == "B" # p2
    assert rezultat_dec[2]["destinatie"] == "C" # p3

    # 4. Filtram luna Iunie (6) - nicio oferta nu o atinge. Raman toate.
    rezultat_iun = filtrare_dupa_luna(lista_test, 6)
    assert len(rezultat_iun) == 4

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 4


def test_raport_perioada_sortat_pret():
    # --- Setup ---
    data_1 = converteste_string_in_data("01/01/2025")
    data_5 = converteste_string_in_data("05/01/2025")
    data_10 = converteste_string_in_data("10/01/2025")
    data_15 = converteste_string_in_data("15/01/2025")

    # p1: in interval, pret 200
    p1 = {"destinatie": "A", "data_inceput": data_1, "data_sfarsit": data_5, "pret": 200}
    # p2: in interval, pret 100
    p2 = {"destinatie": "B", "data_inceput": data_5, "data_sfarsit": data_10, "pret": 100}
    # p3: in afara intervalului (sfarseste prea tarziu), pret 50
    p3 = {"destinatie": "C", "data_inceput": data_10, "data_sfarsit": data_15, "pret": 50}
    # p4: in interval, pret 300
    p4 = {"destinatie": "D", "data_inceput": data_1, "data_sfarsit": data_10, "pret": 300}

    lista_test = [p1, p2, p3, p4]

    # --- Act ---
    # Cautam in intervalul [01/01, 10/01].
    # Functia 'cauta_dupa_interval' gaseste pachetele *continute complet*.
    # Ar trebui sa gaseasca p1 (pret 200), p2 (pret 100), p4 (pret 300).
    # Ordinea sortata trebuie sa fie: p2 (100), p1 (200), p4 (300).

    data_start_cautare = data_1
    data_end_cautare = data_10

    rezultat_sortat = raport_perioada_sortat_pret(lista_test, data_start_cautare, data_end_cautare)

    # --- Assert ---
    assert len(rezultat_sortat) == 3

    # Verificam ordinea preturilor
    assert rezultat_sortat[0]["pret"] == 100  # p2
    assert rezultat_sortat[1]["pret"] == 200  # p1
    assert rezultat_sortat[2]["pret"] == 300  # p4

    # Verificam ca sunt pachetele corecte
    assert rezultat_sortat[0]["destinatie"] == "B"
    assert rezultat_sortat[1]["destinatie"] == "A"
    assert rezultat_sortat[2]["destinatie"] == "D"

    # Test caz fara rezultate
    data_start_cautare_noua = converteste_string_in_data("01/06/2025")
    data_end_cautare_noua = converteste_string_in_data("10/06/2025")
    rezultat_gol = raport_perioada_sortat_pret(lista_test, data_start_cautare_noua, data_end_cautare_noua)
    assert len(rezultat_gol) == 0