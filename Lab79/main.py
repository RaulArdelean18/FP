from Lab79.domain.validators import StudentValidator, ProblemaValidator
from Lab79.repository.repository import Repository
from Lab79.controller.controllers import StudentController, ProblemaController
from Lab79.ui.console import ConsoleUI


print("Aplicația pornește...")


validator_student = StudentValidator()
validator_problema = ProblemaValidator()

repo_studenti = Repository()
repo_probleme = Repository()

controller_studenti = StudentController(repo_studenti, validator_student)
controller_probleme = ProblemaController(repo_probleme, validator_problema)

ui = ConsoleUI(controller_studenti, controller_probleme)

ui.run()

print("Aplicația s-a oprit.")