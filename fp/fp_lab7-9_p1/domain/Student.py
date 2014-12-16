'''
Created on Nov 8, 2014

@author: horatiu
'''
class Student():
    def __init__(self, ID, name):
        self.__ID = ID
        self.__name = name
    def getId(self):
        return self.__ID
    def getName(self):
        return self.__name
    def setId(self, ID):
        self.__ID = ID
    def setName(self, name):
        self.__name = name
    def __eq__(self, ot):
        return self.__ID == ot.__ID
    def __str__(self):
        return str(self.__ID) + ' ' + self.__name
    
def test_getters():
    s1 = Student(1, 'adga')
    s2 = Student(100, 'jth')
    assert s1.getId() == 1
    assert s2.getId() == 100
    assert s1.getName() == 'adga'
    assert s2.getName() == 'jth'

def test_setters():
    s1 = Student(1, 'adga')
    s1.setId(5)
    s1.setName('abcd')
    assert s1.getId() == 5
    assert s1.getName() == 'abcd'

test_getters()
test_setters()