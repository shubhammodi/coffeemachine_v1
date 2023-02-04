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

def print_report(res, profit):
    # pprint.pprint(res)
    for key, value  in res.items():
        if key != "coffee":
            print(key.capitalize()+": " + str(value) + "ml") 
        else:
            print(key.capitalize()+": " + str(value) + "g") 
    print("Money: $"+str(profit))

while inputvalue != "off":
    inputvalue = input("What would you like? (espresso/latte/cappuccino):")
    
    print(inputvalue)
    if inputvalue == "report":
        print_report(resources, profit)
    elif inputvalue == "espresso":
        required_water = MENU[inputvalue]["ingredients"]["water"]
        required_coffee = MENU[inputvalue]["ingredients"]["coffee"]
        if required_water>resources["water"]:
            print("Sorry there is not enough water.")
        elif required_coffee>resources["coffee"]:
            print("Sorry there is not enough coffee.")
        else:
            print("Please insert coins.")
            monetaryvalue = 0.0
            for coin, value in insertcoin.items():
                num = int(input("How many "+coin+"?"))
                monetaryvalue =  monetaryvalue + num*value
            if monetaryvalue < MENU[inputvalue]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif monetaryvalue > MENU[inputvalue]["cost"]:
                monetaryvalue = monetaryvalue - MENU[inputvalue]["cost"]
                offerchange = round(monetaryvalue, 2)
                print(f"Here is ${offerchange} dollars in change.")
                profit = profit + MENU[inputvalue]["cost"]
                resources["water"] = resources["water"] - required_water
                resources["coffee"] = resources["coffee"] - required_coffee
                print(f"Here is your {inputvalue}.")
            else:
                profit = profit + monetaryvalue
                resources["water"] = resources["water"] - required_water
                resources["coffee"] = resources["coffee"] - required_coffee
                print(f"Here is your {inputvalue}.")
                # print_report(resources, profit)
    elif inputvalue == "latte" or inputvalue == "cappuccino":
        required_water = MENU[inputvalue]["ingredients"]["water"]
        required_coffee = MENU[inputvalue]["ingredients"]["coffee"]
        required_milk = MENU[inputvalue]["ingredients"]["milk"]
        if required_water>resources["water"]:
            print("Sorry there is not enough water.")
        elif required_coffee>resources["coffee"]:
            print("Sorry there is not enough coffee.")
        elif required_milk>resources["milk"]:
            print("Sorry there is not enough milk.")
        else:
            print("Please insert coins.")
            monetaryvalue = 0.0
            for coin, value in insertcoin.items():
                num = int(input("How many "+coin+"?"))
                monetaryvalue =  monetaryvalue + num*value
            if monetaryvalue < MENU[inputvalue]["cost"]:
                print("Sorry that's not enough money. Money refunded.")
            elif monetaryvalue > MENU[inputvalue]["cost"]:
                monetaryvalue = monetaryvalue - MENU[inputvalue]["cost"]
                offerchange = round(monetaryvalue, 2)
                print(f"Here is ${offerchange} dollars in change.")
                profit = profit + MENU[inputvalue]["cost"]
                resources["water"] = resources["water"] - required_water
                resources["coffee"] = resources["coffee"] - required_coffee
                resources["milk"] = resources["milk"] - required_milk
                print(f"Here is your {inputvalue}.")
            else:
                profit = profit + monetaryvalue
                resources["water"] = resources["water"] - required_water
                resources["coffee"] = resources["coffee"] - required_coffee
                resources["milk"] = resources["milk"] - required_milk
                print(f"Here is your {inputvalue}.")
                # print_report(resources, profit)


            


# TODO: Check resources sufficient to make drink order.