'''
Created on Nov 23, 2014

@author: horatiu
'''

class Mark():
    def __init__(self, studentId, subjectId, mark):
        self.__studId = studentId
        self.__subjId = subjectId
        self.__mark = mark
    def getStudentId(self):
        return self.__studId
    def getSubjectId(self):
        return self.__subjId
    def getMark(self):
        return self.__mark
    def setMark(self, newMark):
        self.__mark = newMark
    def __eq__(self, ot):
        return (self.__studId == ot.__studId and
                self.__subjId == ot.__subjId)
    
def test_getters():
    mark = Mark(1, 2, 9)
    assert mark.getStudentId() == 1
    assert mark.getSubjectId() == 2
    assert mark.getMark() == 9

test_getters()