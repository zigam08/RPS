def vnos():
    izbira = input("Vnesi kamen, škarje ali papir: ").lower()
    return izbira


def igra(igralec1, igralec2):
    print("Igralec 1:", igralec1)
    print("Igralec 2:", igralec2)

    if igralec1 == igralec2:
        print("Neodločeno!")

    elif (igralec1 == "kamen" and igralec2 == "škarje") or \
         (igralec1 == "škarje" and igralec2 == "papir") or \
         (igralec1 == "papir" and igralec2 == "kamen"):
        print("Igralec 1 je zmagal!")

    else:
        print("Igralec 2 je zmagal!")


if __name__ == "__main__":
    igralec1 = input("Igralec 1 - vnesi: ").lower()
    igralec2 = input("Igralec 2 - vnesi: ").lower()

    if igralec1 in ["kamen", "škarje", "papir"] and igralec2 in ["kamen", "škarje", "papir"]:
        igra(igralec1, igralec2)
    else:
        print("Napačen vnos!")
