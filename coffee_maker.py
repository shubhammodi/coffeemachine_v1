class CoffeeMaker:
    def __init__(self):
        self.resources = {
            "water": 300,
            "milk": 200,
            "coffee": 100,
        }
    def print_report(self):
        for key, value  in self.resources.items():
            if key != "coffee":
                print(key.capitalize()+": " + str(value) + "ml") 
            else:
                print(key.capitalize()+": " + str(value) + "g") 
    
    def make_coffee(self, drinkname):
        """Deduct the required ingredients from the resources."""
        for item in drinkname.ingredients:
            self.resources[item] -= drinkname.ingredients[item]
        print(f"Here is your {drinkname.name} ☕️. Enjoy!")
    
    def is_resources_sufficient(self,drinkname):
        """Returns True when order can be made, False if ingredients are insufficient."""
        for item in drinkname.ingredients:
            if self.resources[item]<drinkname.ingredients[item]:
                print(f"Sorry there is not enough {item}.")
                return False
        return True






