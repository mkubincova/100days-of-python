MENU = {
    "espresso": {
        "ingredients": {
            "water": 50,
            "milk": 0,
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
    "water": 300,
    "milk": 200,
    "coffee": 100,
}


def is_resource_sufficient(ingredients):
    for key in resources:
        if resources[key] < ingredients[key]:
            print(f"Sorry, there is not enough {key}")
            return False
    return True


def get_payment():
    print("Please insert coins.")
    total = float(input("How manu quarters?: ")) * 0.25
    total += float(input("How manu dimes?: ")) * 0.10
    total += float(input("How manu nickles?: ")) * 0.05
    total += float(input("How manu pennies?: ")) * 0.01
    return total


def is_transaction_successful(drink_cost, money_received):
    if money_received < drink_cost:
        print("Sorry that's not enough money. Money refunded.")
        return False
    else:
        change = round(money_received - drink_cost, 2)
        print(f"Here is ${change} in change.")
        global profit
        profit += drink_cost
        return True


def make_coffee(drink_name, ingredients):
    for key in resources:
        resources[key] -= ingredients[key]
    print(f"Here is your {drink_name} ☕️. Enjoy!")


while True:
    order = input("What would you like? (espresso/latte/cappuccino): ")
    if order == "off":
        break
    if order == "report":
        print(f"Water: {resources['water']}ml")
        print(f"Milk: {resources['milk']}ml")
        print(f"Coffee: {resources['coffee']}g")
        print(f"Money: ${profit}")
    elif order == "espresso" or order == "latte" or order == "cappuccino":
        drink = MENU[order]
        if is_resource_sufficient(drink["ingredients"]):
            payment = get_payment()
            if is_transaction_successful(drink["cost"], payment):
                make_coffee(order, drink["ingredients"])
    else:
        print("Sorry, this is not on the menu...")



