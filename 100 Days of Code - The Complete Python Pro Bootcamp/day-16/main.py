from menu import Menu, MenuItem
from coffee_maker import CoffeeMaker
from money_machine import MoneyMachine

# Creating objects
karen_menu = Menu()
karen_coffeemaker = CoffeeMaker()
karen_moneymachine = MoneyMachine()

is_on = True

while is_on:
    karen_drink = input(f"What would you like? ({karen_menu.get_items()}): ")
    if karen_drink == "off":
        is_on = False
        exit()
    elif karen_drink == "report":
        # TODO 1. Print report
        karen_coffeemaker.report()
        karen_moneymachine.report()
    else:
        # TODO 2. Check resources sufficient?
        karen_drink_available = karen_menu.find_drink(karen_drink)
        karen_resource_sufficient = karen_coffeemaker.is_resource_sufficient(karen_drink_available)

        if karen_resource_sufficient and karen_resource_sufficient:
            # TODO 3. Process coins.
            karen_received_payment = karen_moneymachine.make_payment(karen_drink_available.cost)
            # TODO 4. Check transaction successful?
            if karen_received_payment:
                # TODO 5. Make Coffee.
                karen_coffeemaker.make_coffee(karen_drink_available)
                karen_coffeemaker.report()
                karen_moneymachine.report()
