from Lab79.domain.entities import Student, ProblemaLaborator
from Lab79.domain.exceptions import StudentValidError, ProblemaValidError
from Lab79.domain.validators import StudentValidator, ProblemaValidator


def test_student_validator_valideaza():
    """Testează funcția: StudentValidator.valideaza()"""
    validator = StudentValidator()

    # Cazul Bun
    student_valid = Student(1, "Pop Ion", 935)
    try:
        validator.valideaza(student_valid)
    except StudentValidError:
        assert False, "EROARE: Validatorul a picat un student valid."

    # Cazul Rău (Nume gol)
    student_nume_invalid = Student(1, "", 935)
    prins = False
    try:
        validator.valideaza(student_nume_invalid)
    except StudentValidError:
        prins = True
    assert prins, "EROARE: Validatorul nu a prins un student cu nume gol."

    # Cazul Rău (ID invalid)
    student_id_invalid = Student(0, "Nume", 935)
    prins = False
    try:
        validator.valideaza(student_id_invalid)
    except StudentValidError:
        prins = True
    assert prins, "EROARE: Validatorul nu a prins un student cu ID invalid."


def test_problema_validator_valideaza():
    """Testează funcția: ProblemaValidator.valideaza()"""
    validator = ProblemaValidator()

    # Cazul Bun
    prob_valida = ProblemaLaborator("7_2", "Descriere", "S10")
    try:
        validator.valideaza(prob_valida)
    except ProblemaValidError:
        assert False, "EROARE: Validatorul a picat o problemă validă."

    # Cazul Rău (Descriere goală)
    prob_invalida = ProblemaLaborator("7_2", "", "S10")
    prins = False
    try:
        validator.valideaza(prob_invalida)
    except ProblemaValidError:
        prins = True
    assert prins, "EROARE: Validatorul nu a prins o problemă cu descriere goală."

    # Cazul Rău (Format ID)
    prob_id_invalid = ProblemaLaborator("7-2", "Descriere", "S10")
    prins = False
    try:
        validator.valideaza(prob_id_invalid)
    except ProblemaValidError:
        prins = True
    assert prins, "EROARE: Validatorul nu a prins o problemă cu format ID invalid."