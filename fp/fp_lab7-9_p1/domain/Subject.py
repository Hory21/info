'''
Created on Nov 8, 2014

@author: horatiu
'''

class Subject():
    def __init__(self, ID, name, prof):
        self.__ID = ID
        self.__name = name
        self.__prof = prof
    def getId(self):
        return self.__ID
    def getName(self):
        return self.__name
    def getProf(self):
        return self.__prof
    def setId(self, ID):
        self.__ID = ID
    def setName(self, name):
        self.__name = name
    def setProf(self, prof):
        self.__prof = prof
    def __eq__(self, ot):
        return self.__ID == ot.__ID
    def __str__(self):
        return str(self.__ID) + ' ' + self.__name + ' (prof: ' + self.__prof + ')'
    
def test_getters():
    s1 = Subject(1, 'adga', 'aaaa')
    s2 = Subject(100, 'jth', 'bbbb')
    assert s1.getId() == 1
    assert s2.getId() == 100
    assert s1.getName() == 'adga'
    assert s2.getName() == 'jth'
    assert s1.getProf() == 'aaaa'
    assert s2.getProf() == 'bbbb'

def test_setters():
    s1 = Subject(1, 'adga', 'aaaa')
    s1.setId(5)
    s1.setName('abcd')
    s1.setProf('jjjj')
    assert s1.getId() == 5
    assert s1.getName() == 'abcd'
    assert s1.getProf() == 'jjjj'

test_getters()
test_setters()