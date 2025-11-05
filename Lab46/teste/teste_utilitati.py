import datetime
from Lab46.utilitati.date_converter import *
from Lab46.data_base.services import *
from Lab46.utilitati.date_converter import *
from Lab46.app.pachete_manager import *



def test_converteste_string_in_data():
    # Test caz valid
    data_str = "25/10/2024"
    data_obj = converteste_string_in_data(data_str)
    assert data_obj is not None
    assert data_obj.day == 25
    assert data_obj.month == 10
    assert data_obj.year == 2024

    # Test caz invalid - format gresit
    assert converteste_string_in_data("25-10-2024") is None

    # Test caz invalid - litere
    assert converteste_string_in_data("abc") is None

    # Test caz invalid - data inexistenta (ex: 32 Octombrie)
    # Implementarea ta curenta prinde exceptia de la datetime()
    assert converteste_string_in_data("32/10/2024") is None

    # Test caz invalid - prea putine parti
    assert converteste_string_in_data("25/10") is None


def test_format_data_manual():
    # Test caz valid
    data_obj = datetime(2024, 10, 25)
    assert format_data_manual(data_obj) == "25/10/2024"

    # Test alt caz valid
    data_obj_2 = datetime(2025, 1, 5)
    assert format_data_manual(data_obj_2) == "5/1/2025"


def test_functionalitate_undo():
    """
    Testeaza intregul flux de undo:
    1. Simuleaza adaugarea starilor in istoric (cum face controller.py)
    2. Simuleaza apelarea functiilor de logica (cum face controller.py)
    3. Apeleaza executa_undo() (din stare.py)
    4. Verifica daca starea a revenit corect.
    """
    # Cream date de test
    d1 = converteste_string_in_data("01/01/2025")
    d2 = converteste_string_in_data("05/01/2025")
    d3 = converteste_string_in_data("10/01/2025")
    d4 = converteste_string_in_data("15/01/2025")

    # 1. Starea Initiala
    manager = creeaza_manager_stare()
    assert get_lista_curenta(manager) == []
    assert get_lista_undo(manager) == []
    assert are_stari_undo(manager) is False

    # 2. Simulam Operatia 1: Adauga Pachet 1 (Grecia)
    # Controller-ul ar salva starea curenta (lista goala)
    stare_inainte_op1 = get_lista_curenta(manager).copy()
    adauga_la_undo(manager, stare_inainte_op1)

    # UI-ul ar apela serviciul, care returneaza o lista noua
    lista_op1 = adauga_pachet(get_lista_curenta(manager), "Grecia", d1, d2, 100)
    # Controller-ul ar seta starea noua
    set_lista_curenta(manager, lista_op1)

    assert len(get_lista_curenta(manager)) == 1
    assert get_destinatie(get_lista_curenta(manager)[0]) == "Grecia"
    assert len(get_lista_undo(manager)) == 1
    assert get_lista_undo(manager)[0] == []  # Starea salvata era lista goala

    # 3. Simulam Operatia 2: Adauga Pachet 2 (Italia)
    # Controller-ul salveaza starea curenta (lista cu "Grecia")
    stare_inainte_op2 = get_lista_curenta(manager).copy()
    adauga_la_undo(manager, stare_inainte_op2)

    lista_op2 = adauga_pachet(get_lista_curenta(manager), "Italia", d3, d4, 200)
    set_lista_curenta(manager, lista_op2)

    assert len(get_lista_curenta(manager)) == 2
    assert get_destinatie(get_lista_curenta(manager)[1]) == "Italia"
    assert len(get_lista_undo(manager)) == 2

    # 4. Simulam Operatia 3: Sterge "Grecia"
    # Controller-ul salveaza starea curenta (lista cu "Grecia" si "Italia")
    stare_inainte_op3 = get_lista_curenta(manager).copy()
    adauga_la_undo(manager, stare_inainte_op3)

    lista_op3 = sterge_dupa_destinatie(get_lista_curenta(manager), "Grecia")
    set_lista_curenta(manager, lista_op3)

    assert len(get_lista_curenta(manager)) == 1  # A ramas doar "Italia"
    assert get_destinatie(get_lista_curenta(manager)[0]) == "Italia"
    assert len(get_lista_undo(manager)) == 3

    # --- INCEPE TESTAREA UNDO ---

    # 5. TEST UNDO 1 (Anuleaza stergerea Greciei)
    assert executa_undo(manager) is True
    # Verificam daca starea curenta este cea de dinainte de Op. 3 (stare_inainte_op3)
    assert len(get_lista_curenta(manager)) == 2
    assert get_destinatie(get_lista_curenta(manager)[0]) == "Grecia"
    assert get_destinatie(get_lista_curenta(manager)[1]) == "Italia"
    assert len(get_lista_undo(manager)) == 2  # S-a scos o stare din istoric

    # 6. TEST UNDO 2 (Anuleaza adaugarea Italiei)
    assert executa_undo(manager) is True
    # Verificam daca starea curenta este cea de dinainte de Op. 2 (stare_inainte_op2)
    assert len(get_lista_curenta(manager)) == 1
    assert get_destinatie(get_lista_curenta(manager)[0]) == "Grecia"
    assert len(get_lista_undo(manager)) == 1

    # 7. TEST UNDO 3 (Anuleaza adaugarea Greciei)
    assert executa_undo(manager) is True
    # Verificam daca starea curenta este cea de dinainte de Op. 1 (stare_inainte_op1)
    assert len(get_lista_curenta(manager)) == 0
    assert len(get_lista_undo(manager)) == 0

    # 8. TEST UNDO ESEC (Nu mai sunt stari)
    assert are_stari_undo(manager) is False
    assert executa_undo(manager) is False
    assert len(get_lista_curenta(manager)) == 0  # Starea ramane goala
    assert len(get_lista_undo(manager)) == 0