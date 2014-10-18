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
        return self.cn

    def getDay(self):
        return self.day

    def getAmount(self):
        return self.amount

    def getType(self):
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

test_addTrans()
test_updateTrans()

def printList(lst):
    """
    functia afiseaza pe ecran elementele listei lst
    """
    i = 0
    for element in lst:
        print(i, element)
        i += 1
    print()

def mainMenu():
    transList = []
    option = 1
    while option != 0:
        print('Meniu principal:')
        print('(1) Afiseaza tranzactiile (index, zi, suma, tip)')
        print('(2) Adauga/Actualizeaza tranzactie')
        print('(0) Iesire')
        option = int(input())
        if option == 1:
            printList(transList)
        elif option == 2:
            menu1(transList)
        elif option != 0:
            print('Optiune gresita; incercati din nou')

def menu1(transList):
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

mainMenu()
