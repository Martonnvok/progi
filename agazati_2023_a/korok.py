def konzolra_ir():
    pass
def fajl_ir():
    pass
def elso_idos():
    hetvenesek=[]
    for i in range(len(korL)):
        if korL[i] >= 70:
            hetvenesek.append(korL)
            print("Az első hetvenes kor feletti: ",hetvenesek[0])
korL=[]
def masodik():
    i=0
    while i < 5:
        korok = int(input("Kérek egy életkort: [0, 120]"))
        if korok > 120 or korok < 0:
            korok = int(input("nem jól adtad meg, kérek egy életkort: [0, 120]"))
        else:
            korL.append(korok)
            i += 1
    for n in range (len(korL)):
        print("{};".format(korL), end=":")
    print()
