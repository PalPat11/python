from student import Student
from typing import *

def calculateAvarage(students:List[Student])->float:
    sum:float=0
    
    for student in students:
        sum+=student.avarage
    return sum/len(students)



def getBestStudent(students:List[Student])->Student:
    bestStudent:Student = students[0] #referencia érték
    for index in range(1, len(students), 1):
        if(students[index].avarage > bestStudent.avarage):
            bestStudent = students[index]
    return bestStudent



def studentsAboveAvarage(students:List[Student], classAvarage:float)->List[Student]:
    aboveAvarage:List[Student] = []

    for student in students:
        if(student.avarage>=classAvarage):
            aboveAvarage.append(student)

    return aboveAvarage


