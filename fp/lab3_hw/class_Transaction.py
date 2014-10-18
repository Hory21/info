class Transaction:
    currentNb = 0
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
    def show(self):
        """
        functia afiseaza pe ecran atributele obiectului asupra
        caruia se apeleaza
        """
        print(self.cn, self.day, self.amount, self.typ)

l = []
o1 = Transaction(1, 2, 'intrare')
o2 = Transaction(45, 1000, 'intrare')
l.append(o1)
l.append(o2)
l[0].show()
l[1].show()
