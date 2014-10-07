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

def longestSecv1(lst):
    maxLen = 0
    secvIndex = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst)):
            if len(lst[i:j]) > maxLen and checkProp1(lst[i:j]):
                secvIndex = i
                maxLen = len(lst[i:j])
    return lst[secvIndex:secvIndex + maxLen]
