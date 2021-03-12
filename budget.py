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
        if not(self.check_funds(amount)): return False
        if description == None: self.ledger.append({"amount": -amount, "description": ""})
        else: self.ledger.append({"amount": -amount, "description": description})
        return True        


    def get_balance(self): 
        ledger = self.ledger
        return sum([ledger[value]['amount'] for value in range(len(ledger))])


    def transfer(self, amount, destination):
        if  not (self.check_funds(amount)): return False
        self.withdraw(amount, f"Transfer to {destination.category}")
        destination.deposit(amount, f"Transfer from {self.category}")
        return True


    def check_funds(self, amount):
        return  not (amount > self.get_balance())

    def __str__(self): return   self.first_line() + self.print_description_amount()


    def first_line(self): 
        output = str(self.category)
        while len(output) <30: output = '*'+output+'*'
        return output


    def print_description_amount(self):
        output = ""
        for item in self.ledger:
            description = item['description']
            if len(description) >= 23:description = description[:23]
            else: description = description + (23-len(description))*' '
            
            amount = str(item['amount'])
            if len(amount.split('.')) == 1:
                amount += '.00'
            else:
                if len(amount.split('.')[1]) == 1:
                    amount += '0'
            
            if len(amount) <= 7: 
                amount = ' '*(7-len(amount))+amount

            output+='\n' + description + amount

        output += '\n' + "Total: "+str(self.get_balance())        

        return output

def create_spend_chart(categories):
    bar_chart = list()
    bar_chart_values = [100]
    for i in range 

    return "Percentage spent by category"+"\n"