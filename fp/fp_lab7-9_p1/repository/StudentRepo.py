'''
Created on Nov 10, 2014

@author: horatiu
'''
from domain.Student import Student

def test_store():
    s1 = Student(1, "miclaus")
    rep = StudentRepo()
    rep.store(s1)
    assert len(rep.getAll()) == 1
    assert s1 == rep.getAll()[0]
    s2 = Student(1, 'berila')
    try:
        rep.store(s2)
        assert False
    except ValueError:
        assert True

def test_remove():
    s1 = Student(1, "berila")
    rep = StudentRepo()
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
    rep = StudentRepo()
    assert len(rep.getAll()) == 0
    rep.store(Student(1, 'nume'))
    assert len(rep.getAll()) == 1
    rep.store(Student(2, 'nume2'))
    assert len(rep.getAll()) == 2
    assert rep.getAll()[0].getId() == 1

def test_find():
    rep = StudentRepo()
    rep.store(Student(1, 'nume'))
    rep.store(Student(2, 'nume2'))
    assert rep.find(1) == Student(1, 'nume')
    assert rep.find(2) == Student(2, 'nume2')
    try:
        rep.fund(3)
        assert False
    except:
        assert True

class StudentRepo():
    """
    Repository pentru student
    In aceasta clasa se stocheaza obiecte de tip Student
    """
    def __init__(self):
        self.__lst = []
    def getAll(self):
        """
        Functia returneaza o lista cu toti studentii din lista
        """
        return self.__lst
    def store(self, stud):
        """
        Functia stocheaza un nou student in lista
        param:
        stud: studentul de adaugat
        Arunca ValueError daca studentul exista deja in lista
        """
        if stud in self.__lst:
            raise ValueError('Studentul exista deja')
        self.__lst.append(stud)
    def remove(self, ID):
        """
        Functia sterge un student din lista
        param:
        ID: id-ul studentului care va fi sters
        Arunca ValueError daca studentul nu exista
        """
        i = 0;
        for i in range(0, len(self.__lst)):
            if self.__lst[i].getId() == ID:
                self.__lst.pop(i)
                return
        raise ValueError("Nu exista studentul")
    def find(self, ID):
        """
        Functia cauta si returneaza studentul cu id-ul ID
        """
        for stud in self.__lst:
            if stud.getId() == ID:
                return stud
        raise ValueError('Student inexistent')
    
test_store()
test_remove()
test_getAll()
test_find()