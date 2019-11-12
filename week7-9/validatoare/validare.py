from exceptii.exceptii import ValidError
class ValidatorDisciplina:
    def valideaza_disciplina(self, disc):
        errors = ""
        
        if disc.get_id() < 0:
            errors += "id invalid!\n"
        if disc.get_nume() == ""  :
            errors += "nume invalid!\n"
        if disc.get_materie() == "":
            errors += "materie invalida!\n"
        
        if len(errors) > 0:
            raise ValidError(errors)


class ValidatorNote:
    pass


class ValidatorStudent:
    
    def valideaza_student(self, stud):
        errors = ""
        
        if stud.get_id() < 0:
            errors += "id invalid!\n"
        if stud.get_nume() == ""  :
            errors += "nume invalid!\n"
        
        if len(errors) > 0:
            raise ValidError(errors)    



