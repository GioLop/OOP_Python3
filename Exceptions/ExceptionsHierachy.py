# class InvalidWithdrawal(Exception):
#     pass

# raise InvalidWithdrawal("You don´t have $50 in your account")

class InvalidWithdrawal(Exception):
    def __init__(self, balance, amount):
        super().__init__("account doesn´t have ${}".format(amount))
        self.amount = amount
        self.balance = balance
    
    def overgae(self):
        return self.amount - self.balance

# raise InvalidWithdrawal(25, 50)

try:
    raise InvalidWithdrawal(25, 50)
except InvalidWithdrawal as e:
    print("I'm sorry, but your withdrawl is"
        " more than your balance by"
        "${}".format(e.overgae()))
