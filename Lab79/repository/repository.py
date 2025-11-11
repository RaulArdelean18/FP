from Lab79.domain.exceptions import DuplicateIDError, InexistentIDError, RepoError


class Repository:
    """
    Repository generic pentru stocarea entităților în memorie.
    Stocarea se face într-un dicționar, folosind ID-ul entității ca cheie.
    """

    def __init__(self):
        self.__entities = {}  # Dicționar pentru stocare:{entity.id: entity_object}

    def __len__(self):
        """ Returnează numărul de entități din repository. """
        return len(self.__entities)

    def add(self, entity):
        """
        Adaugă o entitate nouă în repository.
        :param entity: Obiectul de tip entitate (ex: Student, ProblemaLaborator)
        :raises DuplicateIDError: dacă o entitate cu același ID există deja.
        """
        entity_id = entity.id
        if entity_id in self.__entities:
            raise DuplicateIDError(f"Entitatea cu ID-ul {entity_id} există deja.")

        self.__entities[entity_id] = entity

    def find_by_id(self, entity_id):
        """
        Găsește o entitate după ID.
        :param entity_id: ID-ul entității căutate.
        :return: Obiectul entitate.
        :raises InexistentIDError:dacă ID-ul nu este găsit.
        """
        if entity_id not in self.__entities:
            raise InexistentIDError(f"Entitatea cu ID-ul {entity_id} nu a fost găsită.")

        return self.__entities[entity_id]

    def delete(self, entity_id):
        """
        Șterge o entitate după ID.
        :param entity_id: ID-ul entității de șters.
        :raises InexistentIDError: dacă ID-ul nu este găsit.
        """
        if entity_id not in self.__entities:
            raise InexistentIDError(f"Entitatea cu ID-ul {entity_id} nu a fost găsită.")

        del self.__entities[entity_id]

    def update(self, entity_id, new_entity):
        """
        Actualizează o entitate existentă.
        :param entity_id: ID-ul entității de actualizat.
        :param new_entity: Noua entitate care o va înlocui pe cea veche.
        :raises InexistentIDError: dacă ID-ul nu este găsit.
        """
        if entity_id not in self.__entities:
            raise InexistentIDError(f"Entitatea cu ID-ul {entity_id} nu a fost găsită.")

        # Asigură-te că ID-ul noii entități este același
        if entity_id != new_entity.id:
            raise RepoError("ID-ul entității noi nu corespunde cu cel care trebuie actualizat.")

        self.__entities[entity_id] = new_entity

    def get_all(self):
        """
        Returnează o listă cu toate entitățile din repository.
        :return: O listă de obiecte entitate.
        """
        # Returnăm valorile din dicționar (obiectele entitate)
        return list(self.__entities.values())