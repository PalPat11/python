from os import system
system('cls')

from matthfunctions import *
from consoleio import *


x:float=None
y:float=None
result:float=None

x=getNumberFromConsole()
y=getNumberFromConsole()

result=sumOfTwoNumbers(x, y)
printToConsole(x, y, result, "+")

osztas=defOfTwoNumbers(x, y)
printToConsole(x, y, osztas, "/")

szorzas=multOfTwoNumbers(x, y)
printToConsole(x, y, szorzas, "*")

kivonas=difOfTwoNumbers(x, y)
printToConsole(x, y, kivonas, "-")