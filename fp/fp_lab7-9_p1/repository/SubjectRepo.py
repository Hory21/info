'''
Created on Nov 10, 2014

@author: horatiu
'''
from domain.Subject import Subject

def test_store():
    s1 = Subject(1, "bere", "eu")
    rep = SubjectRepo()
    rep.store(s1)
    assert len(rep.getAll()) == 1
    assert s1 == rep.getAll()[0]
    s2 = Subject(1, 'mate', "profu' de mate")
    try:
        rep.store(s2)
        assert False
    except ValueError:
        assert True

def test_remove():
    s1 = Subject(1, "bere", "eu")
    rep = SubjectRepo()
    rep.store(s1)
    rep.remove(1)
    assert len(rep.getAll()) == 0
    rep.store(s1)
    try:
        rep.remove(2)
        assert False
    except:
        assert True
        
def test_getAll():
    rep = SubjectRepo()
    assert len(rep.getAll()) == 0
    rep.store(Subject(1, 'nume', 'prof'))
    assert len(rep.getAll()) == 1
    rep.store(Subject(2, 'nume2', 'prof2'))
    assert len(rep.getAll()) == 2
    assert rep.getAll()[0].getId() == 1

def test_find():
    rep = SubjectRepo()
    rep.store(Subject(1, 'nume', 'prof'))
    rep.store(Subject(2, 'nume2', 'prof2'))
    assert rep.find(1) == Subject(1, 'nume', 'prof')
    assert rep.find(2) == Subject(2, 'nume2', 'prof2')
    try:
        rep.fund(3)
        assert False
    except:
        assert True

class SubjectRepo():
    """
    Repository pentru materie
    In aceasta clasa se stocheaza obiecte de tip Subject
    """
    def __init__(self):
        self.__lst = []
    def getAll(self):
        """
        Functia returneaza o lista cu toate materiile din lista
        """
        return self.__lst
    def store(self, subj):
        """
        Functia stocheaza o noua materie in lista
        param:
        subj: materia de adaugat
        Arunca ValueError daca materia exista deja in lista
        """
        if subj in self.__lst:
            raise ValueError('Disciplina exista deja')
        self.__lst.append(subj)
    def remove(self, ID):
        """
        Functia sterge o materie din lista
        param:
        ID: id-ul materiei care va fi stearsa
        Arunca ValueError daca materia nu exista
        """
        i = 0
        for i in range(0, len(self.__lst)):
            if self.__lst[i].getId() == ID:
                self.__lst.pop(i)
                return
        raise ValueError("Nu exista disciplina")
    def find(self, ID):
        for sub in self.__lst:
            if sub.getId() == ID:
                return sub
        raise ValueError('Materie inexistenta')
    
    

test_store()
test_remove()
test_getAll()
test_find()