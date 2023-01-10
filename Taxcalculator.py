class TaxCalculator:
    def __init__(self, income, discount):
        self.income = income
        self.discount = discount
    
    def calTax(self):
        if(self.income) >= 300000:
            caltax = (self.income * 0.3) - (self.discount * 0.05)
            return caltax
        elif(self.income) >= 200000:
            caltax = (self.income * 0.1) - (self.discount * 0.05)
            return caltax
        else:
            caltax = 0
            return caltax

    def showInfo(self):
        print("Your tax in this year = ", self.calTax() , " THB")


val_income = int(input("Enter your Income : "))
val_discount = int(input("Enter your Discount : "))

tax = TaxCalculator(val_income, val_discount)
tax.showInfo()
