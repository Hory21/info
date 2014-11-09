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
        return self.__ID + ' ' + self.__name