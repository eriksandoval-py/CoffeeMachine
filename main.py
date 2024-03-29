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

resources = {
    "water": 300,
    "milk": 200,
    "coffee": 100,
}

machine_is_on = True
cost = 0


def print_report():
    print("Water: " + str(resources["water"]) + " mL.")
    print("Milk: " + str(resources["milk"]) + " mL.")
    print("Coffee: " + str(resources["coffee"]) + " mL.")


def check_available(item):
    water_required = 0
    milk_required = 0
    coffee_required = 0
    if item == "latte" or item == "cappuccino":
        water_required = MENU[item]["ingredients"]["water"]
        milk_required = MENU[item]["ingredients"]["milk"]
        coffee_required = MENU[item]["ingredients"]["coffee"]
    elif item == "espresso":
        water_required = MENU[item]["ingredients"]["water"]
        milk_required = 0
        coffee_required = MENU[item]["ingredients"]["coffee"]
    resources["water"] -= water_required
    resources["milk"] -= milk_required
    resources["coffee"] -= coffee_required
    return water_required, milk_required, coffee_required


def prompt_for_money():
    quarters = int(input("How many quarters: "))
    dimes = int(input("How many dimes: "))
    nickels = int(input("How many nickels: "))
    pennies = int(input("How many pennies: "))
    money_deposited = (quarters * 0.25) + (dimes * 0.10) + (nickels * 0.05) + (pennies * 0.01)
    return money_deposited


def has_enough_money_to_pour(money, item):
    global money_available
    if money >= MENU[item]["cost"]:
        money_available -= MENU[item]["cost"]
        money_available = round(money_available, 2)
        return True
    else:
        return False


while machine_is_on:
    request = input("What would you like? (espresso/latte/cappuccino): ")

    if request == "report":
        print_report()

    elif request == "espresso" or request == "latte" or request == "cappuccino":
        available = check_available(request)
        money_available = prompt_for_money()
        if available and has_enough_money_to_pour(money_available, request):
            print(f"Order approved. Pouring your {request}.")
            print(f"Your change is: ${money_available}.")
        else:
            print("Not enough money.")
            print(f"Returning ${money_available}")

    elif request == "off":
        machine_is_on = False
