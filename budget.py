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

    def sum_withdraws(self):
        ledger = self.ledger
        return sum([-ledger[value]['amount'] for value in range(len(ledger)) if ledger[value]['amount'] < 0])
    


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

    '''Getting name and sum of withdraws of each item in categories list'''
    name_totalWithdraws = dict()
    for category in categories: name_totalWithdraws[category.category] = category.sum_withdraws()

    total = 0
    for key in name_totalWithdraws:
        total += name_totalWithdraws[key]
    
    bars = []
    for key in name_totalWithdraws:
        bars.append(compute_bar_height(name_totalWithdraws[key] / total * 100))
    
    bar_chart_values = ['100|',' 90|', ' 80|', ' 70|', ' 60|', ' 50|', ' 40|', ' 30|', ' 20|', ' 10|', '  0|']
    dashes = ' '*(len(bar_chart_values[0])) 
    output = "Percentage spent by category"+"\n"
    
    for i in range(len(bar_chart_values)):
        for j in range(len(bars)):
            bar_chart_values[i] += ' '+ bars[j][i]+' '
        output += bar_chart_values[i]+' \n'

    output += dashes+'---'*len(bars)+'-\n'

    max_length = None
    for key in name_totalWithdraws:
        if max_length == None: max_length = len(key)
        if len(key) >= max_length: max_length = len(key)
    
    category_names = []
    for key in name_totalWithdraws:
        category_names.append(name_splitter(key,max_length))
    
    final_print =''
    for i in range(max_length):
        final_print +='    '
        for j in range(len(bars)):
            final_print +=' ' + category_names[j][i] + ' '

        if i< max(range(max_length)): final_print +=' \n'
        else: final_print +=' '
        
    return output + final_print

def compute_bar_height(value):
    bar_height = 0
    while value >= 10:
        value -= 10
        bar_height += 1
    if value >= 5: bar_height += 1

    bar = ["o"," "," "," "," "," "," "," "," "," ", " "]
    for i in range(bar_height): bar[i+1]= "o"
    return bar[::-1]

def name_splitter(name, max_length):
    output = []
    for letter in range(max_length):
        try:
            output.append(name[letter])
        except:
            output.append(' ')
    return output
    