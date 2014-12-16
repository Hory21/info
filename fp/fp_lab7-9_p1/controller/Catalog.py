'''
Created on Nov 11, 2014

@author: horatiu
'''
from repository.StudentRepo import StudentRepo
from Validator.StudentValidator import StudentValidator
from domain.Student import Student
from repository.SubjectRepo import SubjectRepo
from Validator.SubjectValidator import SubjectValidator
from domain.Subject import Subject


class Catalog():
    """
    clasa controller pentru studenti si discipline
    """
    def __init__(self, studValidator, studRepo, subjValidator, subjRepo):
        """
        constructor (functia initializeaza obiectele din clasa Catalog)
        param:
        studValidator: validator pentru student
        studRepo: repository pentru student
        subjValidator: validator pentru materie
        subjRepo: repository pentru materie
        """
        self.__studValidator = studValidator
        self.__studRepo = studRepo
        self.__subjValidator = subjValidator
        self.__subjRepo = subjRepo    
    def addStudent(self, ID, name):
        """
        Functia adauga un nou student (cu id-ul ID, numele name) in repository
        param:
        ID: id-ul studentului ce urmeaza sa fie adaugat
        name: numele studentului ce urmeaza sa fie adaugat
        """
        st = Student(ID, name)
        self.__studValidator.validate(st)
        self.__studRepo.store(st)
    def getAllStudents(self):
        """
        Functia returneaza lista tuturor studentilor
        """
        return self.__studRepo.getAll()
    def addSubject(self, ID, name, prof):
        """
        Functia adauga o noua disciplina (cu id-ul ID, numele name,
        si profesorul prof) in repository
        param:
        ID: id-ul disciplinei ce urmeaza sa fie adaugata
        name: numele disciplinei ce urmeaza sa fie adaugata
        prof: numele profesorului care preda disciplina
        """
        su = Subject(ID, name, prof)
        self.__subjValidator.validate(su)
        self.__subjRepo.store(su)
    def getAllSubjects(self):
        """
        Functia returneaza lista tuturor disciplinelor
        """
        return self.__subjRepo.getAll()
    def removeSubject(self, ID):
        """
        Functia sterge o materie
        param:
        ID: id-ul materiei ce va fi sterse
        """
        self.__subjRepo.remove(ID)
    def removeStudent(self, ID):
        """
        Functia sterge un student
        param:
        ID: id-ul studentului ce va fi sters
        """
        self.__studRepo.remove(ID)
    def modifyStudent(self, ID, newName):
        stud = self.__studRepo.find(ID)
        newStud = Student(ID, newName);
        self.__studValidator.validate(newStud)
        stud.setName(newName)
    def modifySubject(self, ID, newName, newProf):
        subj = self.__subjRepo.find(ID)
        newSubj = Subject(ID, newName, newProf);
        self.__subjValidator.validate(newSubj)
        subj.setName(newName)
        subj.setProf(newProf)
    def findStudent(self, ID):
        return self.__studRepo.find(ID)
    def findSubject(self, ID):
        return self.__subjRepo.find(ID)

def test_modifyStudent():
    repo = StudentRepo()
    val = StudentValidator()
    cat = Catalog(val, repo, None, None)
    cat.addStudent(666, 'Branza')
    cat.modifyStudent(666, 'Cascaval')
    assert cat.getAllStudents()[0].getName() == 'Cascaval'
    try:
        cat.modifyStudent(666, '')
        assert False
    except:
        assert True
    
def test_modifySubject():
    repo = SubjectRepo()
    val = SubjectValidator()
    cat = Catalog(None, None, val, repo)
    cat.addSubject(666, 'Branza', 'prof')
    cat.modifySubject(666, 'Cascaval', 'alt prof')
    assert cat.getAllSubjects()[0].getName() == 'Cascaval'
    assert cat.getAllSubjects()[0].getProf() == 'alt prof'
    try:
        cat.modifySubject(666, '', 'tralala')
        assert False
    except:
        assert True
    
def test_addSubject():
    repo = SubjectRepo()
    val = SubjectValidator()
    cat = Catalog(None, None, val, repo)
    cat.addSubject(666, '3d', 'stanila')
    assert len(cat.getAllSubjects()) == 1
    try:
        cat.addSubject(4, 'sdf', '')
        assert False
    except:
        assert True
    try:
        cat.addStudent(-23, 'minusdouasitrei', 'dfsdf')
        assert False
    except:
        assert True  

def test_addStudent():
    repo = StudentRepo()
    val = StudentValidator()
    cat = Catalog(val, repo, None, None)
    cat.addStudent(666, 'Branza')
    assert len(cat.getAllStudents()) == 1
    try:
        cat.addStudent(4, '')
        assert False
    except:
        assert True
    try:
        cat.addStudent(-23, 'minusdouasitrei')
        assert False
    except:
        assert True

test_addStudent()
test_addSubject()
test_modifyStudent()
test_modifySubject()