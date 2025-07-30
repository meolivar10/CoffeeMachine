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
    "water": 1000,
    "milk": 1000,
    "coffee": 100,
}

# TODO: 1. Print a report of all the coffee machine resource. -- done
# TODO: 2. Make the off functionality to turn off the machine -- done
# TODO: 3. Check if there is enough resources based on the coffee chosen by the user -- done
# TODO: 4: Process the coins put in by the customer - done
# TODO: 5. Check if the coins put in by the customer is enough for the chosen drink. If the amount is greater than the price give the change back - done
# TODO: 6. Make the coffee. Subtract the resources used and add the money that was put in.
def print_report():
    for key in resources:
        if key == "coffee":
            print(f"Coffee: {resources[key]}g")
        elif key == "money":
            print(f"Money: ${resources[key]:.2f}")
        else:
            print(f"{key}: {resources[key]}ml")

def get_insufficient_coffee_resource(coffee_of_choice):
    ingredients = MENU[coffee_of_choice]["ingredients"]
    for key in ingredients:
        if resources[key] < ingredients[key]:
            return key
    return ""

def compute_coin_total():
    print("Please insert coins.")
    quarters = int(input("how many quarters?: "))
    dimes = int(input("how many dimes?: "))
    nickles = int(input("how many nickles?: "))
    pennies = int(input("how many pennies?: "))

    total_cost = (quarters * 0.25) + (dimes * 0.10) + (nickles * 0.05) + (pennies * 0.01)
    return round(total_cost, 2)

def make_coffee(coffee_of_choice):
    print("Make coffee.")
    ingredients = MENU[coffee_of_choice]["ingredients"]
    for key in ingredients:
        resources[key] = resources[key] - ingredients[key]

def run_coffee_machine():
    is_coffee_machine_on = True
    money = 0
    while is_coffee_machine_on:

        coffee = input("What would you like? (espresso/latte/cappuccino?): ")

        if coffee.lower() == "off":
            is_coffee_machine_on = False
        elif coffee.lower() == "report":
            resources["money"] = money
            print_report()
        else:
            resource_lacking = get_insufficient_coffee_resource(coffee)
            if not resource_lacking:
                coin_total = compute_coin_total()
                coffe_cost = MENU[coffee]["cost"]
                if coin_total > coffe_cost:
                    make_coffee(coffee)
                    money += coffe_cost
                    print(f"Here is ${(coin_total - coffe_cost):.2f} in change.")
                    print(f"Here is your {coffee} ☕️. Enjoy!")
                else:
                    print("Sorry that's not enough Money. Money refunded.")
            else:
                print(f"Sorry there is not enough {resource_lacking}.")

run_coffee_machine()