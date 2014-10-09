#cerintele 2, 14

g_lst = []

def readList():
    n = int(input("Numarul de elemente din lista: "))
    print("Elementele listei (cate unul pe linie):")
    global g_lst
    g_lst = []
    for i in range(n):
        g_lst.append(int(input()))

"""
    Functia verifica daca o lista contine cel mult 3 valori
    distincte
"""
def checkProp1(lst):
    auxlst = []
    for element in lst:
        if not (element in auxlst):
            auxlst.append(element)
    if len(auxlst) <= 3:
        return True
    else:
        return False

"""
    Functia gaseste cea mai lunga secventa din lista lst care are
    proprietatea propFunc; propFunc va fi o functie care returneaza
    True daca o secventa are o anumita proprietate, si false altfel;
"""
def longestSecv(lst, propFunc):
    maxLen = 0
    secvIndex = 0
    for i in range(len(lst)):
        for j in range(i + 1, len(lst) + 1):
            if len(lst[i:j]) > maxLen and propFunc(lst[i:j]):
                secvIndex = i
                maxLen = len(lst[i:j])
    return lst[secvIndex:secvIndex + maxLen]

"""
    Functia verifica daca lista lst are proprietatea ca oricare 2 elemente
    consecutive sa aiba cel putin 2 cifre distincte comune
"""
def checkProp2(lst):
    for i in range(len(lst) - 1):
        if len(set(str(abs(lst[i]))) & set(str(abs(lst[i + 1])))) < 2:
            return False
    return True

def menu():
    option = '0'
    while option != '4':
        print("(1) Citire lista de numere intregi")
        print("(2) Gasirea secventei de lungime maxima care contine cel mult 3 valori distincte")
        print("(3) Gasirea secventei de lungime maxima ai carei oricare doua elemente consecutive au cel putin 2 cifre distincte comune")
        print("(4) Iesire")
        option = input()
        if option == '1':
            readList()
        elif option == '2':
            print(longestSecv(g_lst, checkProp1))
        elif option == '3':
            print(longestSecv(g_lst, checkProp2))
        elif option != '4':
            print("Optiune inexistenta")

menu()
