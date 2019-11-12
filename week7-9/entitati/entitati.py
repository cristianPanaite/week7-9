class Student:

    
    def __init__(self, stud_id, nume):
        self.__stud_id = stud_id
        self.__nume = nume
        
    def get_id(self):
        return self.__stud_id
    
    def get_nume(self):
        return self.__nume
    
    def set_nume(self, value):
        self.__nume = value

    def __eq__(self, other):
        return self.__stud_id == other.__stud_id
        
    def __str__(self):
        return str(self.__stud_id) + " " + self.__nume



class Disciplina:

    
    def __init__(self, param1, param2, param3):
        self.__id = param1
        self.__materie = param2
        self.__nume = param3

    
    def get_id(self):
        return self.__id

    
    def get_materie(self):
        return self.__materie

    
    def get_nume(self):
        return self.__nume

    
    def set_materie(self, mat):
        self.__materie = mat

    
    def set_nume(self, nume):
        self.__nume = nume
        
    def __eq__(self, other):
        return self.__id == other.__id
    
    def __str__(self):
        return "{} {} {}".format(str(self.__id), self.__materie, self.__nume)
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    


