MENU = {
    "espresso": {
        "ingredients": {
            "water": 200,
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


def display_report():
    print(f"Water: {resources['water']}ml")
    print(f"Milk: {resources['milk']}ml")
    print(f"Coffee: {resources['coffee']}g")
    print(f"Money: ${profit}")


def process_funds():
    quarters = float(input("How many quarters?: ")) * 0.25
    dimes = float(input("How many dimes?: ")) * 0.1
    nickles = float(input("How many nickles?: ")) * 0.05
    pennies = float(input("How many pennies?: ")) * 0.01
    return quarters + dimes + nickles + pennies


def is_transaction_successful(funds, cost):
    if funds >= cost:
        change = round(funds - cost, 2)
        global profit
        profit += cost
        if change > 0:
            print(f"Here is your change: ${change}")
        else:
            print("Sorry, that's not enough money. Money refunded.")


def check_sufficient_resources(order_resources):
    for ingredient in order_resources:
        if order_resources[ingredient] > resources[ingredient]:
            print(f"Not enough {ingredient.title()}")
            return False
        else:
            return True


def make_coffe(drink_name, order_resources):
    for ingredient in order_resources:
        resources[ingredient] -= order_resources[ingredient]
    print(f"Here is your {drink_name.title()}. Enjoy!")


is_on = True

while is_on:
    choice = input("What would you like? (espresso/latte/cappuccino): ")
    if choice == "off":
        is_on = False
    elif choice == "report":
        display_report()
    else:
        drink = MENU[choice]
        if check_sufficient_resources(drink["ingredients"]):
            funds = process_funds()
            is_transaction_successful(funds, drink["cost"])
            make_coffe(choice, drink["ingredients"])
