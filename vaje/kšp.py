# def vnos():
#     izbira = input("Vnesi kamen, škarje ali papir: ").lower()
#     return izbira


# def igra(igralec1, igralec2):
#     print("Igralec 1:", igralec1)
#     print("Igralec 2:", igralec2)

#     if igralec1 == igralec2:
#         print("Neodločeno!")

#     elif (igralec1 == "kamen" and igralec2 == "škarje") or \
#          (igralec1 == "škarje" and igralec2 == "papir") or \
#          (igralec1 == "papir" and igralec2 == "kamen"):
#         print("Igralec 1 je zmagal!")

#     else:
#         print("Igralec 2 je zmagal!")


# if __name__ == "__main__":
#     igralec1 = input("Igralec 1 - vnesi: ").lower()
#     igralec2 = input("Igralec 2 - vnesi: ").lower()

#     if igralec1 in ["kamen", "škarje", "papir"] and igralec2 in ["kamen", "škarje", "papir"]:
#         igra(igralec1, igralec2)
#     else:
#         print("Napačen vnos!")



# ---------------------------------------------------------------------



def izračunajZmage(igre:list) -> list:
    zmage = []
    for i in range(0, len(igre), 2):
        # print(i, i+1)
        prvi = igre[i]
        drugi = igre[i+1]
        odg = kdoZmaga(prvi, drugi)
        zmage.append(odg)
    return zmage
 
def izdelajStat(zmage: list) -> list:
    zmage1 = 0
    zmage2 = 0
    izen = 0
    for z in zmage:
        if z == 1:
            zmage1 += 1
        elif z == 2:
            zmage2 += 1
        else:
            izen += 1
            
    return [izen, zmage1, zmage2] 
       
    #           'K'     'Š'      ->  1
def kdoZmaga(prvi:str, drugi:str) -> int:
    if prvi == drugi: return 0
    if prvi == 'K' and drugi == 'Š': return 1
    if prvi == 'K' and drugi == 'P': return 2
    if prvi == 'Š' and drugi == 'K': return 2
    if prvi == 'Š' and drugi == 'P': return 1
    if prvi == 'P' and drugi == 'Š': return 2
    if prvi == 'P' and drugi == 'K': return 1
    
    
 
if __name__ == "__main__":
    # poz:   0    1   2   3   4     5   6   7
    igre = ['K', 'Š', 'K', 'P', 'Š', 'P', 'K', 'K']
    z = izračunajZmage(igre)
    s = izdelajStat(z)
    print(z)
    print(s)
