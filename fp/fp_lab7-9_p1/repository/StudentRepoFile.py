'''
Created on Dec 2, 2014

@author: horatiu
'''
from repository.StudentRepo import StudentRepo
from domain.Student import Student

class StudentRepoFile(StudentRepo):
    def __init__(self, fileName):
        StudentRepo.__init__(self)
        self.__fileName = fileName
        try:
            f =open(self.__fileName, 'r')
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
                obj = Student(int(atributes[0]), atributes[1][:-1])
                StudentRepo.store(self, obj)
        file.close()
    def __storeFile(self):
        file = open(self.__fileName, 'w')
        for obj in StudentRepo.getAll(self):
            file.write(str(obj.getId()) + ' ' + obj.getName() + '\n')
        file.close()
    def store(self, stud):
        StudentRepo.store(self, stud)
        self.__storeFile()
    def remove(self, ID):
        StudentRepo.remove(self, ID)
        self.__storeFile()