from Lab79.domain.exceptions import ValidError, RepoError


class ConsoleUI:
    def __init__(self, controller_studenti, controller_probleme):
        """
        Se apelează la pornire. Primește controlerele pentru studenți și probleme și le salvează.
        """
        self.__ctrl_studenti = controller_studenti
        self.__ctrl_probleme = controller_probleme

    # --- Meniul Principal ---

    def __afiseaza_meniu(self):
        """Afișează meniul principal pe ecran."""
        print("\n--- MENIU GESTIUNE LABORATOARE ---")
        print("1. Gestiune Studenți")
        print("2. Gestiune Probleme Laborator")
        print("0. Ieșire din aplicație")
        print("---------------------------------")

    def run(self):
        """
        Inima aplicației. Rulează non-stop, afișează meniul principal
        și trimite utilizatorul la sub-meniurile corecte (studenți sau probleme).
        """
        while True:
            self.__afiseaza_meniu()
            operatie = input("Alegeți opțiunea: ").strip()
            if operatie == "1":
                self.__meniu_studenti()
            elif operatie == "2":
                self.__meniu_probleme()
            elif operatie == "0":
                print("La revedere!")
                return
            else:
                print("Comandă invalidă! Încercați din nou.")

    # --- Meniu Studenți ---

    def __meniu_studenti(self):
        """
        Afișează meniul pentru studenți.
        Verifică dacă lista e goală și blochează operațiunile (ștergere, etc.) dacă e cazul.
        """
        while True:
            print("\n  --- Gestiune Studenți ---")
            print("  1. Adaugă student")
            print("  2. Șterge student")
            print("  3. Modifică student")
            print("  4. Caută student după ID")
            print("  5. Afișează toți studenții")
            print("  6. Afișează numărul de studenți")
            print("  0. Revenire la meniul principal")
            print("  -------------------------")

            operatie = input("  Alegeți sub-opțiunea: ").strip()

            is_empty = (self.__ctrl_studenti.get_numar_studenti() == 0)

            if operatie == "1":
                self.__ui_add_student()
            elif operatie == "2":
                if is_empty:
                    print("  EROARE: Nu există studenți în listă. Nu se poate șterge.")
                else:
                    self.__ui_delete_student()
            elif operatie == "3":
                if is_empty:
                    print("  EROARE: Nu există studenți în listă. Nu se poate modifica.")
                else:
                    self.__ui_update_student()
            elif operatie == "4":
                if is_empty:
                    print("  EROARE: Nu există studenți în listă. Nu se poate căuta.")
                else:
                    self.__ui_find_student_by_id()
            elif operatie == "5":
                self.__ui_get_all_studenti()
            elif operatie == "6":
                print(f"  Număr total studenți: {self.__ctrl_studenti.get_numar_studenti()}")
            elif operatie == "0":
                return
            else:
                print("  Comandă invalidă!")

    # --- Meniu Probleme ---

    def __meniu_probleme(self):
        """
        Afișează meniul pentru probleme.
        Verifică dacă lista e goală și blochează operațiunile dacă e cazul.
        """
        while True:
            print("\n  --- Gestiune Probleme ---")
            print("  1. Adaugă problemă")
            print("  2. Șterge problemă")
            print("  3. Modifică problemă")
            print("  4. Caută problemă după ID")
            print("  5. Afișează toate problemele")
            print("  6. Afișează numărul de probleme")
            print("  0. Revenire la meniul principal")
            print("  -------------------------")

            operatie = input("  Alegeți sub-opțiunea: ").strip()

            is_empty = (self.__ctrl_probleme.get_numar_probleme() == 0)

            if operatie == "1":
                self.__ui_add_problema()
            elif operatie == "2":
                if is_empty:
                    print("  EROARE: Nu există probleme în listă. Nu se poate șterge.")
                else:
                    self.__ui_delete_problema()
            elif operatie == "3":
                if is_empty:
                    print("  EROARE: Nu există probleme în listă. Nu se poate modifica.")
                else:
                    self.__ui_update_problema()
            elif operatie == "4":
                if is_empty:
                    print("  EROARE: Nu există probleme în listă. Nu se poate căuta.")
                else:
                    self.__ui_find_problema_by_id()
            elif operatie == "5":
                self.__ui_get_all_probleme()
            elif operatie == "6":
                print(f"  Număr total probleme: {self.__ctrl_probleme.get_numar_probleme()}")
            elif operatie == "0":
                return
            else:
                print("  Comandă invalidă!")

    # --- Funcții UI Probleme ---

    def __ui_add_problema(self):
        """
        Cere datele pentru o problemă nouă și o adaugă.
        Prinde erorile de tastare sau dacă ID-ul există deja.
        """
        try:
            nrLab_nrProb = input("  Introduceți numărul (ex: '7_2'): ").strip()
            descriere = input("  Introduceți descrierea: ").strip()
            deadline = input("  Introduceți deadline-ul (ex: 's10'): ").strip()

            self.__ctrl_probleme.add_problema(nrLab_nrProb, descriere, deadline)
            print("  Problemă adăugată cu succes!")
        except ValidError as ve:
            print(f"  Eroare de Validare:\n{ve}")
        except RepoError as re:
            print(f"  Eroare de Stocare:\n{re}")

    def __ui_get_all_probleme(self):
        """Afișează toate problemele. Anunță dacă lista e goală."""
        probleme = self.__ctrl_probleme.get_all_probleme()
        if len(probleme) == 0:
            print("  Nu există probleme în listă.")
            return

        print("  --- Lista de Probleme ---")
        for problema in probleme:
            print(f"  {problema}")

    # --- Funcții UI Probleme ---

    def __ui_delete_problema(self):
        """
        Cere un ID de problemă până e valid sau anulezi ('0'). Apoi o șterge.
        Anunță dacă ID-ul nu există și cere din nou.
        """
        while True:
            try:
                id_str = input("  Introduceți ID-ul problemei de șters (ex: '7_2') (sau '0' pentru a anula): ").strip()

                if id_str == '0':
                    print("  Operație anulată.")
                    break

                # 2. Încercăm să apelăm controller-ul
                self.__ctrl_probleme.delete_problema(id_str)

                # 3. Dacă ajungem aici, totul a fost bine
                print("  Problemă ștersă cu succes!")
                break

            except RepoError as re:
                # Aici prindem InexistentIDError
                print(f"  EROARE: {re}. Încercați din nou.")
            # Bucla se reia automat dacă s-a prins o eroare

    def __ui_find_problema_by_id(self):
        """
        Cere un ID de problemă până e valid sau anulezi ('0').
        Apoi o găsește și o afișează.
        """
        while True:
            try:
                id_str = input("  Introduceți ID-ul problemei căutate (ex: '7_2') (sau '0' pentru a anula): ").strip()

                if id_str == '0':
                    print("  Operație anulată.")
                    break

                problema = self.__ctrl_probleme.find_problema_by_id(id_str)
                print(f"  Problemă găsită: {problema}")
                break  # Am găsit, ieșim

            except RepoError as re:  # Prinde InexistentIDError
                print(f"  EROARE: {re}. Încercați din nou.")

    def __ui_update_problema(self):
        """
        Actualizează o problemă.
        Pas 1: Cere un ID valid (sau anulezi).
        Pas 2: Cere datele noi. Prinde erorile și cere din nou.
        """
        # Pasul 1: Obținem un ID valid
        while True:
            try:
                id_str = input(
                    "  Introduceți ID-ul problemei de modificat (ex: '7_2') (sau '0' pentru a anula): ").strip()

                if id_str == '0':
                    print("  Operație anulată.")
                    return  # Ieșim de tot din funcție

                # Încercăm să GĂSIM problema
                problema_gasita = self.__ctrl_probleme.find_problema_by_id(id_str)

                print(f"  Problemă găsită: {problema_gasita}. Introduceți noile date mai jos.")
                break

            except RepoError as re:  # Prinde InexistentIDError
                print(f"  EROARE: {re}. Încercați din nou.")

        # Pasul 2: Obținem date noi VALIDE
        while True:
            try:
                descriere_noua = input(f"  Introduceți noua descriere (actual: {problema_gasita.descriere}): ").strip()
                deadline_nou = input(f"  Introduceți noul deadline (actual: {problema_gasita.deadline}): ").strip()

                if descriere_noua == "":
                    descriere_noua = problema_gasita.descriere

                if deadline_nou == "":
                    deadline_nou = problema_gasita.deadline

                # Încercăm să facem actualizarea
                self.__ctrl_probleme.update_problema(id_str, descriere_noua, deadline_nou)

                print("  Problemă modificată cu succes!")
                break

            except ValidError as ve:  # Prindem erorile de la Validator (ex: descriere goală)
                print(f"  Eroare de Validare:\n{ve}\n  Încercați din nou.")

    def __ui_add_student(self):
        """
        Cere datele pentru un student nou și îl adaugă.
        Prinde erorile (dacă ID-ul nu e număr sau dacă există deja).
        """
        try:
            studentID = int(input("  Introduceți ID-ul studentului: ").strip())
            nume = input("  Introduceți numele studentului: ").strip()
            grup = int(input("  Introduceți grupa studentului: ").strip())

            self.__ctrl_studenti.add_student(studentID, nume, grup)
            print("  Student adăugat cu succes!")

        except ValueError:
            print("Eroare UI: ID-ul și grupa trebuie să fie numere întregi.")
        except ValidError as ve:
            print(f"Eroare de Validare:\n{ve}")
        except RepoError as re:
            print(f"Eroare de Stocare:\n{re}")
        except Exception as e:
            print(f"A apărut o eroare neașteptată: {e}")

    def __ui_get_all_studenti(self):
        """Afișează toți studenții. Anunță dacă lista e goală."""
        studenti = self.__ctrl_studenti.get_all_students()
        if len(studenti) == 0:
            print("  Nu există studenți în listă.")
            return

        print("  --- Lista de Studenți ---")
        for student in studenti:
            print(f"  {student}")

    def __ui_delete_student(self):
        """
        Cere un ID de student până e valid sau anulezi ('0'). Apoi îl șterge.
        Anunță dacă ID-ul nu există sau nu e număr și cere din nou.
        """
        while True:
            try:
                id_str = input("  Introduceți ID-ul studentului de șters (sau '0' pentru a anula): ").strip()
                if id_str == '0':
                    print("  Operație anulată.")
                    break
                studentID = int(id_str)
                self.__ctrl_studenti.delete_student(studentID)
                print("  Student șters cu succes!")
                break
            except ValueError:
                print("  EROARE: ID-ul trebuie să fie un număr întreg. Încercați din nou.")
            except RepoError as re:
                print(f"  EROARE: {re}. Încercați din nou.")

    def __ui_update_student(self):
        """
        Actualizează un student.
        Pas 1: Cere un ID valid (sau anulezi).
        Pas 2: Cere datele noi. Prinde erorile și cere din nou.
        """
        while True:
            try:
                id_str = input("  Introduceți ID-ul studentului de modificat (sau '0' pentru a anula): ").strip()
                if id_str == '0':
                    print("  Operație anulată.")
                    return
                studentID = int(id_str)
                student_gasit = self.__ctrl_studenti.find_student_by_id(studentID)
                print(f"  Student găsit: {student_gasit}. Introduceți noile date mai jos.")
                break
            except ValueError:
                print("  EROARE: ID-ul trebuie să fie un număr întreg. Încercați din nou.")
            except RepoError as re:
                print(f"  EROARE: {re}. Încercați din nou.")

        while True:
            try:
                nume_nou = input(f"  Introduceți noul nume (actual: {student_gasit.nume}): ").strip()
                grup_nou_str = input(f"  Introduceți noua grupă (actual: {student_gasit.grup}): ").strip()

                if grup_nou_str == "":
                    grup_nou = student_gasit.grup
                else:
                    grup_nou = int(grup_nou_str)
                if nume_nou == "":
                    nume_nou = student_gasit.nume

                self.__ctrl_studenti.update_student(studentID, nume_nou, grup_nou)
                print("  Student modificat cu succes!")
                break
            except ValueError:
                print("  EROARE: Grupa trebuie să fie un număr întreg. Încercați din nou.")
            except ValidError as ve:
                print(f"  Eroare de Validare:\n{ve}\n  Încercați din nou.")

    def __ui_find_student_by_id(self):
        """
        Cere un ID de student până e valid sau anulezi ('0').
        Apoi îl găsește și îl afișează.
        """
        while True:
            try:
                id_str = input("  Introduceți ID-ul studentului căutat (sau '0' pentru a anula): ").strip()
                if id_str == '0':
                    print("  Operație anulată.")
                    break
                studentID = int(id_str)
                student = self.__ctrl_studenti.find_student_by_id(studentID)
                print(f"  Student găsit: {student}")
                break
            except ValueError:
                print("  EROARE: ID-ul trebuie să fie un număr întreg. Încercați din nou.")
            except RepoError as re:
                print(f"  EROARE: {re}. Încercați din nou.")
