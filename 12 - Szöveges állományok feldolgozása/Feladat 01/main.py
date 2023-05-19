from studentIO import importSzudents
from os import system
from typing import *
from student import Student

students:List[Student]=importSzudents()
for student in students:
    print(student)