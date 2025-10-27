from teste.test_utils import *
from teste.test_services import *


def ruleaza_toate_testele():
    """
    Ruleaza manual toate testele definite in directory-ul teste
    """
    # Lista tuturor functiilor de test pe care vrem sa le rulam
    teste_de_rulat = [
        # Din test_utils.py
        test_converteste_string_in_data,
        test_format_data_manual,

        # Din test_services.py
        test_adauga_pachet,
        test_modifica_pachet,
        verify,
        test_sterge_dupa_durata,
        test_sterge_dupa_destinatie,
        test_sterge_dupa_pret,
        test_cauta_dupa_interval,
        test_cauta_dupa_destinatie_si_pret,
        test_cauta_dupa_data_sfarsit,
        test_filtrare_oferte_dupa_pret_si_destinatie,
        test_filtrare_dupa_luna,
        test_raport_perioada_sortat_pret
    ]

    numar_teste_rulate = 0
    numar_teste_esuate = 0

    print("--- Incepe rularea testelor ---")

    for test_functie in teste_de_rulat:
        test_nume = test_functie.__name__  # Aflam numele functiei (ex: "test_adauga_pachet")
        numar_teste_rulate += 1
        try:
            # Apelam functia de test
            test_functie()

            # Daca ajunge aici, assert-urile au trecut
            print(f"[PASSED] Testul '{test_nume}' a trecut cu succes.")

        except AssertionError as e:
            # Daca un assert esueaza, afisam eroarea
            numar_teste_esuate += 1
            print(f"[FAILED] Testul '{test_nume}' a esuat!")
            print(f"   -> Eroare: {e}")  # Afisam eroarea data de assert
        except Exception as e:
            # Afisam si alte erori neasteptate (ex: KeyError, etc.)
            numar_teste_esuate += 1
            print(f"[ERROR] Testul '{test_nume}' a produs o eroare neasteptata!")
            print(f"   -> Eroare: {e}")

    # --- Sumar final ---
    print("\n--- Sumar teste ---")
    print(f"Teste rulate: {numar_teste_rulate}")
    print(f"Teste esuate: {numar_teste_esuate}")

    if numar_teste_esuate == 0:
        print("\nFelicitari! Toate testele au trecut! 🎉")
    else:
        print(f"\nAtentie! {numar_teste_esuate} teste au esuat. 😟")


if __name__ == "__main__":
    ruleaza_toate_testele()