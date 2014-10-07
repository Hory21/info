#cerintele 2, 14

def readList():
    n = int(input("Numarul de elemente din lista: "))
    lis = []
    print("Elementele listei (cate unul pe linie):")
    for i in range(n):
        lis.append(int(input()))
    return lis

def checkProp1(lst):
    auxlst = []
    auxlst.append(lst[0])
    for element in lst:
        if not (element in auxlst):
            auxlst.append(element)
    if len(auxlst) <= 3:
        return True
    else:
        return False
