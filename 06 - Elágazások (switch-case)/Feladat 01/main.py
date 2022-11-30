from os import system
system('cls')
print("A hét hanyadik napja van?")
napocska=int(input())

match napocska:
    case 1:
        print("Hétfő")
    case 2:
        print("kedd")
    case 3:
        print("szerda")
    case 4:
        print("csütörtök")
    case 5:
        print("péntek")
    case 6:
        print("szombat")
    case 7:
        print("vasarnap")
    