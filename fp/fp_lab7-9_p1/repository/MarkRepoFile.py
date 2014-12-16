'''
Created on Dec 2, 2014

@author: horatiu
'''
from repository.MarkRepo import MarkRepo
from domain.Mark import Mark

class MarkRepoFile(MarkRepo):
    def __init__(self, fileName):
        MarkRepo.__init__(self)
        self.__fileName = fileName
        try:
            f = open(self.__fileName, 'r')
            f.close()
        except FileNotFoundError:
            f = open(self.__fileName, 'w')
            f.close()
        self.__loadFile()
    def __loadFile(self):
        file = open(self.__fileName, 'r')
        for line in file:
            if line != '\n':
                atributes = line.split(' ')
                obj = Mark(int(atributes[0]), int(atributes[1]), int(atributes[2][:-1]))
                MarkRepo.store(self, obj)
        file.close()
    def __storeFile(self):
        file = open(self.__fileName, 'w')
        for obj in MarkRepo.getAll(self):
            file.write(str(obj.getStudentId()) + ' ' + str(obj.getSubjectId())
                       + ' ' + str(obj.getMark()) + '\n')
        file.close()
    def store(self, mark):
        MarkRepo.store(self, mark)
        self.__storeFile()
    def remove(self, idStud, idSubj):
        MarkRepo.remove(self, idStud, idSubj)
        self.__storeFile()
        