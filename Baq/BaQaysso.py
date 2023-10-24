name = input("whos living there?")

match name:
    case "Harry" | "Hermonie" | "Luki":
        print ("Gryffindor")
    case _:
        print ("who?")


