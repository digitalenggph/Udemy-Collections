import functions
from menu import MENU, resources
from art import coffee_machine
from functions import prompt_order, press_buttons, check_resources, collect_coins, check_coins

# Starting resource
resources_with_money = {}
for resource in resources:
    resources_with_money[resource] = resources[resource]
    resources_with_money['money'] = 0


def coffee_shop_func():
    # TODO: 1. Prompt user by asking “What would you like? (espresso/latte/cappuccino):”
    print(coffee_machine)
    customer_order = input("What would you like? (espresso/latte/cappuccino)\n")
    prompt_order(customer_order)

    # TODO: 2 & 3. Turn off the Coffee Machine by entering “off” to the prompt.
    #              Print report of all coffee machine resources.

    button_pressed = input("Type 'report' to display resources or 'off' to turn off machine.\n")
    press_buttons(button_pressed, resources_with_money)

    # TODO: 4. Check resources sufficient?
    make_order_stats = check_resources(customer_order, MENU[customer_order]["ingredients"], resources_with_money)
    # TODO: 5. Process coins.
    if make_order_stats:
        collected_payment = collect_coins()
        print(collected_payment)
    else:
        print("Resources not enough to make this order, please try again next time.")
        exit()

    # TODO: 6. Check transaction successful?
    transaction_proceed = check_coins(collected_payment, MENU[customer_order]["cost"], resources_with_money['money'])

    if transaction_proceed:
        resources_with_money['money'] += MENU[customer_order]["cost"]
        resources_with_money['water'] -= MENU[customer_order]["ingredients"]['water']
        resources_with_money['coffee'] -= MENU[customer_order]["ingredients"]['coffee']

        if customer_order != 'espresso':
            resources_with_money['milk'] -= MENU[customer_order]["ingredients"]['coffee']

        print(resources_with_money)

        # TODO: 7. Make Coffee.
        functions.coffee_machine_report(resources_with_money)
        print(f"Here's your {customer_order}. Enjoy!")
        next_customer = input("Next customer, pwease?")
        if next_customer == 'y':
            coffee_shop_func()
        else:
            print("Coffee shop is closing, see ya tomorrow!")
            exit()


coffee_shop_func()
