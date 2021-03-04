class Category:
    

    def __init__(self, category): # Constructor
        self.category = category
        self.ledger = list()
        
    
    def deposit(self, amount, description = None):
        if description == None:
            self.ledger.append({"amount": amount, "description": ""})
        else:
            self.ledger.append({"amount": amount, "description": description})


    def withdraw(self, amount, description = None):
        sum_ledger = self.get_balance()
        if sum_ledger <=0: return False
        if description == None: self.ledger.append({"amount": -amount, "description": ""})
        else: self.ledger.append({"amount": -amount, "description": description})
        return True


    def get_balance(self): 
        ledger = self.ledger
        return sum([ledger[value]['amount'] for value in range(len(ledger))])
        

    def transfer(self, amount, destination):
        sum_ledger = self.get_balance()
        if sum_ledger <=0: return False
        self.withdraw(amount, f"Transfer to {destination.category}")
        destination.deposit(amount, f"Transfer from {self.category}")
        return True

    def check_funds(self, amount):
        if self.get_balance() < amount: return False
        return True

def create_spend_chart(categories):
    pass