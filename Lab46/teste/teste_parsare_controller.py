from datetime import datetime
from Lab46.app.parsare_controller import _valideaza_si_converteste_pachet, _valideaza_date_interval


def test_valideaza_pachet_corect():
    """Testeaza validarea corecta a unui pachet."""
    params = ["Paris", "10/12/2025", "15/12/2025", "500.50"]

    dest, start, end, pret = _valideaza_si_converteste_pachet(params)

    assert dest == "Paris"
    assert start == datetime(2025, 12, 10)
    assert end == datetime(2025, 12, 15)
    assert pret == 500.50


def test_valideaza_pachet_erori():
    """Testeaza diferitele erori la validarea pachetului."""

    # 1. Test parametri insuficienti
    params_1 = ["Paris", "10/12/2025", "15/12/2025"]
    try:
        _valideaza_si_converteste_pachet(params_1)
        assert False  # Ar trebui sa ridice exceptie
    except ValueError as e:
        assert str(e) == "Comanda 'add' necesita 4 parametri: destinatie, data_start, data_sf, pret"

    # 2. Test data start invalida
    params_2 = ["Paris", "data-rea", "15/12/2025", "100"]
    try:
        _valideaza_si_converteste_pachet(params_2)
        assert False
    except ValueError as e:
        assert "Format data invalid" in str(e)

    # 3. Test interval temporal gresit
    params_3 = ["Paris", "15/12/2025", "10/12/2025", "100"]
    try:
        _valideaza_si_converteste_pachet(params_3)
        assert False
    except ValueError as e:
        assert "Data de sfarsit trebuie sa fie dupa data de inceput" in str(e)

    # 4. Test pret invalid
    params_4 = ["Paris", "10/12/2025", "15/12/2025", "o-suta"]
    try:
        _valideaza_si_converteste_pachet(params_4)
        assert False
    except ValueError as e:
        assert "Pretul 'o-suta' trebuie sa fie un numar" in str(e)


def test_valideaza_interval_corect():
    """Testeaza validarea corecta a unui interval."""
    params = ["01/01/2025", "05/01/2025"]

    start, end = _valideaza_date_interval(params)

    assert start == datetime(2025, 1, 1)
    assert end == datetime(2025, 1, 5)


def test_valideaza_interval_erori():
    """Testeaza diferitele erori la validarea intervalului."""

    # 1. Test parametri insuficienti
    params_1 = ["01/01/2025"]
    try:
        _valideaza_date_interval(params_1)
        assert False
    except ValueError as e:
        assert str(e) == "Comanda necesita 2 parametri: data_start si data_sfarsit (zz/ll/aaaa)."

    # 2. Test interval temporal gresit
    params_2 = ["05/01/2025", "01/01/2025"]
    try:
        _valideaza_date_interval(params_2)
        assert False
    except ValueError as e:
        assert "Data de sfarsit trebuie sa fie dupa data de inceput" in str(e)