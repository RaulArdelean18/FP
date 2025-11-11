from Lab79.controller.controllers import StudentController
from Lab79.domain.exceptions import StudentValidError, DuplicateIDError, InexistentIDError
from Lab79.domain.validators import StudentValidator
from Lab79.repository.repository import Repository


def test_controller_add_student():
    """Testează funcția: StudentController.add_student()"""
    repo = Repository()
    validator = StudentValidator()
    ctrl = StudentController(repo, validator)

    # Cazul Bun
    ctrl.add_student(1, "Ion", 935)
    assert ctrl.get_numar_studenti() == 1

    # Cazul Rău (Validare)
    prins_validare = False
    try:
        ctrl.add_student(2, "", 935)  # Nume gol
    except StudentValidError:
        prins_validare = True
    assert prins_validare, "EROARE [Ctrl]: Nu a prins eroarea de validare."
    assert ctrl.get_numar_studenti() == 1  # Nu l-a adăugat

    # Cazul Rău (Repo - Duplicat)
    prins_repo = False
    try:
        ctrl.add_student(1, "Ana", 936)  # ID duplicat
    except DuplicateIDError:
        prins_repo = True
    assert prins_repo, "EROARE [Ctrl]: Nu a prins eroarea de ID duplicat."
    assert ctrl.get_numar_studenti() == 1


def test_controller_delete_student():
    """Testează funcția: StudentController.delete_student()"""
    repo = Repository()
    validator = StudentValidator()
    ctrl = StudentController(repo, validator)
    ctrl.add_student(1, "Ion", 935)

    # Cazul Bun
    ctrl.delete_student(1)
    assert ctrl.get_numar_studenti() == 0

    # Cazul Rău (Inexistent)
    prins = False
    try:
        ctrl.delete_student(999)
    except InexistentIDError:
        prins = True
    assert prins, "EROARE [Ctrl]: Nu a prins ștergerea unui ID inexistent."


def test_controller_update_student():
    """Testează funcția: StudentController.update_student()"""
    repo = Repository()
    validator = StudentValidator()
    ctrl = StudentController(repo, validator)
    ctrl.add_student(1, "Ion", 935)

    # Cazul Bun
    ctrl.update_student(1, "Ion Nou", 936)
    student_modificat = ctrl.find_student_by_id(1)
    assert student_modificat.nume == "Ion Nou"

    # Cazul Rău (Validare)
    prins_validare = False
    try:
        ctrl.update_student(1, "", 937)  # Nume gol
    except StudentValidError:
        prins_validare = True
    assert prins_validare, "EROARE [Ctrl]: Nu a prins validarea la update."

    # Cazul Rău (Inexistent)
    prins_repo = False
    try:
        ctrl.update_student(999, "Nume", 937)
    except InexistentIDError:
        prins_repo = True
    assert prins_repo, "EROARE [Ctrl]: Nu a prins update pe ID inexistent."


def test_controller_find_student_by_id():
    """Testează funcția: StudentController.find_student_by_id()"""
    repo = Repository()
    validator = StudentValidator()
    ctrl = StudentController(repo, validator)
    ctrl.add_student(1, "Ion", 935)

    # Cazul Bun
    student_gasit = ctrl.find_student_by_id(1)
    assert student_gasit.nume == "Ion"

    # Cazul Rău (Inexistent)
    prins = False
    try:
        ctrl.find_student_by_id(999)
    except InexistentIDError:
        prins = True
    assert prins, "EROARE [Ctrl]: Nu a prins căutarea unui ID inexistent."


def test_controller_get_all_students():
    """Testează funcția: StudentController.get_all_students()"""
    repo = Repository()
    validator = StudentValidator()
    ctrl = StudentController(repo, validator)

    assert ctrl.get_all_students() == []
    ctrl.add_student(1, "Ion", 935)
    lista = ctrl.get_all_students()
    assert len(lista) == 1
    assert lista[0].id == 1