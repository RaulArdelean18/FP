from Lab79.controller.controllers import ProblemaController
from Lab79.domain.exceptions import ProblemaValidError
from Lab79.domain.validators import ProblemaValidator
from Lab79.repository.repository import Repository


def test_controller_add_problema():
    """Testează funcția: ProblemaController.add_problema()"""
    repo_prob = Repository()
    val_prob = ProblemaValidator()
    ctrl_prob = ProblemaController(repo_prob, val_prob)

    # Cazul Bun
    ctrl_prob.add_problema("7_1", "Desc 1", "S10")
    assert ctrl_prob.get_numar_probleme() == 1

    # Cazul Rău (Validare)
    prins = False
    try:
        ctrl_prob.add_problema("7_2", "", "S10")  # Descriere goală
    except ProblemaValidError:
        prins = True
    assert prins, "EROARE [Ctrl-Prob]: Nu a prins eroarea de validare."
    assert ctrl_prob.get_numar_probleme() == 1  # Verifică că nu s-a adăugat