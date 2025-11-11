from Lab79.domain.entities import Student
from Lab79.domain.exceptions import DuplicateIDError, InexistentIDError
from Lab79.repository.repository import Repository


def test_repository_add_and_len():
    """Testează funcțiile: Repository.add() și Repository.__len__()"""
    repo = Repository()
    student1 = Student(1, "Student A", 100)

    assert len(repo) == 0
    repo.add(student1)
    assert len(repo) == 1

    # Test ID Duplicat
    student_duplicat = Student(1, "Alt Nume", 102)
    prins = False
    try:
        repo.add(student_duplicat)
    except DuplicateIDError:
        prins = True
    assert prins, "EROARE [Repo]: Nu a prins ID duplicat la adăugare."
    assert len(repo) == 1  # Verificăm că nu l-a adăugat


def test_repository_get_all():
    """Testează funcția: Repository.get_all()"""
    repo = Repository()
    student1 = Student(1, "Student A", 100)
    student2 = Student(2, "Student B", 101)

    assert repo.get_all() == []
    repo.add(student1)
    assert repo.get_all() == [student1]
    repo.add(student2)
    assert repo.get_all() == [student1, student2]


def test_repository_find_by_id():
    """Testează funcția: Repository.find_by_id()"""
    repo = Repository()
    student1 = Student(1, "Student A", 100)
    repo.add(student1)

    # Cazul Bun
    gasit = repo.find_by_id(1)
    assert gasit == student1
    assert gasit.nume == "Student A"

    # Cazul Rău (Inexistent)
    prins = False
    try:
        repo.find_by_id(999)
    except InexistentIDError:
        prins = True
    assert prins, "EROARE [Repo]: Nu a prins ID inexistent la căutare."


def test_repository_delete():
    """Testează funcția: Repository.delete()"""
    repo = Repository()
    student1 = Student(1, "Student A", 100)
    repo.add(student1)
    assert len(repo) == 1

    # Cazul Bun
    repo.delete(1)
    assert len(repo) == 0

    # Cazul Rău (Inexistent)
    prins = False
    try:
        repo.delete(999)
    except InexistentIDError:
        prins = True
    assert prins, "EROARE [Repo]: Nu a prins ID inexistent la ștergere."


def test_repository_update():
    """Testează funcția: Repository.update()"""
    repo = Repository()
    student1 = Student(1, "Student A", 100)
    repo.add(student1)

    # Cazul Bun
    student_nou = Student(1, "Nume Nou", 101)
    repo.update(1, student_nou)
    gasit = repo.find_by_id(1)
    assert gasit.nume == "Nume Nou"

    # Cazul Rău (Inexistent)
    student_inexistent = Student(999, "Alt Nume", 102)
    prins = False
    try:
        repo.update(999, student_inexistent)
    except InexistentIDError:
        prins = True
    assert prins, "EROARE [Repo]: Nu a prins ID inexistent la actualizare."