class Transaction:
    currentNb = 1

    def __init__(self, day, amount, typ):
        """
        functia creeaza un obiect nou si il initializeaza
        day: numar intreg
        amount: numar real
        typ: string
        """
        self.day = day
        self.amount = amount
        self.typ = typ
        self.cn = Transaction.currentNb
        Transaction.currentNb += 1

    def __str__(self):
        return str(self.day) + ' ' + str(self.amount) + ' ' + self.typ

    def update(self, day, amount, typ):
        """
        functia actualizeaza un obiect (ii schimba atributele)
        day: numar intreg
        amount: numar real
        typ: string
        """
        self.day = day
        self.amount = amount
        self.typ = typ

    def getCn(self):
        """
        functia returneaza numarul curent al unei tranzactii
        """
        return self.cn

    def getDay(self):
        """
        functia returneaza ziua in care s-a facut o tranzactie
        """
        return self.day

    def getAmount(self):
        """
        functia returneaza suma unei tranzactii
        """
        return self.amount

    def getType(self):
        """
        functia returneaza tipul unei tranzactii
        """
        return self.typ

def test_addTrans():
    l = []
    o = Transaction(9, 100, 'intrare')
    addTrans(l, o)
    assert l[0].cn == 1 and l[0].day == 9 and l[0].amount == 100 \
            and l[0].typ == 'intrare'
    o = Transaction(1, 10, 'iesire')
    addTrans(l, o)
    assert l[1].cn == 2 and l[1].day == 1 and l[1].amount == 10 \
            and l[1].typ == 'iesire'

def addTrans(lst, trans):
    """
    functia adauga o noua tranzactie (trans) in lista lst
    returneaza: lst cu elementul trans adaugat
    lst: lista de Transaction
    trans: obiect din clasa Transaction, care va fi adaugat in lst
    precond: lst: lista, trans: Transaction
    postcond: lista
    """
    lst.append(trans)
    return lst

def test_updateTrans():
    l = []
    o = Transaction(1, 2, 'iesire')
    addTrans(l, o)
    updateTrans(l, 0, 10, 10, 'intrare')
    assert l[0].day == 10 and l[0].amount == 10 and l[0].typ == 'intrare'

def updateTrans(lst, index, newDay, newAmount, newType):
    """
    functia modifica atributele unei anumite tranzactii
    returneaza: lst cu elementul de pe pozitia index modificat
    lst: lista din care va fi updatat un element
    index: pozitia din lst pe care se afla elementul care va fi modificat
    newDay, newAmount, newType: atributele cu care se vor inlocui cele actuale
        ale tranzactiei
    precond: lst: lista nevida, index: numar natural, < dimensiunea listei lst
    """
    lst[index].update(newDay, newAmount, newType)
    return lst

def test_deleteAllInPeriod():
    l = []
    o1 = Transaction(1, 100, 'iesire')
    o2 = Transaction(2, 10, 'intrare')
    o3 = Transaction(3, 100, 'intrare')
    l.append(o1)
    l.append(o2)
    l.append(o3)
    deleteAllInPeriod(l, 1, 2)
    assert l[0].day == 3
    assert l[0].amount == 100
    assert l[0].typ == 'intrare'
    assert len(l) == 1

def deleteAllInPeriod(lst, day1, day2):
    """
    sterge toate tranzactiile din perioada day1 - day2
    returneaza: lst din care tranzactiile din perioada day1 - day2 au fost sterse
    lst: lista din care se sterge
    day1: ziua de inceput
    day2: ziua de sfarsit
    precond: day1 <= day2
    """
    index = 0
    while index < len(lst):
        if lst[index].getDay() >= day1 and lst[index].getDay() <= day2:
            lst.pop(index)
            index -= 1
        index += 1
    return lst

def test_deleteAllOfType():
    l = []
    o1 = Transaction(1, 100, 'iesire')
    o2 = Transaction(2, 10, 'intrare')
    o3 = Transaction(3, 100, 'intrare')
    l.append(o1)
    l.append(o2)
    l.append(o3)
    deleteAllOfType(l, 'intrare')
    assert l[0].day == 1
    assert len(l) == 1

def deleteAllOfType(lst, typ):
    """
    functia sterge toate tranzactiile de tipul typ din lista lst
    returneaza: lst, dupa ce din lst s-au sters tranzactiile cu tipul typ
    lst: lista din care se sterge
    typ: tipul elementelor care se vor sterge
    """
    i = 0
    while i < len(lst):
        if lst[i].typ == typ:
            lst.pop(i)
            i -= 1
        i += 1
    return lst

