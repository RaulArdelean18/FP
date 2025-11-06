from Lab46.data_base.services import *
from Lab46.utilitati.date_converter import converteste_string_in_data

def setup_date_pachete():
    """Creeaza un set de pachete si date pentru teste."""

    # Datele
    d_01_01 = converteste_string_in_data("01/01/2025")
    d_05_01 = converteste_string_in_data("05/01/2025")
    d_10_01 = converteste_string_in_data("10/01/2025")
    d_15_01 = converteste_string_in_data("15/01/2025")

    # Folosim 'creeaza_pachet' pentru a crea pachetele de test
    p1 = creeaza_pachet("Grecia", d_01_01, d_05_01, 100.0)
    p2 = creeaza_pachet("Italia", d_01_01, d_10_01, 200.0)
    p3 = creeaza_pachet("Grecia", d_05_01, d_15_01, 150.0)

    # Lista initiala
    lista_pachete = [p1, p2, p3]

    return lista_pachete, d_01_01, d_05_01, d_10_01, d_15_01


# --- Teste pentru Gettere si Creare---
def test_gettere_si_creare_pachet():
    """
    Testeaza creatorul de pachet ('creeaza_pachet') si
    getterele ('get_destinatie', 'get_pret', etc.).
    """
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
    """
    Testeaza functia IMUTABILA 'adauga_pachet'.
    Verifica daca lista noua este corecta SI ca cea veche nu s-a modificat.
    """
    lista_test_initiala = []
    d_start = converteste_string_in_data("01/01/2025")
    d_end = converteste_string_in_data("05/01/2025")

    # 1. Adaugam primul pachet
    lista_noua_1 = adauga_pachet(lista_test_initiala, "Spania", d_start, d_end, 500)

    # Verificam ca lista originala NU s-a modificat
    assert len(lista_test_initiala) == 0
    # Verificam lista noua
    assert len(lista_noua_1) == 1
    assert get_destinatie(lista_noua_1[0]) == "Spania"
    assert get_pret(lista_noua_1[0]) == 500.0

    # 2. Adaugam al doilea pachet, pornind de la lista noua (lista_noua_1)
    lista_noua_2 = adauga_pachet(lista_noua_1, "Turcia", d_start, d_end, 300)

    # Verificam ca prima lista noua nu s-a modificat
    assert len(lista_noua_1) == 1
    # Verificam a doua lista noua
    assert len(lista_noua_2) == 2
    assert get_destinatie(lista_noua_2[1]) == "Turcia"


def test_modifica_pachet():
    """
    Testeaza functia 'modifica_pachet'.
    Verifica daca lista noua este corecta SI ca cea veche nu s-a modificat.
    """
    lista_test_initiala, d_01_01, d_05_01, _, _ = setup_date_pachete()

    d_new_start = converteste_string_in_data("02/01/2025")
    d_new_end = converteste_string_in_data("06/01/2025")

    lista_noua = modifica_pachet(lista_test_initiala, 0, "Spania", d_new_start, d_new_end, 999.0)

    # Verificam lista noua
    assert len(lista_noua) == 3
    assert get_destinatie(lista_noua[0]) == "Spania"
    assert get_pret(lista_noua[0]) == 999.0
    assert get_data_inceput(lista_noua[0]) == d_new_start

    # Verificam ca lista ORIGINALA NU s-a modificat
    assert get_destinatie(lista_test_initiala[0]) == "Grecia"
    assert get_pret(lista_test_initiala[0]) == 100.0
    assert get_destinatie(lista_test_initiala[1]) == "Italia"  # Verificam si alt pachet


def test_sterge_dupa_durata():
    '''
    testam daca stergem corect dupa durata
    '''
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: 4 zile, p2: 9 zile, p3: 10 zile

    # Pastram pachetele >= 5 zile (ar trebui sa stearga p1)
    rezultat = sterge_dupa_durata(lista_test, 5)
    assert len(rezultat) == 2
    assert get_destinatie(rezultat[0]) == "Italia"  # p2
    assert get_destinatie(rezultat[1]) == "Grecia"  # p3

    # Pastram pachetele >= 10 zile (ar trebui sa stearga p1, p2)
    rezultat_2 = sterge_dupa_durata(lista_test, 10)
    assert len(rezultat_2) == 1
    assert get_destinatie(rezultat_2[0]) == "Grecia"  # p3

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 3


