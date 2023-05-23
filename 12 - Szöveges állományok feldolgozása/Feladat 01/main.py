from typing import *
from student import Student
from studentIO import *
from services import *


students: List[Student] = importStudents()

for student in students:
    print(student)

countofClass:int=len(students)
print(f"\n\nAz osztálynak {countofClass} tanulója van.\n\n")

classAvarage:float=calculateAvarage(students)
print(f"\nAz osztály átlaga: {classAvarage:1.2f}\n\n")

bestStudent:Student=getBestStudent(students)
print(f"A legjibb tanuló: {bestStudent}")

aboveAvarage:List[Student]=studentsAboveAvarage(students, classAvarage)
writeStudentsInFile(aboveAvarage, "atlagfelett.txt")