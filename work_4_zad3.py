class BankAccount:

    def __int__(self, number):
        self.number = number
        self.cash = 0.0

    def deposit_cash(self, amount):
        if amount < 0:
            return
        if amount <= self.cash:
            self.cash -= amount
            return amount
        else:
            ret_val = self.cash
            self.cash = 0
            return ret_val

    def print_info(self):
        print(f'konto o numerze{self.number} i stanie {self.cash}')

b = BankAccount(123)
b.deposit_cash(1000)
b.print_info()
b.withdraw_cash(200)
b.withdraw_cash(100)
b.print_info()