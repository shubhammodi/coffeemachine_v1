class MoneyMachine:
    def __init__(self):
        self.profit = 0
        self.moneyreceived = 0

    insertcoin = {"quarters":.25,"dimes":.1,"nickel":.05,"pennies":.01}
    def print_report(self):
        print("Money: $"+str(self.profit))
    def is_transaction_successful(self, drinkcost):
        """Return True when the payment is accepted, or False if money is insufficient."""
        self.process_coins()
        if self.moneyreceived < drinkcost:
            print("Sorry that's not enough money. Money refunded.")
            self.moneyreceived = 0
            return False
        else:
            # global profit
            offerchange = round(self.moneyreceived - drinkcost, 2)
            print(f"Here is ${offerchange} dollars in change.")
            self.profit = self.profit + drinkcost
            self.moneyreceived = 0
            return True

    def process_coins(self):
        """Returns the total calculated from coins inserted."""
        print("Please insert coins.")
        # monetaryvalue = 0.0
        for coin, value in self.insertcoin.items():
            num = int(input("How many "+coin+"? "))
            self.moneyreceived =  self.moneyreceived + num*value
        return self.moneyreceived 
    