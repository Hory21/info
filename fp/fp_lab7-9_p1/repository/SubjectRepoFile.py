'''
Created on Dec 2, 2014

@author: horatiu
'''
from repository.SubjectRepo import SubjectRepo
from domain.Subject import Subject

class SubjectRepoFile(SubjectRepo):
    def __init__(self, fileName):
        SubjectRepo.__init__(self)
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
                obj = Subject(int(atributes[0]), atributes[1], atributes[2][:-1])
                SubjectRepo.store(self, obj)
        file.close()
    def __storeFile(self):
        file = open(self.__fileName, 'w')
        for obj in SubjectRepo.getAll(self):
            file.write(str(obj.getId()) + ' ' + obj.getName()
                       + ' ' + obj.getProf() + '\n')
        file.close()
    def store(self, subj):
        SubjectRepo.store(self, subj)
        self.__storeFile()
    def remove(self, ID):
        SubjectRepo.remove(self, ID)
        self.__storeFile()