'''
Created on Nov 23, 2014

@author: horatiu
'''
from domain.Mark import Mark


class MarkValidator():
    """
    Clasa care se ocupa cu validatrea obiectelor de tip Mark
    """
    def validate(self, mark):
        """
        Functia valideaza note
        param:
        mark: obiectul de tip Mark care va fi validat
        Arunca ValueError in caz de eroare
        """
        lst = []
        if (mark.getMark() < 1 or mark.getMark() > 10):
            lst.append('Nota trebuie sa fie un numar de la 1 la 10')
        if (mark.getStudentId() < 0 or mark.getSubjectId() < 0):
            lst.append('Id-ul studentului si id-ul materiei trebuie sa fie numere pozitive')
        if (len(lst) > 0):
            raise ValueError(lst)


def test_validate():
    m1 = Mark(1, 2, 9)
    m2 = Mark(-2, 4, 6)
    m3 = Mark(2, 5, 11)
    m4 = Mark(2, 3, 0)
    val = MarkValidator()
    try:
        val.validate(m1)
        assert True
    except ValueError:
        assert False
    try:
        val.validate(m2)
        assert False
    except ValueError:
        assert True
    try:
        val.validate(m3)
        assert False
    except ValueError:
        assert True
    try:
        val.validate(m4)
        assert False
    except ValueError:
        assert True

test_validate()