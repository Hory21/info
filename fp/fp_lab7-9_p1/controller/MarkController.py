'''
Created on Nov 23, 2014

@author: horatiu
'''
from domain.Mark import Mark
from repository.MarkRepo import MarkRepo
from repository.StudentRepo import StudentRepo
from repository.SubjectRepo import SubjectRepo
from Validator.MarkValidator import MarkValidator
from domain.Student import Student
from domain.Subject import Subject


class StudMarkDTO(object):
    def __init__(self, studentName, mark):
        self.__studentName = studentName
        self.__mark = mark
    def __str__(self):
        return (self.__studentName + ' ' + str(self.__mark))


class StudAverageDTO(object):
    def __init__(self, studentName, average):
        self.__studentName = studentName
        self.__average = average
    def __str__(self):
        return (self.__studentName + ' ' + str(self.__average))
    def getAverage(self):
        return self.__average


class MarkController:
    """
    Clasa controller pentru note
    """
    def __init__(self, markValidator, markRepo, studRepo, subjRepo):
        """
        constructor (functia initializeaza obiectele din clasa MarkController)
        param:
        markValidator: validator pentru note
        markRepo: repository pentru nota
        studRepo: repository pentru student
        subjRepo: repository pentru materie
        """
        self.__markValidator = markValidator
        self.__markRepo = markRepo
        self.__studRepo = studRepo
        self.__subjRepo = subjRepo
    def addMark(self, idStud, idSubj, mark):
        """
        Functia adauga nota mark unui student (cu id-ul idStud) la o
        materie (cu id-ul idSubj)
        """
        self.__studRepo.find(idStud)
        self.__subjRepo.find(idSubj)
        mk = Mark(idStud, idSubj, mark)
        self.__markValidator.validate(mk)
        self.__markRepo.store(mk)
    def getAll(self):
        """
        Functia returneaza o lista de obiecte de tip Mark
        """
        return self.__markRepo.getAll()
    def getStudSubjList(self, idSubj):
        """
        Functia construieste o lista de obiecte de tip StudMarkDTO
        returneaza: o lista cu obiecte de tip StudMarkDTO, ordonata alfabetic
            dupa numele studentilor
        idSubj: id-ul materiei ai carei studenti si ale carei note se cauta
        """
        lstdto = []
        lst = sorted(self.__markRepo.getAllForSubject(idSubj),
                     key = lambda mk : self.__studRepo.find(mk.getStudentId()).getName())
        for m in lst:
            dto = StudMarkDTO(self.__studRepo.find(m.getStudentId()).getName(),
                              m.getMark())
            lstdto.append(dto)
        return lstdto
    def getStudAverageList(self):
        """
        Functia returneaza primii 20% din studenti in functie de media tuturor notelor
        returneaza: o lista de obiecte de tip StudAverageDTO
            ordonata dupa numele studentilor
        """
        studLst = self.__studRepo.getAll()
        dtolst = []
        for stud in studLst:
            markSum = 0
            markCount = 0
            markLst = self.__markRepo.getAllForStudent(stud.getId())
            for mark in markLst:
                markSum += mark.getMark()
                markCount += 1
            if markCount == 0:
                continue
            dto = StudAverageDTO(stud.getName(), markSum / markCount)
            dtolst.append(dto)
        dtolst = sorted(dtolst, key = lambda dto : dto.getAverage(), reverse = True)
        n = round(len(dtolst) / 5)
        if n < 1:
            n = 1
        else:
            n = int(n)
        return dtolst[0:n]
        
def test_getStudAverageList():
    markRepo = MarkRepo()
    markVal = MarkValidator()
    studRepo = StudentRepo()
    studRepo.store(Student(1, 'gigel'))
    subjRepo = SubjectRepo()
    subjRepo.store(Subject(1, 'materie', 'profesor'))
    subjRepo.store(Subject(2, 'materie2', 'profesor2'))
    mc = MarkController(markVal, markRepo, studRepo, subjRepo)
    mc.addMark(1, 2, 10)
    mc.addMark(1, 1, 8)
    assert  len(mc.getStudAverageList()) == 1

def test_addMark():
    markRepo = MarkRepo()
    markVal = MarkValidator()
    studRepo = StudentRepo()
    studRepo.store(Student(1, 'gigel'))
    subjRepo = SubjectRepo()
    subjRepo.store(Subject(2, 'materie', 'profesor'))
    mc = MarkController(markVal, markRepo, studRepo, subjRepo)
    mc.addMark(1, 2, 10)
    assert len(mc.getAll()) == 1
    try:
        mc.addMark(1, 2, 9)
        assert False
    except:
        assert True
    try:
        mc.addMark(3, 4, 5)
        assert False
    except:
        assert True

def test_getStudSubjList():
    markRepo = MarkRepo()
    markVal = MarkValidator()
    studRepo = StudentRepo()
    studRepo.store(Student(1, 'gigel'))
    subjRepo = SubjectRepo()
    subjRepo.store(Subject(2, 'materie', 'profesor'))
    mc = MarkController(markVal, markRepo, studRepo, subjRepo)
    mc.addMark(1, 2, 10)
    assert  len(mc.getStudSubjList(2)) == 1
     
    

test_addMark()
test_getStudSubjList()
test_getStudAverageList()