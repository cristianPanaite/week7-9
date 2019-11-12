from exceptii.exceptii import RepoError

class Repo:
    
    def __init__(self):
        self.__items = []
    
    def size(self):
        return len(self.__items)
        
    def adauga(self, item):
        if item in self.__items:
            raise RepoError("id deja existent!\n")
        self.__items.append(item)

    
    def cauta(self, item):
        if item not in self.__items:
            raise RepoError("id inexistent")
        for x in self.__items:
            if x == item:
                return x
    
    def modifica(self, item, change):
        item = self.cauta(item)
        self.delete(item)
        item.set_nume(change)
        self.adauga(item)
    
    def modifica_materie(self, item, change):
        item = self.cauta(item)
        self.delete(item)
        item.set_materie(change)
        self.adauga(item)
        
    def get_all(self):
        return self.__items[:]

    
    def delete(self, item):
        if item not in self.__items:
            raise RepoError("id inexistent")
        index = -1
        for i in range(len(self.__items)):
            if self.__items[i] == item:
                index = i
                break
        del self.__items[index]
        
        
    
    
    
    
    
    
