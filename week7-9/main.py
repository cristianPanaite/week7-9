from testing.teste import Teste
from infrastructura.repo import Repo
from validatoare.validare import ValidatorStudent, ValidatorDisciplina, ValidatorNote
from business.services import ServiceStudent, ServiceDisciplina, ServiceNote
from presentation.controller import Console

teste = Teste()
teste.run()
validStudent = ValidatorStudent()
validDisciplina = ValidatorDisciplina()
validNote = ValidatorNote()
repoStudent = Repo()
repoDisciplina = Repo()
repoNote = Repo()
srvStudent = ServiceStudent(repoStudent, validStudent)
srvDisciplina = ServiceDisciplina(repoDisciplina, validDisciplina)
srvNote = ServiceNote(repoNote, validNote)
ui = Console(srvStudent, srvDisciplina, srvNote)
ui.run()