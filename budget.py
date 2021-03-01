class Category:
    

    def __init__(self, category): # Constructor
        self.category = category
        self.ledger = list()
        
    
    def deposit(self, amount, description = None):
        if description == None:
            self.ledger.append({"amount": amount, "description": ""})
        else:
            self.ledger.append({"amount": amount, "description": description})

    
def create_spend_chart(categories):
    pass