def test_sumOfTypeTrans():
    l = []
    o1 = Transaction(1, 100, 'iesire')
    o2 = Transaction(2, 10, 'intrare')
    o3 = Transaction(3, 100, 'intrare')
    l.append(o1)
    l.append(o2)
    l.append(o3)
    assert sumOfTypeTrans(l, 'intrare') == 110
    assert sumOfTypeTrans(l, 'iesire') == 100

def sumOfTypeTrans(lst, typ):
    """
    functia calculeaza suma tuturor tranzactiilor de tipul typ din lista lst
    returneaza: suma respectiva
    lst: lista in care se gasesc tranzactii
    typ: tipul tranzactiilor a caror suma se va calcula
    """
    summ = 0
    for trans in lst:
        if trans.getType() == typ:
            summ += trans.getAmount()
    return summ

def test_balanceOnDate():
    l = []
    o1 = Transaction(1, 100, 'iesire')
    o2 = Transaction(2, 10, 'intrare')
    o3 = Transaction(3, 100, 'intrare')
    l.append(o1)
    l.append(o2)
    l.append(o3)
    assert balanceOnDate(l, 1) == -100
    assert balanceOnDate(l, 2) == -90
    assert balanceOnDate(l, 3) == 10

def balanceOnDate(lst, day):
    """
    functia calculeaza si returneaza soldul contului din ziua day
    daca in ziua day s-a facut vreo tranzactie, aceasta VA FI si ea luata in
        calcul
    lst: lista cu tranzactii
    day: ziua a carui sold va fi afisat
    """
    balance = 0
    for trans in lst:
        if trans.getDay() <= day:
            if trans.getType() == 'intrare':
                balance += trans.getAmount()
            if trans.getType() == 'iesire':
                balance -= trans.getAmount()
    return balance

def test_getAllTransOfType_orderByAmount():
    l = []
    o1 = Transaction(1, 100, 'iesire')
    o2 = Transaction(2, 10, 'intrare')
    o3 = Transaction(3, 1, 'intrare')
    l.append(o1)
    l.append(o2)
    l.append(o3)
    o4 = o2
    o5 = o3
    auxLst = []
    auxLst.append(o5)
    auxLst.append(o4)
    assert getAllTransOfType_orderByAmount(l, 'intrare') == auxLst

def getAllTransOfType_orderByAmount(lst, typ):
    """
    functia cauta toate tranzactiile de tipul typ din lista lst, le sorteaza
        dupa suma (amount) si returneaza lista care le contine pe acestea
    lst: lista in care se cauta tranzactii
    typ: tipul tranzactiilor care se vor returna
    postcond: o lista cu tranzactii, unde acestea sunt sortate crescator
        dupa suma
    """
    auxLst = []
    for trans in lst:
        if trans.getType() == typ:
            auxLst.append(trans)
    return sorted(auxLst, key = lambda trans: trans.amount)

test_addTrans()
test_updateTrans()
test_deleteAllInPeriod()
test_deleteAllOfType()
test_sumOfTypeTrans()
test_balanceOnDate()
test_getAllTransOfType_orderByAmount()

def printList(lst):
    """
    functia afiseaza pe ecran elementele listei lst
    """
    i = 0
    for element in lst:
        print(i, element)
        i += 1
    print()

def printTransHigherThan(lst, amount):
    """
    functia afiseaza toate tranzactiile cu sume mai mari strict decat amount
    lst: (numar) lista din care se afiseaza tranzactii
    amount: (numar) suma fata de care se afiseaza tranzactii
    """
    for trans in lst:
        if trans.getAmount() > amount:
            print(trans)
    print()

def printTransBeforeDayHigherThan(lst, day, amount):
    """
    functia scrie pe ecran toate tranzactiile din lst facute mai devreme de
        day, si mai mari decat amount
    lst: lista de tranzactii
    day: (numar) ziua din care se afiseaza tranzactii
    amount: (numar) suma fata de care se afiseaza tranzactii
    """
    for trans in lst:
        if trans.getDay() < day and trans.getAmount() > amount:
            print(trans)
    print()

def printTransOfType(lst, typ):
    """
    functia afiseaza toate tranzactie de tipul typ
    typ: (string) tipul tranzactiilor care vor fi afisate
    lst: lista din care se afiseaza tranzactii
    """
    for trans in lst:
        if trans.getType() == typ:
            print(trans)
    print()

