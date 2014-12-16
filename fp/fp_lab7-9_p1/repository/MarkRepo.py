'''
Created on Nov 23, 2014

@author: horatiu
'''
from domain.Mark import Mark

class MarkRepo():
    """
    Repository pentru note
    In aceasta clasa se stocheaza obiecte de tip Mark
    """
    def __init__(self):
        self.__lst = []
    def store(self, mark):
        """
        Functia stocheaza o noua nota lista
        param:
        mark: nota de adaugat
        Arunca ValueError daca nota exista deja in lista
        """
        if mark in self.__lst:
            raise ValueError('Nota exista deja')
        self.__lst.append(mark)
    def getAll(self):
        """
        Functia returneaza o lista cu toate notele
        """
        return self.__lst
    def remove(self, idStud, idSubj):
        """
        Functia sterge o nota din lista
        param:
        idStud: id-ul studentului a carui nota va fi stearsa
        idSubj: id-ul materiei de la care va fi stearsa nota
        Arunca ValueError daca nota nu exista
        """
        i = 0;
        for i in range(0, len(self.__lst)):
            if (self.__lst[i].getStudentId() == idStud and
                self.__lst[i].getSubjectId() == idSubj):
                self.__lst.pop(i)
                return
        raise ValueError("Nu exista nota")
    def getAllForSubject(self, Id):
        """
        Functia returneaza o lista cu toate notele la materia cu id-ul Id
        """
        rezlst = []
        for m in self.__lst:
            if m.getSubjectId() == Id:
                rezlst.append(m)
        return rezlst
    def getAllForStudent(self, studentId):
        """
        Functia returneaza o lista cu toate notele studentului cu id-ul studentId
        """
        rezlst = []
        for m in self.__lst:
            if m.getStudentId() == studentId:
                rezlst.append(m)
        return rezlst

def test_getAllForStudent():
    rep = MarkRepo()
    m1 = Mark(1, 2, 10)
    rep.store(m1)
    m2 = Mark(2, 2, 10)
    rep.store(m2)
    m3 = Mark(3, 2, 10)
    rep.store(m3)
    m4 = Mark(1, 6, 10)
    rep.store(m4)
    assert len(rep.getAllForStudent(2)) == 1
    assert len(rep.getAllForStudent(1)) == 2

def test_getAllForSubject():
    rep = MarkRepo()
    m1 = Mark(1, 2, 10)
    rep.store(m1)
    m2 = Mark(2, 2, 10)
    rep.store(m2)
    m3 = Mark(3, 2, 10)
    rep.store(m3)
    m4 = Mark(1, 6, 10)
    rep.store(m4)
    assert len(rep.getAllForSubject(2)) == 3
    assert len(rep.getAllForSubject(6)) == 1
    assert len(rep.getAllForSubject(5)) == 0
    

def test_store():
    m1 = Mark(1, 2, 10)
    rep = MarkRepo()
    rep.store(m1)
    assert len(rep.getAll()) == 1
    assert m1 == rep.getAll()[0]
    s2 = Mark(1, 2, 9)
    try:
        rep.store(s2)
        assert False
    except ValueError:
        assert True

def test_remove():
    m1 = Mark(1, 2, 5)
    rep = MarkRepo()
    rep.store(m1)
    rep.remove(1, 2)
    assert len(rep.getAll()) == 0
    rep.store(m1)
    try:
        rep.remove(2, 1)
        assert False
    except:
        assert True

def test_getAll():
    rep = MarkRepo()
    assert len(rep.getAll()) == 0
    rep.store(Mark(1, 2, 6))
    assert len(rep.getAll()) == 1
    rep.store(Mark(2, 2, 10))
    assert len(rep.getAll()) == 2
    assert rep.getAll()[0].getStudentId() == 1
    assert rep.getAll()[0].getSubjectId() == 2

test_store()
test_remove()
test_getAll()
test_getAllForSubject()
test_getAllForStudent()