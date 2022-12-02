from os import system
system('cls')

print("Adja meg a hónapot amiben született")
honap=str(input().lower().strip())

match honap:

    case "január" | "jan":
        print("Ön az 1. hónapban született")
    case "február" | "feb":
        print("Ön a 2. hónapban született")
    case "március" | "mar":
        print("Ön a 3. hónapban született")
    case "április" | "apr":
        print("Ön a 4. hónapban született")
    case "május" | "maj":
        print("Ön az 5. hónapban született")
    case "június" | "jun":
        print("Ön a 6. hónapban születetett")
    case "július" | "jul":
        print("Ön a 7. hónapban született")
    case "augusztus" | "aug":
        print("Ön a 8. hónapban született")
    case "szeptember" | "sep":
        print("Ön a 9. hónapban született")
    case "október" | "okt":
        print("Ön a 10. hóapban született")
    case "november" | "nov":
        print("Ön a 11. hónapban született")
    case "december" | "dec":
        print("Ön a 12. hónapban született")