from entitati.entitati import Student, Disciplina
from validatoare.validare import ValidatorStudent, ValidatorDisciplina
from exceptii.exceptii import ValidError, RepoError
from infrastructura.repo import Repo

class Teste:
    
    
    def __init__(self):
        pass

    
    def creaza_student(self):
        st_id = 5
        st_name = "Hamsie"
        student = Student(st_id, st_name)
        
        assert student.get_id() == st_id
        assert student.get_nume() == st_name
        
        student.set_nume("Ricardo")
        assert student.get_nume() == "Ricardo"
        
        student2 = Student(5, "hail")
        assert student == student2
    
    
    def valideaza_student(self):
        studValid = Student(25, "Japonia")
        stud_id_invalid = Student(-5, "grecia")
        stud_nume_invalid = Student(5, "")
        studInvalid = Student(-5, "")
        validStud = ValidatorStudent()
        
        validStud.valideaza_student(studValid)
        try:
            validStud.valideaza_student(stud_id_invalid)
            assert False
        except ValidError as ve:
            assert str(ve) == "id invalid!\n"
            
        try:
            validStud.valideaza_student(stud_nume_invalid)
            assert False
        except ValidError as ve:
            assert str(ve) ==  "nume invalid!\n"
            
        try:
            validStud.valideaza_student(studInvalid)
            assert False
        except ValidError as ve:
            assert str(ve) == "id invalid!\nnume invalid!\n"
    
    def repo_adauga_student(self):
        student = Student(25, "laris")
        repo_stud = Repo()
        assert repo_stud.size() == 0
        repo_stud.adauga(student)
        assert repo_stud.size() == 1
        student = Student(25, "lala")
        try:
            repo_stud.adauga(student)
            assert False
        except RepoError as re:
            assert str(re) == "id deja existent!\n"
        
    def modifica_student(self):
        student = Student(25, "laris")
        repo_stud = Repo()
        repo_stud.adauga(student)
        nume_change = "Andrei"
        cheie_stud = Student(24, None)
        try: 
            repo_stud.cauta(cheie_stud)
            assert False
        except RepoError as re:
            assert str(re) == "id inexistent"
        cheie_stud = Student(25, None)
        stud_gasit = repo_stud.cauta(cheie_stud)
        repo_stud.modifica(stud_gasit, nume_change)
        assert repo_stud.cauta(stud_gasit).get_nume() == nume_change
            
        
    def repo_delete_student(self):
        student = Student(25, "andrei")
        repo = Repo()
        
        repo.adauga(student)
        assert repo.size() == 1
        cheie_student = Student(24, None)
        try:
            repo.delete(cheie_student)
            assert False
        except RepoError as re:
            assert str(re) == "id inexistent"
            
        cheie_student = Student(25, None)
        repo.delete(cheie_student)
        assert repo.size() == 0
    

    def caut_stud(self):
        student = Student(1, "Andrei")
        repo = Repo()
        
        repo.adauga(student)
        cheie = Student(2, None)
        
        try:
            repo.cauta(cheie)
            assert False
        except RepoError as re:
            assert str(re) == "id inexistent"
        cheie = Student(1, None)
        gasit = repo.cauta(cheie)
        assert gasit.get_id() == 1
        assert gasit.get_nume() == "Andrei"
    
    
    def run_teste_studenti(self):
        
        self.creaza_student()
        self.valideaza_student()
        self.repo_adauga_student()
        self.modifica_student()
        self.repo_delete_student()
        self.caut_stud()
    
    
    
    def creeaza_disciplina(self):
        dis1 = Disciplina(1, "Mate", "stoica")
        
        assert dis1.get_id() == 1
        assert dis1.get_materie() == "Mate"
        assert dis1.get_nume() == "stoica"
        
        dis1.set_materie("Info")
        assert dis1.get_materie() == "Info"
        
        dis1.set_nume("Gabi")
        assert dis1.get_nume() == "Gabi"
        
        dis2 = Disciplina(1, "info", "lala")
        
        assert dis1 == dis2
        
    
    
    def valideaza_disciplina(self):
        disValida = Disciplina(1, "Mate", "stoica")
        dis_id_invalid = Disciplina(-1, "mate", "stoica")
        dis_materie_invalida = Disciplina(1, "", "stoica")
        dis_nume_invalid = Disciplina(1, "mate", "")
        
        valid_disciplina = ValidatorDisciplina()
        
        valid_disciplina.valideaza_disciplina(disValida)
        try: 
            valid_disciplina.valideaza_disciplina(dis_id_invalid)
            assert False
        except ValidError as ve:
            assert str(ve) == "id invalid!\n"
        try: 
            valid_disciplina.valideaza_disciplina(dis_materie_invalida)
            assert False
        except ValidError as ve:
            assert str(ve) == "materie invalida!\n"
        try: 
            valid_disciplina.valideaza_disciplina(dis_nume_invalid)
            assert False
        except ValidError as ve:
            assert str(ve) == "nume invalid!\n"
            
        
    
    
    def repo_adauga_disciplina(self):
        disciplina = Disciplina(1, "mate", "berinde")
        repo = Repo()
        assert repo.size() == 0
        repo.adauga(disciplina)
        try:
            repo.adauga(disciplina)
            assert False
        except RepoError as re:
            assert str(re) == "id deja existent!\n"
    
    def repo_delete_disciplina(self):
        disciplina = Disciplina(25, "andrei", "romana")
        repo = Repo()
        
        repo.adauga(disciplina)
        assert repo.size() == 1
        cheie_disciplina = Disciplina(24, None, None)
        try:
            repo.delete(cheie_disciplina)
            assert False
        except RepoError as re:
            assert str(re) == "id inexistent"
            
        cheie_disciplina = Disciplina(25, None, None)
        repo.delete(cheie_disciplina)
        assert repo.size() == 0
    
    def modifica_disciplina(self):
        disciplina = Disciplina(25, "mate", "ladla")
        repo = Repo()
        repo.adauga(disciplina)
        nume_change = "Andrei"
        materie_change = "info"
        cheie_disciplina = Disciplina(24, None, None)
        try: 
            repo.cauta(cheie_disciplina)
            assert False
        except RepoError as re:
            assert str(re) == "id inexistent"
        cheie_disciplina = Disciplina(25, None, None)
        disciplina_gasita = repo.cauta(cheie_disciplina)
        repo.modifica(disciplina_gasita, nume_change)
        repo.modifica_materie(disciplina_gasita, materie_change)
        assert repo.cauta(disciplina_gasita).get_nume() == nume_change
        assert repo.cauta(disciplina_gasita).get_materie() == materie_change    


    def caut_disciplina(self):
        disciplina = Disciplina(25, "andrei", "romana")
        repo = Repo()
        
        repo.adauga(disciplina)
        cheie = Disciplina(23, "andrei", "romana")
        
        try:
            repo.cauta(cheie)
            assert False
        except RepoError as re:
            assert str(re) == "id inexistent"
        cheie = Disciplina(25, "andrei", "romana")
        gasit = repo.cauta(cheie)
        assert gasit.get_id() == 25
        assert gasit.get_nume() == "romana"
        assert gasit.get_materie() == "andrei"
    
    
    def run_teste_discipline(self):
        self.creeaza_disciplina()
        self.valideaza_disciplina()
        self.repo_adauga_disciplina()
        self.repo_delete_disciplina()
        self.modifica_disciplina()
        self.caut_disciplina()
    
    def run(self):
        self.run_teste_studenti()
        self.run_teste_discipline()
    
    



