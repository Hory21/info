#cerintele 2, 14

g_lst = []

"""
    Functia citeste o lista de numere, citind initial numarul
    de elemente din lista, apoi elementele listei pe rand,
    cate unul pe linie;
    Lista citita este stocata apoi in variabila globala g_lst;
"""
def readList():
    n = int(input("Numarul de elemente din lista: "))
    print("Elementele listei (cate unul pe linie):")
    global g_lst
    g_lst = []
    for i in range(n):
        g_lst.append(int(input()))

"""
    Functia verifica daca o lista contine cel mult 3 valori
    distincte;
    lst: o lista de numere intregi
    returneaza: True daca lst contine cel mult 3 valori distincte,
    False altfel;
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
    proprietatea propFunc;
    lst: o lista de numere intregi
    propFunc: o functie care returneaza True daca o secventa are
    o anumita proprietate, si false altfel;
    returneaza: o lista de numere intregi
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
    lst: o lista de numere intregi
    returneaza: True sau False
"""
def checkProp2(lst):
    for i in range(len(lst) - 1):
        if len(set(str(abs(lst[i]))) & set(str(abs(lst[i + 1])))) < 2:
            """
                daca intersectia dintre multimea cifrelor distincte ale
                elementului lst[i] si multimea cifrelor distincte ale
                elementului lst[i + 1] are mai putin de 2 cifre, se
                returneaza False;
            """
            return False
    return True

"""
    Functia afiseaza meniul, lasa utilizatorul ca selecteze o optiune
    din meniu introducand un numar, si executa o functie, in functie
    de optiunea aleasa, dupa care afiseaza din nou meniul, pana cand
    optiunea 4 (iesire) este aleasa;
"""
def menu():
    option = '0'
    while option != '4':
        print("(1) Citire lista de numere intregi")
        print("(2) Gasirea secventei de lungime maxima care contine cel mult 3 valori distincte")
        print("(3) Gasirea secventei de lungime maxima ale carei oricare doua elemente consecutive au cel putin 2 cifre distincte comune")
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
