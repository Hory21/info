'''
Created on Nov 17, 2014

@author: horatiu
'''
from domain.Subject import Subject

class SubjectValidator():
    """
    Clasa se ocupa cu validarea obiectelor de tip Subject
    """
    def __init__(self):
        pass
    def validate(self, sub):
        """
        Functia valideaza o materie
        param:
        sub: materia care va fi validat
        Arunca ValueError daca materia nu este valida
        """
        errors = []
        if (len(sub.getName()) == 0):
            errors.append('Numele materiei nu poate fi vid')
        if (sub.getId() < 0):
            errors.append('Id-ul materiei nu poate fi negativ')
        if (len(sub.getProf()) == 0):
            errors.append('Numele profesorului nu poate fi vid')
        if (len(errors) != 0):
            raise ValueError(errors)


def test_validate():
    s1 = Subject(1, '', 'sfsd')
    s2 = Subject(-2, 'abc', '')
    s3 = Subject(2, 'def', 'pac')
    val = SubjectValidator()
    try:
        val.validate(s1)
        assert False
    except ValueError:
        assert True
    try:
        val.validate(s2)
        assert False
    except ValueError:
        assert True
    try:
        val.validate(s3)
        assert True
    except ValueError:
        assert False

test_validate()