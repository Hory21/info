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
        return str(self.cn) + ' ' + str(self.day) + ' ' + \
            str(self.amount) + ' ' + self.typ

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
