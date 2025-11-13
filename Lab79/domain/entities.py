class Student:
    """
    Clasa de domeniu care definește un Student.
    """

    def __init__(self, student_id, nume, grup):
        self.__studentID = student_id
        self.__nume = nume
        self.__grup = grup

    # --- Getters (folosind @property) ---

    @property
    def studentID(self):
        return self.__studentID

    @property
    def nume(self):
        return self.__nume

    @property
    def grup(self):
        return self.__grup

    @property
    def id(self):
        """ Getter comun pentru ID-ul unic al entității. """
        return self.__studentID
    # --- Setters ---

    @nume.setter
    def nume(self, value):
        self.__nume = value

    @grup.setter
    def grup(self, value):
        self.__grup = value

    def __str__(self):
        """ Returnează o reprezentare string a obiectului Student. """
        return f"[ID: {self.__studentID}] Nume: {self.__nume}, Grupa: {self.__grup}"

    def __eq__(self, other):
        """
        Verifică egalitatea între doi studenți (bazat pe ID).
        Permite folosirea operatorului '==' (ex: student1 == student2)
        """
        if not isinstance(other, Student):
            return False
        return self.__studentID == other.__studentID


class ProblemaLaborator:
    """
    Clasa de domeniu care definește o Problemă de Laborator.
    """

    def __init__(self, nr_lab_nr_prob, descriere, deadline):
        # nrLab_nrProb este un string de forma "lab_prob", ex: "7_2"
        self.__nrLab_nrProb = nr_lab_nr_prob
        self.__descriere = descriere
        self.__deadline = deadline

    # --- Getters ---

    @property
    def nrLab_nrProb(self):
        return self.__nrLab_nrProb

    @property
    def descriere(self):
        return self.__descriere

    @property
    def deadline(self):
        return self.__deadline

    @property
    def id(self):
        """ Getter comun pentru ID-ul unic al entității. """
        return self.__nrLab_nrProb

    # --- Setters ---

    @descriere.setter
    def descriere(self, value):
        self.__descriere = value

    @deadline.setter
    def deadline(self, value):
        self.__deadline = value


    def __str__(self):
        """ Returnează o reprezentare string a obiectului ProblemaLaborator. """
        return f"[Nr: {self.__nrLab_nrProb}] Descriere: {self.__descriere}, Deadline: {self.__deadline}"

    def __eq__(self, other):
        """
        Verifică egalitatea între două probleme (bazat pe nrLab_nrProb).
        """
        if not isinstance(other, ProblemaLaborator):
            return False
        return self.__nrLab_nrProb == other.__nrLab_nrProb