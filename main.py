from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

inputvalue = ''
ison = True
money_mach = MoneyMachine()
coffee_make = CoffeeMaker()
menu_obj = Menu()

while ison:
    inputvalue = input("What would you like? (espresso/latte/cappuccino):")
    print(inputvalue)
    if inputvalue == "off":
        ison = False   
    elif inputvalue == "report":
        coffee_make.print_report()
        money_mach.print_report()
    else:
        drink = menu_obj.find_drink(inputvalue)
        
        if coffee_make.is_resources_sufficient(drink):            
            if money_mach.is_transaction_successful(drink.cost):
                coffee_make.make_coffee(drink)
                