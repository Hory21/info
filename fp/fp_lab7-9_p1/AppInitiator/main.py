'''
Created on Nov 11, 2014

@author: horatiu
'''
from controller.Catalog import Catalog
from repository.StudentRepo import StudentRepo
from Validator.StudentValidator import StudentValidator
from ui.ui import UI
from Validator.SubjectValidator import SubjectValidator
from repository.SubjectRepo import SubjectRepo
from controller.MarkController import MarkController
from repository.MarkRepo import MarkRepo
from Validator.MarkValidator import MarkValidator
from repository.MarkRepoFile import MarkRepoFile
from repository.StudentRepoFile import StudentRepoFile
from repository.SubjectRepoFile import SubjectRepoFile

stur = StudentRepoFile("students1.txt")
sbr = SubjectRepoFile("subjects1.txt")
catalog = Catalog(StudentValidator(), stur,
                  SubjectValidator(), sbr)
markController = MarkController(MarkValidator(), MarkRepoFile("marks1.txt"),
                                stur, sbr)
ui = UI(catalog, markController)
ui.startUi()
