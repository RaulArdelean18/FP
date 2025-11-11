# Nu este nevoie să importăm validatorii sau repository-ul, deoarece le vom primi ca parametri în constructor (injecție de dependențe).
from Lab79.domain.entities import Student, ProblemaLaborator

# --- Controller pentru Studenti ---

class StudentController:
    """
    Clasa Controller pentru operațiuni legate de Studenți.
    Face legătura între UI și straturile de Repository/Domain.
    """

    def __init__(self, repo_studenti, validator_student):
        self.__repo = repo_studenti
        self.__validator = validator_student

    def add_student(self, student_id, nume, grup):
        """
        Creează, validează și adaugă un student nou.
        :param student_id: int
        :param nume: string
        :param grup: int
        :raises StudentValidError: dacă datele studentului nu sunt valide.
        :raises DuplicateIDError: dacă ID-ul există deja.
        """
        # 1. Creează obiectul
        student = Student(student_id, nume, grup)

        # 2. Validează obiectul
        # Aici folosim validatorul primit în constructor
        # Metoda 'valideaza' va arunca StudentValidError dacă ceva e greșit
        self.__validator.valideaza(student)

        # 3. Adaugă în repository
        # Metoda 'add' va arunca DuplicateIDError dacă ID-ul există
        self.__repo.add(student)

    def delete_student(self, student_id):
        """
        Șterge un student după ID.
        :param student_id: int
        :raises InexistentIDError: dacă ID-ul nu există.
        """
        self.__repo.delete(student_id)

    def update_student(self, student_id, nume_nou, grup_nou):
        """
        Actualizează un student existent.
        :param student_id: int (ID-ul studentului de actualizat)
        :param nume_nou: string
        :param grup_nou: int
        :raises StudentValidError: dacă noile date nu sunt valide.
        :raises InexistentIDError: dacă ID-ul nu există.
        """
        # 1. Creează noua versiune a obiectului
        student_nou = Student(student_id, nume_nou, grup_nou)

        # 2. Validează noul obiect
        self.__validator.valideaza(student_nou)

        # 3. Actualizează în repository
        # Metoda 'update' va arunca InexistentIDError dacă ID-ul nu există
        self.__repo.update(student_id, student_nou)

    def find_student_by_id(self, student_id):
        """
        Găsește un student după ID.
        :param student_id: int
        :return: obiectul Student
        :raises InexistentIDError: dacă ID-ul nu există.
        """
        return self.__repo.find_by_id(student_id)

    def get_all_students(self):
        """
        Returnează o listă cu toți studenții.
        :return: listă de obiecte Student
        """
        return self.__repo.get_all()

    def get_numar_studenti(self):
        """ Returnează numărul total de studenți. """
        return len(self.__repo)


# --- Controller pentru Probleme ---

class ProblemaController:
    """
    Clasa Controller pentru operațiuni legate de Problemele de Laborator.
    """

    def __init__(self, repo_probleme, validator_problema):
        self.__repo = repo_probleme
        self.__validator = validator_problema

    def add_problema(self, nr_lab_nr_prob, descriere, deadline):
        """
        Creează, validează și adaugă o problemă nouă.
        """
        problema = ProblemaLaborator(nr_lab_nr_prob, descriere, deadline)
        self.__validator.valideaza(problema)
        self.__repo.add(problema)

    def delete_problema(self, nr_lab_nr_prob):
        """ Șterge o problemă după ID (nrLab_nrProb). """
        self.__repo.delete(nr_lab_nr_prob)

    def update_problema(self, nr_lab_nr_prob, descriere_noua, deadline_nou):
        """ Actualizează o problemă existentă. """
        problema_noua = ProblemaLaborator(nr_lab_nr_prob, descriere_noua, deadline_nou)
        self.__validator.valideaza(problema_noua)
        self.__repo.update(nr_lab_nr_prob, problema_noua)

    def find_problema_by_id(self, nr_lab_nr_prob):
        """ Găsește o problemă după ID. """
        return self.__repo.find_by_id(nr_lab_nr_prob)

    def get_all_probleme(self):
        """ Returnează o listă cu toate problemele. """
        return self.__repo.get_all()

    def get_numar_probleme(self):
        """ Returnează numărul total de probleme. """
        return len(self.__repo)