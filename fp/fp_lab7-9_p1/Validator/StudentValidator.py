'''
Created on Nov 10, 2014

@author: horatiu
'''
from domain.Student import Student


class StudentValidator():
    """
    Clasa se ocupa cu validarea obiectelor de tip Student
    """
    def __init__(self):
        pass
    def validate(self, stud):
        """
        Functia valideaza un student
        param:
        stud: studentul care va fi validat
        Arunca ValueError daca studentul nu este valid
        """
        errors = []
        if (len(stud.getName()) == 0):
            errors.append('Numele studentului nu poate fi vid')
        if (stud.getId() < 0):
            errors.append('Id-ul studentului nu poate fi negativ')
        if (len(errors) != 0):
            raise ValueError(errors)


def test_validate():
    s1 = Student(1, '')
    s2 = Student(-2, 'semafor')
    s3 = Student(2, 'cascaval')
    val = StudentValidator()
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