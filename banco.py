import datetime

# Constant for business rules
# there no const in python these are only uppercase cuz of convention for setting const
MAXIMUMDAILYWITHDRAWLIMIT = 3
MAXIMUMDEPOSITVALUEALLOWED = 1000000


class Banco:
    def __init__(self):
        self.balance = 0
        self.deposits = []
        self.withdraws = []
        self.dailyWithdraws = {}

    def isDepositValid(self, amount):
        if amount > 0 and amount < MAXIMUMDEPOSITVALUEALLOWED:
            return True
        else:
            print("Não é possivel realizar um deposito de um valor não positivo")
            return False

    def isWithdrawValid(self, amount):
        today = datetime.date.today()

        if amount > 0:
            if self.balance >= amount:
                if today in self.dailyWithdraws:
                    self.dailyWithdraws[today] += 1
                    return True
                else:
                    self.dailyWithdraws[today] = 1
                    return False
            else:
                print("Saldo insulficiente para realizar o saque.")
                return False
        else:
            print("O Valor do saque deve ser positivo")
            return False

    def checkDailyWithdrawsLimit(self):
        today = datetime.date.today()

        if today in self.dailyWithdraws and self.dailyWithdraws[today] > MAXIMUMDAILYWITHDRAWLIMIT:
            print("Limite maximo de saques diarios atingido")
            return False
        else:
            return True

    def deposit(self, amount):
        if (self.isDepositValid(amount)):
            self.balance += amount
            self.deposits.append(amount)
            print(f"Um deposito de R$:{amount:.2f} foi realizado com sucesso")

    def withdraw(self, amount):
        if self.checkDailyWithdrawsLimit() and self.isWithdrawValid(amount):
            self.balance -= amount
            self.withdraws.append(amount)

    def bankStatement(self):
        if not self.deposits and not self.withdraws:
            print("Não foram realizadas movimentações")
        else:
            print("Extrato")
            for deposits in self.deposits:
                print(f"Deposito: R$: {deposits:.2f}")
            for withdraw in self.withdraws:
                print(f"Saque: R$ {withdraw:.2f}")
            print(f"Saldo atual: R$ {self.balance:.2f}")