def test_sterge_dupa_destinatie():
    '''
    testam daca stergem corect dupa destinatie
    '''
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, p2: Italia, p3: Grecia

    # Stergem "Grecia" (ar trebui sa ramana p2)
    rezultat = sterge_dupa_destinatie(lista_test, "Grecia")
    assert len(rezultat) == 1
    assert get_destinatie(rezultat[0]) == "Italia"

    # Stergem "Spania" (nu exista, nu sterge nimic)
    rezultat_2 = sterge_dupa_destinatie(lista_test, "Spania")
    assert len(rezultat_2) == 3

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 3


def test_sterge_dupa_pret():
    '''
    testam daca stergem corect dupa pret
    '''
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: 100, p2: 200, p3: 150

    # Pastram pachetele <= 160 (ar trebui sa stearga p2)
    rezultat = sterge_dupa_pret(lista_test, 160)
    assert len(rezultat) == 2
    assert get_pret(rezultat[0]) == 100.0  # p1
    assert get_pret(rezultat[1]) == 150.0  # p3

    # Pastram pachetele <= 99 (ar trebui sa stearga tot)
    rezultat_2 = sterge_dupa_pret(lista_test, 99)
    assert len(rezultat_2) == 0

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 3


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
    assert get_destinatie(rezultat_2[0]) == "Grecia"
    assert get_pret(rezultat_2[0]) == 100.0

    # Cautam intervalul [05/01, 10/01] (gaseste doar p2, p3 depaseste.
    # p2 (01-10) nu e complet in [05-10]. p3 (05-15) nu e.
    # pachet (05-10) ar fi gasit
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
    assert get_pret(rezultat_2[0]) == 100.0

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
    assert get_destinatie(rezultat[0]) == "Italia"

    # Cautam sfarsit pe 05/01 (ar trebui sa gaseasca p1)
    rezultat_2 = cauta_dupa_data_sfarsit(lista_test, d_05_01)
    assert len(rezultat_2) == 1
    assert get_pret(rezultat_2[0]) == 100.0

    # Cautam sfarsit pe 06/01 (nu gaseste nimic)
    d_06_01 = converteste_string_in_data("06/01/2025")
    rezultat_3 = cauta_dupa_data_sfarsit(lista_test, d_06_01)
    assert len(rezultat_3) == 0


def test_filtrare_oferte_dupa_pret_si_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, 100
    # p2: Italia, 200
    # p3: Grecia, 150

    # Filtram: destinatie != "Grecia" SI pret <= 250 (ar trebui sa gaseasca p2)
    rezultat = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Grecia", 250)
    assert len(rezultat) == 1
    assert get_destinatie(rezultat[0]) == "Italia"

    # Filtram: destinatie != "Spania" SI pret <= 160 (ar trebui sa gaseasca p1, p3)
    rezultat_2 = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Spania", 160)
    assert len(rezultat_2) == 2

    # Filtram: destinatie != "Grecia" SI pret <= 100 (nu gaseste nimic)
    rezultat_3 = filtrare_oferte_dupa_pret_si_destinatie(lista_test, "Grecia", 100)
    assert len(rezultat_3) == 0


