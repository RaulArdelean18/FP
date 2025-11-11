from Lab79.domain.exceptions import StudentValidError, ProblemaValidError

class StudentValidator:
    """
    Validează un obiect de tip Student.
    Adună toate erorile și le aruncă într-o singură excepție StudentValidError.
    """
    def valideaza(self, student):
        erori = []
        if not isinstance(student.studentID, int) or student.studentID <= 0:
            erori.append("ID-ul studentului trebuie să fie un număr întreg pozitiv.")

        if student.nume == "":
            erori.append("Numele studentului nu poate fi gol.")

        if not isinstance(student.grup, int) or student.grup <= 0:
            erori.append("Grupa trebuie să fie un număr întreg pozitiv.")

        if len(erori) > 0:
            # Dacă s-au găsit erori, ridicăm o excepție care le conține pe toate
            raise StudentValidError(erori)


class ProblemaValidator:
    """
    Validează un obiect de tip ProblemaLaborator.
    """
    def valideaza(self, problema):
        erori = []

        # Validăm formatul "lab_prob", ex: "7_1", "10_3"
        parts = problema.nrLab_nrProb.split('_')
        if len(parts) != 2:
            erori.append("Numărul problemei trebuie să fie de forma 'nrLab_nrProb'.")
        else:
            try:
                lab = int(parts[0])
                prob = int(parts[1])
                if lab <= 0 or prob <= 0:
                    erori.append("Numărul laboratorului și al problemei trebuie să fie pozitive.")
            except ValueError:
                erori.append("Numărul laboratorului și al problemei trebuie să fie numere.")

        if problema.descriere == "":
            erori.append("Descrierea problemei nu poate fi goală.")

        if problema.deadline == "":
            erori.append("Deadline-ul nu poate fi gol.")  # Se poate extinde cu validare de dată

        if len(erori) > 0:
            raise ProblemaValidError(erori)