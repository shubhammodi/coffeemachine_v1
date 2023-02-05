# import pprint
MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "coffee": 18,
        },
        "cost": 1.5,
    },
    "latte": {
        "ingredients": {
            "water": 200,
            "milk": 150,
            "coffee": 24,
        },
        "cost": 2.5,
    },
    "cappuccino": {
        "ingredients": {
            "water": 250,
            "milk": 100,
            "coffee": 24,
        },
        "cost": 3.0,
    }
}

profit = 0
resources = {
    "water": 500,
    "milk": 300,
    "coffee": 100,
}

inputvalue = ''
insertcoin = {"quarters":.25,"dimes":.1,"nickel":.05,"pennies":.01}
ison = True

def print_report(res, profit):
    # pprint.pprint(res)
    for key, value  in res.items():
        if key != "coffee":
            print(key.capitalize()+": " + str(value) + "ml") 
        else:
            print(key.capitalize()+": " + str(value) + "g") 
    print("Money: $"+str(profit))

def is_resources_sufficient(drinkname):
    """Returns True when order can be made, False if ingredients are insufficient."""
    for ingredients, quantity in drinkname["ingredients"].items():
        if resources[ingredients]<quantity:
            print(f"Sorry there is not enough {ingredients}.")
            return False
    return True

def process_coins():
    """Returns the total calculated from coins inserted."""
    print("Please insert coins.")
    monetaryvalue = 0.0
    for coin, value in insertcoin.items():
        num = int(input("How many "+coin+"? "))
        monetaryvalue =  monetaryvalue + num*value
    return monetaryvalue

def is_transaction_successful(moneyreceived, drinkcost):
    """Return True when the payment is accepted, or False if money is insufficient."""
    if moneyreceived < drinkcost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        global profit
        offerchange = round(moneyreceived - drinkcost, 2)
        print(f"Here is ${offerchange} dollars in change.")
        profit = profit + drinkcost
        return True

def make_coffee(drink_name, order_ingredients):
    """Deduct the required ingredients from the resources."""
    for item in order_ingredients:
        resources[item] -= order_ingredients[item]
    print(f"Here is your {drink_name} ☕️. Enjoy!")

while ison:
    inputvalue = input("What would you like? (espresso/latte/cappuccino):")
    print(inputvalue)
    if inputvalue == "off":
        ison = False   
    elif inputvalue == "report":
        print_report(resources, profit)
    else:
        drink = MENU[inputvalue]
        if is_resources_sufficient(drink):
            payment = process_coins()
            if is_transaction_successful(payment, drink["cost"]):
                make_coffee(inputvalue, drink["ingredients"])

            


# TODO: Check resources sufficient to make drink order.