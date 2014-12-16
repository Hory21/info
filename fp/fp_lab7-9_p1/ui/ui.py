'''
Created on Nov 11, 2014

@author: horatiu
'''

class UI():
    """
    Clasa se ocupa cu afisari/citiri (chestii ce tin de user interface)
    """
    def __init__(self, catalog, markController):
        self.__catalog = catalog
        self.__markController = markController
    def startUi(self):
        """
        Inceperea programului
        """
        option = 1;
        while (option != 0):
            print("(1) Afiseaza toti studentii")
            print("(2) Adauga student")
            print("(3) Afiseaza toate materiile")
            print("(4) Adauga materie")
            print("(5) Sterge student")
            print("(6) Sterge materie")
            print("(7) Modifica student")
            print("(8) Modifica materie" )
            print("(9) Gaseste student")
            print("(10) Gaseste materie")
            print("(11) Adauga nota")
            print("(12) Afiseaza toate notele")
            print("(13) Afiseaza lista de studenti si notele lor la o disciplina data")
            print("(14) Afiseaza primii 20% studenti in functie de media lor")
            print("(0) Iesire")
            option = int(input("alegeti o optiune:"))
            if option == 1:
                for st in self.__catalog.getAllStudents():
                    print(st)
                print()
            elif option == 2:
                ID = int(input("ID student: "))
                name = input("Nume student: ")
                try:
                    self.__catalog.addStudent(ID, name)
                except ValueError as lst:
                    print(lst)
            elif option == 3:
                for su in self.__catalog.getAllSubjects():
                    print(su)
                print()
            elif option == 4:
                ID = int(input("ID materie: "))
                name = input("Nume materie: ")
                prof = input("Profesor care preda materia: ")
                try:
                    self.__catalog.addSubject(ID, name, prof)
                except ValueError as lst:
                    print(lst);
            elif option == 5:
                ID = int(input("Id student: "))
                try:
                    self.__catalog.removeStudent(ID)
                except ValueError as err:
                    print(err)
            elif option == 6:
                ID = int(input("Id materie: "))
                try:
                    self.__catalog.removeSubject(ID)
                except ValueError as err:
                    print(err)
            elif option == 7:
                ID = int(input("Id student: "))
                newName = input("Noul nume pentru student: ")
                try:
                    self.__catalog.modifyStudent(ID, newName)
                except ValueError as err:
                    print(err);
            elif option == 8:
                ID = int(input("Id materie: "))
                newName = input("Noul nume pentru materie: ")
                newProf = input("Noul profesor pentru materie: ")
                try:
                    self.__catalog.modifySubject(ID, newName, newProf)
                except ValueError as err:
                    print(err);
            elif option == 9:
                ID = int(input("Id student: "))
                try:
                    stud = self.__catalog.findStudent(ID)
                    print(stud)
                except ValueError as err:
                    print(err)
            elif option == 10:
                ID = int(input("Id materie: "))
                try:
                    subj = self.__catalog.findSubject(ID)
                    print(subj)
                except ValueError as err:
                    print(err)
            elif option == 11:
                studId = int(input("Id student: "))
                subjId = int(input("Id materia: "))
                mark = int(input("Nota: "))
                try:
                    self.__markController.addMark(studId, subjId, mark)
                except ValueError as err:
                    print (err)
            elif option == 12:
                lst = self.__markController.getAll()
                for mark in lst:
                    print(self.__catalog.findStudent(mark.getStudentId()).getName(),
                          self.__catalog.findSubject(mark.getSubjectId()).getName(),
                          mark.getMark())
            elif option == 13:
                idSubj = int(input("Id-ul disciplinei: "))
                lst = self.__markController.getStudSubjList(idSubj)
                for dto in lst:
                    print(dto)
            elif option == 14:
                lst = self.__markController.getStudAverageList()
                for dto in lst:
                    print(dto)
            elif option != 0:
                print("Ati introdus o optiune gresita. Incercati din nou")
                print()