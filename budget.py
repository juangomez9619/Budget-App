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
        sum_ledger = self.sum_ledger()
        if sum_ledger <=0: return False
        if description == None: self.ledger.append({"amount": -amount, "description": ""})
        else: self.ledger.append({"amount": -amount, "description": description})
        return True


    def get_balance(self): return self.sum_ledger()
    def sum_ledger(self):
        '''
        Returns the actual sum of the ladger. 
        '''
        ledger = self.ledger
        ledger_values = [ledger[value]['amount'] for value in range(len(ledger))]
        
        return sum(ledger_values)

    def transfer(self, amount, destination):
        sum_ledger = self.sum_ledger()
        if sum_ledger <=0: return False
        self.withdraw(amount, f"Transfer to {destination.category}")
        destination.deposit(amount, f"Transfer from {self.category}")
        return True






        



        






def create_spend_chart(categories):
    pass