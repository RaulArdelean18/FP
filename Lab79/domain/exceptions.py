class ValidError(Exception):
    """
    Clasa de bază pentru erorile de validare din aplicație.
    """

    def __init__(self, mesaje):
        # mesaje poate fi o listă de string-uri cu toate erorile găsite
        self.__mesaje_eroare = mesaje

    @property
    def mesaje(self):
        return self.__mesaje_eroare

    def __str__(self):
        # Returnează un singur string cu toate erorile, separate de newline
        return "\n".join(self.__mesaje_eroare)


class StudentValidError(ValidError):
    """ Excepție ridicată pentru erori de validare la Student. """
    pass


class ProblemaValidError(ValidError):
    """ Excepție ridicată pentru erori de validare la ProblemaLaborator. """
    pass

class RepoError(Exception):
    """
    Clasa de bază pentru erorile din Repository.
    """
    def __init__(self, message="Eroare de Repository."):
        self.message = message
        super().__init__(self.message)

class DuplicateIDError(RepoError):
    """
    Ridicată când se încearcă adăugarea unei entități cu un ID care există deja.
    """
    def __init__(self, message="ID duplicat."):
        # Apelăm constructorul clasei de bază (RepoError)
        super().__init__(message)

class InexistentIDError(RepoError):
    """
    Ridicată când se caută o entitate cu un ID care nu există.
    """
    def __init__(self, message="ID inexistent."):
        # Apelăm constructorul clasei de bază (RepoError)
        super().__init__(message)
