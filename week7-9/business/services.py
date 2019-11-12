from entitati.entitati import Student, Disciplina

class ServiceDisciplina:
    
    
    def __init__(self, repoDisciplina, validDisciplina):
        self.__repoDisciplina = repoDisciplina
        self.__validDisciplina = validDisciplina
    
    def adauga_disciplina(self, id_disc, materie, nume):
        disciplina = Disciplina(id_disc, materie, nume)
        self.__validDisciplina.valideaza_disciplina(disciplina)
        self.__repoDisciplina.adauga(disciplina)
        
    def modify_materie(self, d_id, materie_change):
        cheie = Disciplina(d_id, "NONE", "NONE")
        self.__validDisciplina.valideaza_disciplina(cheie)
        self.__repoDisciplina.modifica_materie(cheie, materie_change)
        
    def modify_nume(self, d_id, name_change):
        cheie = Disciplina(d_id, "NONE", "NONE")
        self.__validDisciplina.valideaza_disciplina(cheie)
        self.__repoDisciplina.modifica(cheie, name_change)
        
    def delete_disciplina(self, s_id):
        cheie = Disciplina(s_id, "NONE", "NONE")
        self.__validDisciplina.valideaza_disciplina(cheie)
        self.__repoDisciplina.delete(cheie)
    
    def caut_disciplina(self, d_id):
        cheie = Disciplina(d_id, None, None)
        self.__validDisciplina.valideaza_disciplina(cheie)
        return self.__repoDisciplina.cauta(cheie)
        
    def get_disciplines(self):
        return self.__repoDisciplina.get_all()
    


class ServiceNote:
    
    
    def __init__(self, repoNote, validNote):
        self.__repoNote = repoNote
        self.__validNote = validNote
    
    



class ServiceStudent:
    
    
    def __init__(self, repoStudent, validStudent):
        self.__repoStudent = repoStudent
        self.__validStudent = validStudent
    
    
    def adauga_stud(self, stud_id, nume):
        student = Student(stud_id, nume)
        self.__validStudent.valideaza_student(student)
        self.__repoStudent.adauga(student)
        
    def delete_student(self, stud_id):
        cheie = Student(stud_id, "None")
        self.__validStudent.valideaza_student(cheie)
        self.__repoStudent.delete(cheie)  
        
    def modify_student(self, s_id, nume_change):
        cheie = Student(s_id, "NONE")
        self.__validStudent.valideaza_student(cheie)
        self.__repoStudent.modifica(cheie, nume_change)    
        
    def cauta_student(self, s_id):
        cheie = Student(s_id, None)
        self.__validStudent.valideaza_student(cheie)
        return self.__repoStudent.cauta(cheie)
        
    def get_students(self):
        return self.__repoStudent.get_all()
        
        



