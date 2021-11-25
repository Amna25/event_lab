class Customer:
    def __init__(self,name,wallet,favourite_performer):
        self.name= name
        self.wallet= wallet
        self.favourite_performer= favourite_performer

    def check_money(self):
        return self.wallet  

    def reduce_wallet(self, amount):
        self.wallet -= amount

    def say_favourite_performer(self):
        return self.favourite_performer
