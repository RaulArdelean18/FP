import datetime
from Lab46.utilitati.date_converter import converteste_string_in_data, format_data_manual


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
    data_obj = datetime.datetime(2024, 10, 25)
    assert format_data_manual(data_obj) == "25/10/2024"

    # Test alt caz valid
    data_obj_2 = datetime.datetime(2025, 1, 5)
    assert format_data_manual(data_obj_2) == "5/1/2025"