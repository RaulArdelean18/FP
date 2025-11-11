from Lab79.test.test_domain import *
from Lab79.test.test_repository import *
from Lab79.test.test_controller_student import *
from Lab79.test.test_controller_problema import *


def ruleaza_toate_testele():
    """
    Rulează manual toate testele definite și adunate în lista de mai jos.
    Afișează un raport detaliat pentru fiecare test și un sumar la final.
    """

    # Lista tuturor funcțiilor de test pe care vrem să le rulăm
    teste_de_rulat = [
        # Din test_domain.py
        test_student_validator_valideaza,
        test_problema_validator_valideaza,

        # Din test_repository.py
        test_repository_add_and_len,
        test_repository_get_all,
        test_repository_find_by_id,
        test_repository_delete,
        test_repository_update,

        # Din test_controller_student.py
        test_controller_add_student,
        test_controller_delete_student,
        test_controller_update_student,
        test_controller_find_student_by_id,
        test_controller_get_all_students,

        # Din test_controller_problema.py
        test_controller_add_problema
    ]

    numar_teste_rulate = 0
    numar_teste_esuate = 0

    print("--- Incepe rularea testelor ---")

    for test_functie in teste_de_rulat:
        test_nume = test_functie.__name__  # Aflăm numele funcției (ex: "test_repository_add_and_len")
        numar_teste_rulate += 1

        try:
            # Apelăm funcția de test
            test_functie()

            # Dacă ajunge aici, assert-urile au trecut
            print(f"  [PASSED] Testul '{test_nume}' a trecut.")

        except AssertionError as e:
            # Dacă un assert eșuează, afișăm eroarea
            numar_teste_esuate += 1
            print(f"  [FAILED] Testul '{test_nume}' a eșuat!")
            print(f"      -> Eroare: {e}")  # Afișăm eroarea dată de assert

        except Exception as e:
            # Afișăm și alte erori neașteptate (ex: eroare de import, eroare de logică)
            numar_teste_esuate += 1
            print(f"  [ERROR] Testul '{test_nume}' a produs o eroare neașteptată!")
            print(f"      -> Eroare: {e}")

    # --- Sumar final ---
    print("\n--- Sumar teste ---")
    print(f"Teste rulate: {numar_teste_rulate}")
    print(f"Teste eșuate: {numar_teste_esuate}")

    if numar_teste_esuate == 0:
        print("\nFelicitări! Toate testele au trecut!")
    else:
        print(f"\nAtenție! {numar_teste_esuate} teste au eșuat.")


if __name__ == "__main__":
    ruleaza_toate_testele()
