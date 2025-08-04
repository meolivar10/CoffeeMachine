from menu import Menu
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

menu = Menu()
coffee_maker = CoffeeMaker()
money_machine = MoneyMachine()

is_coffee_machine_on = True
money = 0
while is_coffee_machine_on:
    items = menu.get_items()
    coffee = input(f"What would you like? ({items.rstrip(items[-1])}?): ")

    if coffee.lower() == "off":
        is_coffee_machine_on = False
    elif coffee.lower() == "report":
        coffee_maker.report()
        money_machine.report()
    else:
        drink = menu.find_drink(coffee)
        if drink is not None:
            if coffee_maker.is_resource_sufficient(drink):
                if money_machine.make_payment(drink.cost):
                    coffee_maker.make_coffee(drink)