def test_filtrare_dupa_luna():
    # Folosim 'creeaza_pachet'
    p1 = creeaza_pachet("A", converteste_string_in_data("15/01/2025"), converteste_string_in_data("25/01/2025"), 100)
    p2 = creeaza_pachet("B", converteste_string_in_data("15/02/2025"), converteste_string_in_data("05/03/2025"), 200)
    p3 = creeaza_pachet("C", converteste_string_in_data("10/04/2025"), converteste_string_in_data("20/04/2025"), 300)
    p4 = creeaza_pachet("D", converteste_string_in_data("15/12/2024"), converteste_string_in_data("10/01/2025"), 400)

    lista_test = [p1, p2, p3, p4]

    # 1. Filtram luna Ianuarie (1). Ar trebui sa elimine p1 si p4. Raman p2, p3.
    rezultat_ian = filtrare_dupa_luna(lista_test, 1)
    assert len(rezultat_ian) == 2
    assert get_destinatie(rezultat_ian[0]) == "B"  # p2
    assert get_destinatie(rezultat_ian[1]) == "C"  # p3

    # 2. Filtram luna Martie (3). Ar trebui sa elimine p2. Raman p1, p3, p4.
    rezultat_mar = filtrare_dupa_luna(lista_test, 3)
    assert len(rezultat_mar) == 3
    assert get_destinatie(rezultat_mar[0]) == "A"  # p1
    assert get_destinatie(rezultat_mar[1]) == "C"  # p3
    assert get_destinatie(rezultat_mar[2]) == "D"  # p4

    # Verificam ca lista originala nu s-a modificat
    assert len(lista_test) == 4


def test_raport_perioada_sortat_pret():
    data_1 = converteste_string_in_data("01/01/2025")
    data_5 = converteste_string_in_data("05/01/2025")
    data_10 = converteste_string_in_data("10/01/2025")
    data_15 = converteste_string_in_data("15/01/2025")

    # Folosim 'creeaza_pachet'
    p1 = creeaza_pachet("A", data_1, data_5, 200)
    p2 = creeaza_pachet("B", data_5, data_10, 100)
    p3 = creeaza_pachet("C", data_10, data_15, 50)
    p4 = creeaza_pachet("D", data_1, data_10, 300)

    lista_test = [p1, p2, p3, p4]

    data_start_cautare = data_1
    data_end_cautare = data_10

    rezultat_sortat = raport_perioada_sortat_pret(lista_test, data_start_cautare, data_end_cautare)

    assert len(rezultat_sortat) == 3

    # Verificam ordinea preturilor
    assert get_pret(rezultat_sortat[0]) == 100  # p2
    assert get_pret(rezultat_sortat[1]) == 200  # p1
    assert get_pret(rezultat_sortat[2]) == 300  # p4

    # Verificam ca sunt pachetele corecte
    assert get_destinatie(rezultat_sortat[0]) == "B"
    assert get_destinatie(rezultat_sortat[1]) == "A"
    assert get_destinatie(rezultat_sortat[2]) == "D"

    # Test caz fara rezultate
    data_start_cautare_noua = converteste_string_in_data("01/06/2025")
    data_end_cautare_noua = converteste_string_in_data("10/06/2025")
    rezultat_gol = raport_perioada_sortat_pret(lista_test, data_start_cautare_noua, data_end_cautare_noua)
    assert len(rezultat_gol) == 0


def test_raport_numar_oferte_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, p2: Italia, p3: Grecia

    # Test 1: "Grecia" (ar trebui sa gaseasca 2)
    assert raport_numar_oferte_destinatie(lista_test, "Grecia") == 2

    # Test 2: "Italia" (ar trebui sa gaseasca 1)
    assert raport_numar_oferte_destinatie(lista_test, "Italia") == 1

    # Test 3: "Spania" (ar trebui sa gaseasca 0)
    assert raport_numar_oferte_destinatie(lista_test, "Spania") == 0


def test_raport_medie_pret_destinatie():
    lista_test, _, _, _, _ = setup_date_pachete()
    # p1: Grecia, 100.0
    # p2: Italia, 200.0
    # p3: Grecia, 150.0

    # Test 1: "Grecia" ( (100 + 150) / 2 = 125.0 )
    assert raport_medie_pret_destinatie(lista_test, "Grecia") == 125.0

    # Test 2: "Italia" ( 200 / 1 = 200.0 )
    assert raport_medie_pret_destinatie(lista_test, "Italia") == 200.0

    # Test 3: "Spania" ( 0 / 0 = 0 )
    assert raport_medie_pret_destinatie(lista_test, "Spania") == 0