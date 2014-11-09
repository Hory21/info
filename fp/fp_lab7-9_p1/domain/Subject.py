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
        return self.__ID + ' ' + self.__name + ' (prof: ' + self.__prof + ')'