def mainMenu():
    """
    meniul principal; de aici se incepe rularea programului
    """
    transList = []
    option = 1
    while option != 0:
        print('Meniu principal:')
        print('(1) Afiseaza tranzactiile (index, zi, suma, tip)')
        print('(2) Adauga/Actualizeaza tranzactie')
        print('(3) Stergere')
        print('(4) Cautari')
        print('(5) Rapoarte')
        print('(6) Filtrare')
        print('(7) Undo (renunta la ultima modificare a tranzactiilor)')
        print('(0) Iesire')
        option = int(input())
        if option == 1:
            printList(transList)
        elif option == 2:
            menu1(transList)
        elif option == 3:
            menu2(transList)
        elif option == 4:
            menu3(transList)
        elif option == 5:
            menu4(transList)
        elif option != 0:
            print('Optiune gresita; incercati din nou')

def menu1(transList):
    """
    meniu de adaugare/actualizare tranzactii
    """
    option = 1
    while option != 0:
        print('(1) Adaugare tranzactie noua')
        print('(2) Actualizare tranzactie')
        print('(0) Inapoi')
        option = int(input())
        if option == 1:
            day = int(input('ziua:'))
            amount = int(input('suma:'))
            typ = input('tipul (intrare/iesire):')
            addTrans(transList, Transaction(day, amount, typ))
        elif option == 2:
            index = int(input('indexul tranzactiei care va fi modificata:'))
            if index >= len(transList):
                print('Tranzactia cu numarul de ordine', index, 'nu exista!')
                continue
            day = int(input('ziua:'))
            amount = int(input('suma:'))
            typ = input('tipul (intrare/iesire):')
            updateTrans(transList, index, day, amount, typ)
        elif option != 0:
            print('Optiune gresita; incercati din nou')

def menu2(transList):
    """
    meniu de stergere tranzactii
    """
    option = 1
    while option != 0:
        print('(1) Sterge toate tranzactiile de la ziua specificata')
        print('(2) Șterge tranzacțiile dintr-o perioadă dată',
                '(se dă ziua de început și sfârșit)')
        print('(3) Sterge toate tranzactiile de un anumit tip')
        print('(0) Inapoi')
        option = int(input())
        if option == 1:
            day = int(input('ziua: '))
            deleteAllInPeriod(transList, day, day)
        elif option == 2:
            day1 = int(input('ziua de inceput: '))
            day2 = int(input('ziua de sfarsit: '))
            deleteAllInPeriod(transList, day1, day2)
        elif option == 3:
            typ = input('tipul: ')
            deleteAllOfType(transList, typ)
        elif option != 0:
            print('Optiune gresita; incercati din nou')

def menu3(transList):
    """
    meniu de cautare tranzactii
    """
    option = 1
    while option != 0:
        print('(1) Tipărește tranzacțiile cu sume mai mari decăt o sumă dată')
        print('(2) Tipărește toate tranzacțiile efectuate înainte de o zi și',
                'mai mari decât o sumă (se dă suma și ziua)')
        print('(3) Tipărește tranzacțiile de un anumit tip')
        print('(0) Inapoi')
        option = int(input())
        if option == 1:
            printTransHigherThan(transList, int(input('suma: ')))
        elif option == 2:
            printTransBeforeDayHigherThan(transList, int(input('ziua: ')),
                    int(input('suma: ')))
        elif option == 3:
            printTransOfType(transList, input('tipul: '))
        elif option != 0:
            print('Optiune gresita; incercati din nou')

def menu4(transList):
    """
    meniu de rapoarte
    """
    option = 1
    while option != 0:
        print('(1) Afiseaza suma totală a tranzacțiilor de un anumit tip')
        print('(2) Afiseaza soldul contului la o dată specificată')
        print('(3) Tipărește toate tranzacțiile de un anumit tip ordonate după sumă')
        print('(0) Inapoi')
        option = int(input())
        if option == 1:
            typ = input('tipul: ')
            print('Suma totala a tranzactiilor de', typ, 'este',
                    sumOfTypeTrans(transList, typ))
        elif option == 2:
            date = int(input('data: '))
            print('Soldul contului pe data de', date, 'este',
                    balanceOnDate(transList, date))
        elif option == 3:
            typ = input('tip: ')
            printList(getAllTransOfType_orderByAmount(transList, typ))
        elif option != 0:
            print('Optiune gresita; incercati din nou')

mainMenu()
